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

~~------------------------------~~