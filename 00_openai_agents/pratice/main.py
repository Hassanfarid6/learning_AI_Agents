
import os
import asyncio
from dotenv import load_dotenv, find_dotenv
from dataclasses import dataclass
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled, function_tool, ModelSettings

_: bool = load_dotenv(find_dotenv())

gemini_api_key: str | None = os.environ.get("GEMINI_API_KEY")

# Tracing disabled
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

def Sdk_Key(weather: str) -> bool:
    if weather == "weather":
        return True
    else:
        return False

@function_tool(is_enabled=Sdk_Key("weather"))
def get_current_weather(location: str, unit: str = "celsius") -> str:
    """Get the current weather in a given location"""
    # For the sake of this example, we'll return a hardcoded response.
    return f"The current weather in {location} is 28 degrees {unit} with clear skies."

async def main() -> None:
    # 3. Which Agent?
    agent: Agent = Agent(
        name="WeatherAgent",
        model_settings=ModelSettings(tool_choice="required"),
        model=model,
        tools=[get_current_weather],
    )
    result = await Runner.run(
        starting_agent=agent,
        input="What's the weather in Karachi?"
    )

    print("🤖 Agent Output:", result.final_output)
    
    

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
    