from openai import OpenAI
import os
import datetime
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

client = OpenAI()


def generate_prompt(task_type, user_input):
    """
    Generate a detailed and optimized prompt based on the task type and user input.

    Args:
        task_type (str): The type of task (code_generation, bug_fixing, project_architecture).
        user_input (str): Context or description provided by the user.

    Returns:
        str: The generated prompt.
    """

    system_messages = {
        "code_generation": """You are an expert software engineer specializing in generating high-quality, efficient, and contextually accurate code based on user requirements. Your expertise spans multiple programming languages and paradigms. When generating code, you should:
        1. Consider best practices and design patterns appropriate for the task.
        2. Optimize for readability, maintainability, and performance.
        3. Include inline comments explaining complex logic.
        4. Suggest appropriate error handling and input validation.
        5. Consider scalability and potential future extensions.
        6. Adhere to language-specific style guides and conventions.""",
        "bug_fixing": """You are an expert software developer who provides comprehensive, step-by-step debugging prompts to solve programming issues. Your approach should include:
        1. Asking for relevant code snippets, error messages, and context.
        2. Suggesting debugging techniques like logging, breakpoints, or unit tests.
        3. Providing a systematic approach to isolate the problem.
        4. Explaining potential causes of the bug and their likelihood.
        5. Offering multiple solutions when applicable, with pros and cons for each.
        6. Recommending best practices to prevent similar bugs in the future.
        7. Suggesting tools or libraries that could help in debugging or preventing similar issues.""",
        "project_architecture": """You are an experienced software architect who creates detailed project architectures, including tech stacks, directory structures, dependencies, and documentation. Your expertise covers:
        1. Analyzing project requirements and constraints.
        2. Recommending appropriate tech stacks based on project needs and scalability.
        3. Designing modular and maintainable directory structures.
        4. Specifying clear interfaces between components and services.
        5. Considering security, performance, and scalability in the architecture.
        6. Suggesting appropriate design patterns and architectural styles (e.g., microservices, event-driven).
        7. Providing guidance on version control strategies and branching models.
        8. Recommending CI/CD pipelines and deployment strategies.
        9. Outlining necessary documentation, including API docs, architecture diagrams, and developer guides.
        10. Considering cross-cutting concerns like logging, monitoring, and error handling.""",
    }

    if task_type not in system_messages:
        raise ValueError(
            "Invalid task type. Choose from: 'code_generation', 'bug_fixing', or 'project_architecture'."
        )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_messages[task_type]},
            {
                "role": "user",
                "content": f"Generate a detailed and optimized prompt based on this input: {user_input}",
            },
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content


def save_prompt_to_markdown(task_type, prompt):
    """
    Save the generated prompt to a markdown file.

    Args:
        task_type (str): The type of task for which the prompt was generated.
        prompt (str): The generated prompt.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    filename = f"generated_prompts/{task_type}_prompt_{timestamp}.md"

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w") as file:
        file.write(f"# {task_type.capitalize()} Prompt\n\n")
        file.write(f"**Generated on:** {timestamp}\n\n")
        file.write("## Optimized Prompt\n")
        file.write(f"```\n{prompt}\n```\n")

    print(f"Prompt saved to {filename}")


if __name__ == "__main__":
    print("Welcome to the AI Developer Prompt Generator!")
    print("Choose a task type:")
    print("1. Code Generation")
    print("2. Bug Fixing")
    print("3. Project Architecture")

    # Get user choice
    task_choice = input("Enter the number corresponding to your choice: ").strip()
    task_map = {"1": "code_generation", "2": "bug_fixing", "3": "project_architecture"}

    # Validate user choice
    if task_choice not in task_map:
        print("Invalid choice. Please run the script again.")
        exit()

    task_type = task_map[task_choice]
    user_input = input(
        f"Enter a description or context for {task_type.replace('_', ' ')}: "
    ).strip()

    # Generate the prompt
    print("\nGenerating your optimized prompt...")
    generated_prompt = generate_prompt(task_type, user_input)
    print("\nGenerated Prompt:")
    print(generated_prompt)

    # Save the prompt to a markdown file
    save_prompt_to_markdown(task_type, generated_prompt)
