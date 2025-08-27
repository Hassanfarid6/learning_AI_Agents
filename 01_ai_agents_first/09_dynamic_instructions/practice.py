import os
from dotenv import load_dotenv
from agents import RunContextWrapper, Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled
load_dotenv()
set_tracing_disabled(disabled=True)  # Optional: Disable tracing for cleaner output (good for beginners)

external_client: AsyncOpenAI = AsyncOpenAI(
    api_key = os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
model = OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=external_client)


# def my_dynamic_instructions(context: RunContextWrapper, agent: Agent) -> str:
#     return f"You are {agent.name}. You love helping people learn Python!"


def message_count_aware(context: RunContextWrapper, agent: Agent) -> str:
    message_count = len(getattr(context, 'messages', []))
    
    if message_count == 0:
        return "You are a welcoming assistant. Say hello!"
    else:
        
        return f"You are an assistant. This is message #{message_count}. Be helpful!"

# agent = Agent(
#     name="Message Counter",
#     instructions=message_count_aware
# )

def main():
    """Learn Dynamic Instructions with simple examples."""
     # 🌿 Dynamic Instructions Example
     # Here, we define instructions that change based on the agent's name and context.
     # This allows for more personalized and context-aware interactions.
    agent = Agent(
        # name="Python Helper",
        # instructions=my_dynamic_instructions,
        name="Message Counter",
        instructions=message_count_aware,
        model=model
    )
    result = Runner.run_sync(agent, "What is a function?")
    print(result.final_output)


if __name__ == "__main__":
    main()
