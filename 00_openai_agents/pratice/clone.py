import os
from agents import Agent, ModelSettings, Runner, enable_verbose_stdout_logging, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env file
load_dotenv(find_dotenv())


gemini_api_key: str | None = os.environ.get("GEMINI_API_KEY")
# enable_verbose_stdout_logging()

set_tracing_disabled(disabled=True)

# 1. Which LLM Service?
external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

# 2. Which LLM Model?
model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
      )

base_agent = Agent(
    name="BaseAssistant",
    instructions="You are a helpful assistant.",
    model=model,
    model_settings=ModelSettings(temperature=0.7)
)

# Simple clone
friendly_agent = base_agent.clone(
    name="FriendlyAssistant",
    instructions="You are a very friendly and warm assistant."
)

# Test both agents
query = "Hello, how are you?"

result_base = Runner.run_sync(base_agent, query)
result_friendly = Runner.run_sync(friendly_agent, query)

print("Base Agent:", result_base.final_output)
print("Friendly Agent:", result_friendly.final_output)

# Create a base agent
# base_agent = Agent(
#     name="BaseAssistant",
#     instructions="You are a helpful assistant.",
#     model=model,
#     model_settings=ModelSettings(temperature=0.7)
# )

# # Create 3 different variants
# variants = {
#     "Poet": base_agent.clone(
#         name="Poet",
#         instructions="You are a poet. Respond in verse.",
#         model_settings=ModelSettings(temperature=0.9)
#     ),
#     "Scientist": base_agent.clone(
#         name="Scientist", 
#         instructions="You are a scientist. Be precise and factual.",
#         model_settings=ModelSettings(temperature=0.1)
#     ),
#     "Chef": base_agent.clone(
#         name="Chef",
#         instructions="You are a chef. Talk about food and cooking."
#     )
# }

# # Test all variants

# query = "What is love? in roman urdu"

# for name, agent in variants.items():
#     result = Runner.run_sync(agent, query)
#     print(f"\n{name}:")
#     print(result.final_output)