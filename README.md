# Prompt Generator

An intelligent prompt generation tool designed to assist developers with various software development tasks. This tool specializes in generating optimized prompts for code generation, bug fixing, and project architecture planning using OpenAI's API.

Prompt Generator acts as your personal AI programming assistant, helping you:
- Generate clean, efficient, and well-documented code across multiple programming languages
- Debug issues systematically with step-by-step guidance
- Design scalable software architectures with best practices and modern design patterns
- Save time by automating repetitive development tasks
- Learn better coding practices through AI-generated explanations and recommendations

## Features

- **Code Generation**: Creates detailed prompts for generating high-quality, efficient code following best practices
- **Bug Fixing**: Generates systematic debugging prompts with step-by-step approaches
- **Project Architecture**: Helps design comprehensive project structures and tech stack recommendations

## Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/LEO2822/Prompt-Generator.git
   cd Prompt-Generator
   ```

2. Install uv (Python packaging tool):
   Visit [uv Installation Guide](https://docs.astral.sh/uv/getting-started/installation/) for detailed installation instructions.

   Quick install commands:
   - Linux/macOS:
     ```bash
     curl -LsSf https://astral.sh/uv/install.sh | sh
     ```
   - Windows (PowerShell):
     ```powershell
     powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
     ```

3. Install dependencies and run:
   ```bash
   uv sync
   uv run main.py
   ```

4. Create a `.env` or edit `.env.local` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Requirements
- Python 3.12.x
- OpenAI API key
- uv package manager