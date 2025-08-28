
import os
import asyncio
from dotenv import load_dotenv, find_dotenv
from dataclasses import dataclass
from pydantic import BaseModel
from agents import Agent, Runner, enable_verbose_stdout_logging, RunContextWrapper, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled, function_tool, ModelSettings

_: bool = load_dotenv(find_dotenv())

gemini_api_key: str | None = os.environ.get("GEMINI_API_KEY")
enable_verbose_stdout_logging()

class myContext(BaseModel):
    inputType: str
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

def check_enable(contxt: RunContextWrapper, agent: Agent) -> bool:
    if contxt.context.inputType == "weather":
        return True
    elif contxt.context.inputType == "none":
        return True
    else:
        return False

@function_tool(is_enabled=check_enable)
# @function_tool(is_enabled=False)
# @function_tool
def get_current_weather(location: str, unit: str = "celsius") -> str:
    """Get the current weather in a given location"""
    # For the sake of this example, we'll return a hardcoded response.
    return f"The current weather in {location} is 28 degrees {unit} with clear skies."

@function_tool(is_enabled=check_enable)
def get_weather(location: str, unit: str = "celsius") -> str:
    """Get the current weather in a given location"""
    # For the sake of this example, we'll return a hardcoded response.
    return f"The weather in {location} is sunny with a temperature of 25 degrees {unit}._"

async def main() -> None:
    # 3. Which Agent?
    agent: Agent = Agent(
        name="WeatherAgent",
        model_settings=ModelSettings(tool_choice="required"),
        # model_settings=ModelSettings(tool_choice="auto"),
        model=model,
        tools=[get_current_weather, get_weather],
    )
    context = myContext(
        # inputType="weather"
        inputType="none"
    )
    result = await Runner.run(
        starting_agent=agent,
        input="What's the weather in Karachi?",
        context=context
    )

    print("🤖 Agent Output:", result.final_output)
    
    

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
    