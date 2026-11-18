import sqlite3
from contextlib import contextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field

DATABASE_PATH = Path(__file__).with_name("tasks.db")
app = FastAPI(title="Task API with SQLite")


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    description: str = ""
    completed: bool = False


class Task(TaskCreate):
    id: int


@contextmanager
def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


def initialize_database():
    with get_connection() as connection:
        # TODO: Create the tasks table with the required columns.
        pass


initialize_database()


@app.get("/")
def read_root():
    return {"message": "Task API with SQLite is running"}


# TODO: Add GET /tasks and POST /tasks.
# TODO: Add GET, PUT, and DELETE routes for /tasks/{task_id}.