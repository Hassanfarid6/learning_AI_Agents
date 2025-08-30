# Agents as a Tool

“**Agents as a tool**” means you let one agent **call another agent like a function**—without giving away control of the conversation. It’s perfect when you want a **main agent** 🧑‍💼 to stay in charge while **specialist agents** do small, focused jobs (translate this, extract dates, summarize, etc.).

---

## 💡Why do we need “agents as a tool”?

Think of your main agent as a **project manager** 📋 and specialist agents as **skilled contractors** 🛠:

- **Keep control** 🕹 — The manager (main agent) keeps the mic 🎤 and just “uses” specialists when needed, instead of transferring the whole call to another department (that’s a *handoff*).
- **Modular skills** 🧩 — You can plug in a translator, date-extractor, code fixer—each as its own small agent.
- **Deterministic orchestration** 🎯 — You decide when and how sub-agents are used, while still enjoying tool-calling smarts.
- **Cleaner prompts** ✍ — Each specialist keeps a sharp instruction (e.g., “only translate”), which is easier to get right.

When tasks are **open-ended** or require long multi-step work, you may prefer *handoffs* (let a different agent take over). But when you just need a **quick capability** from a specialist while staying in one flow, “agents as a tool” shines.

---

## 🧠 The mental model (analogy)

- **Handoff** = transferring the caller to another department to finish the conversation.
- **Agent as a tool** = putting the caller on mute, asking a colleague for a quick answer, then **you** reply back to the caller.
    
    ✅  Main agent keeps context and tone while borrowing skills from specialists.
    

---

## 🛠 Core idea from the SDK

- The SDK explicitly supports *Agents as tools*: an **agent can be turned into a tool** that other agents can call.
- There’s a **convenience method** `agent.as_tool(...)` to wrap an agent as a tool quickly. If you need advanced control, implement a tool that **runs the agent via `Runner.run` directly** (e.g., custom `max_turns`).

---




---

## 🆚 When should beginners choose “agents as tools” vs “handoffs”?

| Scenario | Prefer… | Why |
| --- | --- | --- |
| One main voice; quick subtask (translate, extract, reformat) | **Agents as tools** | Main agent stays in charge, borrows a capability briefly. |
| Long, specialized conversation (e.g., billing agent should take over) | **Handoffs** | The flow moves to a specialized agent to finish the turn(s). |

---

## 🕵Important knobs & gotchas (beginner traps)

- **⚙ Tool choice**: You can force or forbid tool use via `model_settings.tool_choice` (`"auto"`, `"required"`, `"none"`, or a specific tool name). Great for tests and guardrails.
- **🔄 Auto reset after a tool**: To avoid infinite loops, the SDK **resets** `tool_choice` to `"auto"` after a tool call; you can change this or even stop after the first tool by setting `Agent.tool_use_behavior="stop_on_first_tool"`.
- **⚡ Convenience vs control**: `agent.as_tool(...)` is quick but doesn’t expose everything (e.g., `max_turns`). For full control, call `Runner.run(...)` **inside** your tool.
- **🔍 Tracing**: Use traces to see when your main agent called sub-agents and what they returned—super helpful for debugging beginner mistakes.

---

## 🏗 Step-by-step mini-lesson

1. **Start small**
    
    Create two tiny specialists (e.g., “Lowercaser” and “Title-Caser”). Wrap them with `as_tool`. Ask your orchestrator to choose.
    
2. **Add a “real” skill**
    
    Replace one toy tool with a real capability (e.g., “Summarizer” or “Translator” agent).
    
3. **Introduce control**
    
    Force the orchestrator to use a tool (`tool_choice="required"`) and see how behavior changes.
    
4. **Switch to advanced pattern**
    
    Re-implement one tool as a **function tool** that runs a sub-agent with `Runner.run(...)` to cap `max_turns` or to post-process output.
    
5. **Inspect with tracing**
    
    Open the trace viewer and identify each tool call and result.
    

---

## 📦 Starter template you can copy

```python
from agents import Agent, Runner, function_tool

# 1) Specialists
summer = Agent(
    name="Summarizer",
    instructions="Summarize in 3 bullet points. No extra text."
)
detect_lang = Agent(
    name="Language Detector",
    instructions="Return the ISO language code for the given text."
)

# 2) Wrap as tools (quick pattern)
summarize_tool = summer.as_tool("summarize", "Summarize in 3 bullets.")
detect_tool = detect_lang.as_tool("detect_language", "Detect language code.")

# 3) Main agent
coach = Agent(
    name="Coach",
    instructions=("Help the user polish writing. If they say 'summarize', call summarize. "
                  "If they ask 'what language', call detect_language. Otherwise, respond normally."),
    tools=[summarize_tool, detect_tool],
)

# 4) Run
# result = await Runner.run(coach, "Summarize: Large language models are...")
# print(result.final_output)

```

If later you need stricter control, replace a tool with a `@function_tool` that calls `Runner.run(...)` for the sub-agent.

---

## 🏁 Wrap-up

- **📌 What it is**: Treat other agents like **callable tools** to keep orchestration in one place.
- **✅ When to use**: Short, focused subtasks—translate, extract, format—while preserving one conversational owner.
- **🔨 How to do it**: Start with `agent.as_tool(...)`; switch to a function tool that calls `Runner.run(...)` when you need more control.

If you want, I can turn this into a printable cheat-sheet or a small lab with checkpoints and expected outputs.