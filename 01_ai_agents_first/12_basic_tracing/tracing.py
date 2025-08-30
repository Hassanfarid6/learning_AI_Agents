import os
from agents import Agent, ModelSettings, trace, Runner, enable_verbose_stdout_logging, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
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

async def main():
    agent = Agent(name="Joke generator", instructions="funny jokes btao in roman urdu.", model=model)

    with trace("Joke workflow"): 
        first_result = await Runner.run(agent, "Tell me a joke")
        second_result = await Runner.run(agent, f"Rate this joke: {first_result.final_output}")
        print(f"Joke  ==>>: {first_result.final_output}")
        print(f"Rating ==>>: {second_result.final_output}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())