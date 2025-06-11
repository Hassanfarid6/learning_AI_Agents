uv init --package myproject

cd myproject

uv add litellm

uv venv

uv pip install python-dotenv

uv add agents

uv python install 3.7
uv python use 3.7

TensorFlow 1.15 only supports Python versions up to 3.7. To fix this, you need to switch to a compatible Python version (e.g., Python 3.7 or 3.8) in your uv environment.

in .toml files
<!-- [project] -->
requires-python = ">=3.7,<3.8"

uv pip install tensorflow==1.15 --no-deps


source .venv\Scripts\activate

uv run openai

uv run gemini

uv run gemini2