from datetime import datetime
from fastapi import FastAPI, status
from typing import Optional
from pydantic import BaseModel, Field

app = FastAPI()

task_db = []
id_counter = 1

class taskCreate(BaseModel):
    title: str = Field(min_length=2)
    description: Optional[str] = None
    completed: bool = False


# adding the GET/health
# this is the real curl i have seen :)
# curl.exe -X GET http://127.0.0.1:8000/health
@app.get("/health")
def health_check():
    return {"Status": "OK"}


@app.post("/task", status_code=status.HTTP_201_CREATED)
def create_task(task: taskCreate):
    # return {"message": "Task created", "task_data": task}
    global id_counter

    new_task = {
        "id": id_counter,
        "title": task.title,
        "description": task.description,
        "completed": task.completed,
        "created_at": datetime.now().isoformat(),
    }

    task_db.append(new_task)
    id_counter += 1
    return new_task

