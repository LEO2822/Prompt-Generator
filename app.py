# create a fastapi application that will use the prompt_generator.py file to generate prompts

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from prompt_generator import generate_prompt
from typing import Optional

app = FastAPI(
    title="Prompt Generator API",
    description="API for generating various types of prompts",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class PromptRequest(BaseModel):
    task_type: str
    user_input: str

# Response model
class PromptResponse(BaseModel):
    prompt: str
    task_type: str
    status: str = "success"
    error: Optional[str] = None

@app.get("/")
def read_root():
    return {
        "message": "Welcome to Prompt Generator API",
        "status": "active",
        "version": "1.0.0"
    }

@app.post("/generate_prompt", response_model=PromptResponse)
async def create_prompt(request: PromptRequest):
    try:
        generated_prompt = generate_prompt(request.task_type, request.user_input)
        return PromptResponse(
            prompt=generated_prompt,
            task_type=request.task_type
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate prompt: {str(e)}"
        )

@app.get("/supported_tasks")
def get_supported_tasks():
    return {
        "supported_tasks": [
            "code_generation",
            "bug_fixing",
            "project_architecture"
        ]
    }
