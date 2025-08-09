# Yeh teen example batate hain ke Agents SDK mein hum different LLM provider (yahan Gemini) ko kaise 
# set kar sakte hain — aur yeh kaam teen levels pe hota hai:

# 1️⃣ Agent Level
# Sirf ek specific agent ke liye provider set karte ho.

# Har agent apne liye custom LLM use karega.
# Advantage: Flexible — har agent alag model use kar sakta hai.

# agent = Agent(
#     name="Assistant",
#     instructions="You only respond in haikus.",
#     model=OpenAIChatCompletionsModel(
#         model="gemini-2.0-flash",
#         openai_client=client
#     ),
# )

# 2️⃣ Run Level
# Jab agent ko run karte ho, us waqt provider set kar dete ho.
# Ek hi agent alag-alag runs me different models use kar sakta hai.
# Advantage: Runtime pe control.

# config = RunConfig(
#     model=model,
#     model_provider=external_client,
#     tracing_disabled=True
# )

# result = Runner.run_sync(agent, "Hello", run_config=config)
# 3️⃣ Global Level
# Poore project ke liye default provider set kar dete ho.

# Har agent yahi default provider use karega (jab tak override na karein).

# Advantage: Sab agents ek hi config follow karenge.
# set_default_openai_client(external_client)
# agent = Agent(name="Assistant", instructions="You are a helpful assistant", model="gemini-2.0-flash")


# 💡 Summary in one line:
# Agent Level: Har agent apna model rakhta hai.
# Run Level: Model run ke time decide hota hai.
# Global Level: Sab agents ek hi model use karte hain by default.


# 01: AGENT LEVEL
import asyncio
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

gemini_api_key = ""

#Reference: https://ai.google.dev/gemini-api/docs/openai
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_tracing_disabled(disabled=True)

async def main():
    # This agent will use the custom LLM provider
    agent = Agent(
        name="Assistant",
        instructions="You only respond in haikus.",
        model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
    )

    result = await Runner.run(
        agent,
        "Tell me about recursion in programming.",
    )
    print(result.final_output)


# if __name__ == "__main__":
#     asyncio.run(main())

# 2. RUN LEVEL
# from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

gemini_api_key = ""

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

agent: Agent = Agent(name="Assistant", instructions="You are a helpful assistant")

result = Runner.run_sync(agent, "Hello, how are you.", run_config=config)

print(result.final_output)


# 03 Globle Level

from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, set_default_openai_api

gemini_api_key = ""
set_tracing_disabled(True)
set_default_openai_api("chat_completions")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
set_default_openai_client(external_client)

agent: Agent = Agent(name="Assistant", instructions="You are a helpful assistant", model="gemini-2.0-flash")

result = Runner.run_sync(agent, "Hello")

print(result.final_output)

