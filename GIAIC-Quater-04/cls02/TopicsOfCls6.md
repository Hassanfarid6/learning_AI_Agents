# 🎓 **Class 06 — Gemini CLI (14 Nov 2025)**
Today’s session focused on working with **Gemini CLI** and exploring useful **Gemini CLI slash commands** for faster AI-assisted development.
~~------------------------------~~
## 🔧 What is `uv`?
`uv` is a modern Python package manager and environment tool. It replaces tools like `pip`, `pipenv`, and `virtualenv` with a **faster, simpler, and more reliable** workflow.

### ⭐ Why use `uv`?
* Ultra-fast package installs
* Built-in virtual environments
* No dependency conflicts
* Cleaner project setup

### 📌 Common `uv` Commands

* `uv init` → Creates a new Python project with recommended structure.
* `uv add <package-name>` → Installs a package and updates your `pyproject.toml`.
* `uv sync` → Installs all dependencies listed in the project configuration.
* `uv venv` → Creates a virtual environment inside the project.

~~------------------------------~~
## 🤖 Gemini CLI — Slash Commands

### 🧭 General
* `/help` — Show all available commands
* `/tools` — List all available tools

### 🧠 Memory (`gemini.md`)
* `/memory add` — Add notes to memory
* `/memory refresh` — Reload memory from files
* `/memory list` — Show all memory file paths

### 💬 Chat Management
* `/chat list` — View saved conversation checkpoints
* `/chat save <tag>` — Save the current chat
* `/chat resume <tag>` — Restore a previous checkpoint

~~------------------------------~~
## ⚙️ More Modes
`!` — Enter shell mode
`Ctrl + Y` — Enter “yolo mode”

📕 Learn more about slash commands & `gemini.md`: [Gemini CLI Command Line Parameters](https://medium.com/google-cloud/gemini-cli-tutorial-series-part-2-gemini-cli-command-line-parameters-e64e21b157be)

~~------------------------------~~
## 💲 Personal Finance Tracker

We also created the entire **Personal Finance Tracker** using **Gemini CLI** — without writing a single line of code. ✨
Following the step-by-step Notion guide, we generated two fully runnable versions:

🌐 **Two versions**
* **CLI version**
* **Web (Streamlit) version**

📕 Guide we followed: [Personal Finance Tracker CLI](https://www.notion.so/Personal-Finance-Tracker-CLI-2aada4c664118005907ce48afdfaba56)

~~------------------------------~~


# 🎓 **Class 07 — MCP & Gemini CLI (21 Nov 2025)**

Today we explored **MCP (Model Context Protocol)** by Anthropic and how Gemini CLI uses it to connect AI agents with tools, data, and external context.
~~------------------------------~~

## 🔧 What is `MCP`?

MCP is a protocol that lets AI agents access **tools, files, APIs, and context** in a **standard, secure, modular** way.

### ⭐ Benefits with AI Agents

* Consistent access to external data
* More reliable tool integrations
* Cleaner, scalable agent workflows

~~------------------------------~~

## 🤖 Gemini CLI + MCP

We connected **context7’s MCP server** with **Gemini CLI** and generated a **personalized Chainlit chatbot** using the class guide.

📕 Guide we followed: [*Personalization Chatbot with Chainlit*](https://www.notion.so/Personalization-Chatbot-with-Chainlit-2b2644e5197680728913dc57ee7df803)


~~-----------------------------                                                             -~~

# 🎓 **Class 08 — Claude Code & Spec-Kit Plus (28 Nov 2025)**

Today’s session explored **Claude Code** and took an overview of **Spec-Kit Plus**, a structured workflow for agent-driven development.
~~------------------------------~~

## 🔧 Installing Claude Code
We installed Claude Code using the [official guide](https://ai-native.panaversity.org/docs/AI-Tool-Landscape/claude-code-features-and-workflows/installation-and-authentication):
```bash
npm install -g @anthropic-ai/claude-code
```
If you don’t have a Claude subscription, you can set up the [**free Claude Code (via Gemini)**](https://ai-native.panaversity.org/docs/AI-Tool-Landscape/claude-code-features-and-workflows/free-claude-setup):
~~------------------------------~~

## 📦 Spec-Kit Plus Overview

Spec-Kit Plus provides a structured Spec-Driven Development workflow.

📕 [Learning resource](https://ai-native.panaversity.org/docs/SDD-RI-Fundamentals/spec-kit-plus-hands-on/spec-kit-plus-foundation)

Install Specify CLI:
```bash
pip install specifyplus
```
Create a project:
```bash
specifyplus init <PROJECT_NAME>
```
Select **Claude** as the coding agent.
~~------------------------------~~

## 🤖 Spec-Kit Plus Slash Commands

### 🧱 Core

* `/sp.constitution` — Set project principles
* `/sp.specify` — Define requirements
* `/sp.plan` — Generate tech plan
* `/sp.tasks` — Create task lists
* `/sp.implement` — Build features

### 🔍 Optional

* `/sp.clarify` — Improve requirements
* `/sp.analyze` — Consistency check
* `/sp.checklist` — Quality validation  
  ~~------------------------------~~

## 🏠 Homework Assignment

1️⃣ Install Claude Code (or connect free via Gemini)
2️⃣ Create a [**Docusaurus**](https://docusaurus.io/) project using SDD
3️⃣ Add **new chapter** with SDD commands
4️⃣ Build & push to GitHub using Claude Code
5️⃣ Deploy to **GitHub Pages** 🚀


~~                                                                          ------------------------------~~


# 🎓 **Class 09 — Qwen CLI & OpenAI ChatKit (05 Dec 2025)**

Today we set up the **Qwen model with Claude Code**, explored the **RAG system pipeline**, and took an overview of **OpenAI ChatKit**.
~~------------------------------~~

## 🔧 Installing Qwen

Install Qwen CLI:

```bash
npm install -g @qwen-code/qwen-code
```

Run & authenticate:

```bash
qwen
```

Set up **Qwen with Claude Code** using these guides:
- [PowerShell (Windows)](https://github.com/DanielHashmi/Q4_learning/blob/main/spec-driven-development/tutorials/How%20to%20Use%20Claude%20Code%20with%20Qwen%20models%20for%20Free%20on%20Windows.md)
- [WSL / Linux / macOS](https://github.com/DanielHashmi/Q4_learning/blob/main/spec-driven-development/tutorials/How%20to%20Use%20Claude%20Code%20with%20Qwen%20models%20for%20Free%20on%20Linux%20and%20macOS%20%28sh%20and%20bash%29.md)

~~------------------------------~~

## 🧠 RAG System Pipeline

* Documents are broken into **chunks**
* Chunks are sent to an **embedding model**
* Generated **vectors** are stored in a **vector database** (with text as metadata)

When the user asks a question:

* User prompt → converted into **vectors**
* **Similar vectors** are searched in the database
* Related **text is fetched from metadata**
* This context is added to the **agent prompt**
* Agent now answers with **higher accuracy**

~~------------------------------~~

## 🏠 Homework Assignment

Create an **agent using OpenAI Agents SDK**, integrate it into a **React/Next.js app using ChatKit**.
⚠️ Everything must be done using **Spec-Driven Development** — **no manual code**.


~~------------------------------~~
