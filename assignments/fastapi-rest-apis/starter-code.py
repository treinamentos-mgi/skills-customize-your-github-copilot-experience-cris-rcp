from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    description: str = ""
    completed: bool = False


class Task(TaskCreate):
    id: int


tasks = [
    Task(
        id=1,
        title="Learn FastAPI",
        description="Build the first API route",
        completed=False,
    )
]
next_task_id = 2


@app.get("/")
def read_root():
    return {"message": "Task API is running"}


# TODO: Add GET /tasks and POST /tasks.
# TODO: Add GET, PUT, and DELETE routes for /tasks/{task_id}.