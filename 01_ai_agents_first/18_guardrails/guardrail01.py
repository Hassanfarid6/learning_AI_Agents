from pydantic import BaseModel
import os
from dotenv import load_dotenv, find_dotenv 
from agents import (
    Agent,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    RunContextWrapper,
    Runner,
    TResponseInputItem,
    input_guardrail,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
)

gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")

# 1. Which LLM Service?
external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# 2. Which LLM Model?
llm_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)


# Define what our guardrail should output
class MathHomeworkOutput(BaseModel):
    is_math_homework: bool
    reasoning: str

# Create a simple, fast agent to do the checking
guardrail_agent = Agent( 
    name="Homework Police",
    instructions="Check if the user is asking you to do their math homework.",
    output_type=MathHomeworkOutput,
    model=llm_model
)

# Create our guardrail function
@input_guardrail
async def math_guardrail( 
    ctx: RunContextWrapper[None], 
    agent: Agent, 
    input: str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    # Run our checking agent
    result = await Runner.run(guardrail_agent, input, context=ctx.context)
    
    # Return the result with tripwire status
    return GuardrailFunctionOutput(
        output_info=result.final_output, 
        tripwire_triggered=result.final_output.is_math_homework,  # Trigger if homework detected
    )

# Main agent with guardrail attached
customer_support_agent = Agent(  
    name="Customer Support Specialist",
    instructions="You are a helpful customer support agent for our software company.",
    input_guardrails=[math_guardrail],  # Attach our guardrail
    model=llm_model
)

# Testing the guardrail
async def test_homework_detection():
    try:
        # This should trigger the guardrail
        res = await Runner.run(customer_support_agent, "Can you solve 2x + 3 = 11 for x?")
        print("❌ Guardrail failed - homework request got through!", res)
    
    except InputGuardrailTripwireTriggered:
        print("✅ Success! Homework request was blocked.")
        # Handle appropriately - maybe send a polite rejection message