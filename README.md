# Mervin AI Developer

An intelligent prompt generation tool designed to assist developers with various software development tasks. This tool specializes in generating optimized prompts for code generation, bug fixing, and project architecture planning using OpenAI's API.

## Features

- **Code Generation**: Creates detailed prompts for generating high-quality, efficient code following best practices
- **Bug Fixing**: Generates systematic debugging prompts with step-by-step approaches
- **Project Architecture**: Helps design comprehensive project structures and tech stack recommendations

## Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/mervin-ai-developer.git
   cd mervin-ai-developer
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install openai python-dotenv
   ```

4. Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

5. Run the application:
   ```bash
   python main.py
   ```

## Requirements
- Python 3.x
- OpenAI API key
- python-dotenv

## Note
Make sure to keep your API key confidential and never commit it to version control.