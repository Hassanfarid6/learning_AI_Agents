import os
from pydantic import BaseModel
from agents import Agent, Runner, input_guardrail, GuardrailFunctionOutput, RunConfig
from agents import AsyncOpenAI, OpenAIChatCompletionsModel
from dotenv import load_dotenv, find_dotenv

# Load API key
load_dotenv(find_dotenv())
gemini_api_key: str | None = os.environ.get("GEMINI_API_KEY")

# External client (Google Gemini via OpenAI wrapper)
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Model
model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)

# RunConfig
config = RunConfig(model=model)

# -------------------------
# Step 1: Guardrail Output Type
# -------------------------
class MedicineOutput(BaseModel):
    response: str
    isMedicineQuery: bool

# -------------------------
# Step 2: Guardrail Agent
# -------------------------
guardrail_agent = Agent(
    name="Guardrail Agent",
    instructions="Allow only queries related to medicine. Block everything else.",
    output_type=MedicineOutput,
    model=model
)

# -------------------------
# Step 3: Input Guardrail Function
# -------------------------
@input_guardrail
async def medicine_guardrail(ctx, agent, input) -> GuardrailFunctionOutput:
    result = await Runner.run(guardrail_agent, input, run_config=config)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.isMedicineQuery
    )

# -------------------------
# Step 4: Medicine Agent
# -------------------------
medicine_agent = Agent(
    name="Medicine Agent",
    instructions="You are a medicine expert. Answer only medicine related queries.",
    model=model
)

# -------------------------
# Step 5: Triage Agent (with Guardrail)
# -------------------------
triage_agent = Agent(
    name="Triage Agent",
    instructions="Route queries to correct agents.",
    handoffs=[medicine_agent],
    input_guardrails=[medicine_guardrail]
)

# -------------------------
# Step 6: Run
# -------------------------
response = Runner.run_sync(
    starting_agent=triage_agent,
    input="What is the best medicine for cold?",
    run_config=config
)

print(response.final_output)