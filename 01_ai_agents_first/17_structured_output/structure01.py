import os
import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled, ModelSettings, function_tool

# 🌿 Load environment variables
load_dotenv()
set_tracing_disabled(disabled=True)

# 🔐 Setup Gemini client
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

external_client = AsyncOpenAI(api_key=GEMINI_API_KEY, base_url=BASE_URL)
llm_model = OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=external_client)


from pydantic import BaseModel
from agents import Agent, Runner
from typing import List, Optional
class ActionItem(BaseModel):
    task: str
    assignee: str
    due_date: Optional[str] = None
    priority: str = "medium"

class Decision(BaseModel):
    topic: str
    decision: str
    rationale: Optional[str] = None

class MeetingMinutes(BaseModel):
    meeting_title: str
    date: str
    attendees: List[str]
    agenda_items: List[str]
    key_decisions: List[Decision]
    action_items: List[ActionItem]
    next_meeting_date: Optional[str] = None
    meeting_duration_minutes: int

# Meeting minutes extractor
agent = Agent(
    name="MeetingSecretary",
    instructions="""Extract structured meeting minutes from meeting transcripts.
    Identify all key decisions, action items, and important details.""",
    model=llm_model,
    output_type=MeetingMinutes
)

meeting_transcript = """
Marketing Strategy Meeting - January 15, 2024
Attendees: Sarah (Marketing Manager), John (Product Manager), Lisa (Designer), Mike (Developer)
Duration: 90 minutes

Agenda:
1. Q1 Campaign Review
2. New Product Launch Strategy  
3. Budget Allocation
4. Social Media Strategy

Key Decisions:
- Approved $50K budget for Q1 digital campaigns based on strong ROI data
- Decided to launch new product in March instead of February for better market timing
- Will focus social media efforts on Instagram and TikTok for younger demographics

Action Items:
- Sarah to create campaign timeline by January 20th (high priority)
- John to finalize product features by January 25th
- Lisa to design landing page mockups by January 22nd
- Mike to review technical requirements by January 30th

Next meeting: January 29, 2024
"""

result = Runner.run_sync(agent, meeting_transcript)

print("=== Meeting Minutes ===")
# print(f"---->>: {', '.join(result.final_output.attendees)} attended the {result.final_output.meeting_title} on {result.final_output.date}.")
print(f"Meeting Minutes: {result.final_output}")