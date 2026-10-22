
# Task Manager API

This is a Task Manager API, a further extension of the [Student Management CLI](https://github.com/Deepcode2021/student-managment-cli).

I will be documenting what I am building here based on what I learn and how I create it.

---

## PHASE 0

In this phase, I learned the basics of what I need to know:

### HTTP Methods: GET, POST, PUT, PATCH, DELETE

- **GET:** Retrieve information from the API server.
- **POST:** Create a new resource on the server.
- **PUT:** Fully replace an existing resource on the server.
- **PATCH:** Modify specific fields of an existing resource on the server.
- **DELETE:** Remove a resource from the server.

---

### Status Codes: 200, 201, 204, 400, 404, 500

These are standardized server responses sent back through the API.

---

### Path Parameters vs Query Parameters vs Request Bodies

| Path Parameter | Query Parameter | Request Body |
|---|---|---|
| Inside the URL path | At the end of URL after `?` | Separate HTTP payload |

---

### REST Actions Mapping

| Action | HTTP Verb | Resource URL | Request Body | Success Status |
|---|---|---|---|---|
| Get all tasks | GET | `/tasks` | None | 200 OK |
| Get specific task | GET | `/tasks/:id` | None | 200 OK |
| Create new task | POST | `/tasks` | `{ "title": "..." }` | 201 Created |
| Replace full task | PUT | `/tasks/:id` | Full `{ "title": "...", ... }` | 200 OK |
| Update partial task | PATCH | `/tasks/:id` | Partial `{ "completed": true }` | 200 OK |
| Delete task | DELETE | `/tasks/:id` | None | 204 No Content |

---

## API Endpoints

| Method | Endpoint | Behavior |
|---|---|---|
| GET | `/health` | Health response |
| POST | `/tasks` | Create task |
| GET | `/tasks` | List tasks |
| GET | `/tasks/{task_id}` | Retrieve one task |
| PUT | `/tasks/{task_id}` | Update task |
| DELETE | `/tasks/{task_id}` | Delete task |

Now, consider what happens if an ID doesn't exist:
- Throw an **ERROR** with status code `404 Not Found` and message `"Task not found"`.

These edge cases need to be handled carefully.

---

## Installation

First, install FastAPI and Uvicorn. Installing bare packages helps in understanding how each component works individually:

```bash
pip install fastapi uvicorn
```
To run this main.py by this command
```bash
uvicorn main:app --reload
```
i also learn about the requirements.txt from this u can install the required pakages from below command
```bash
pip install -r requirements.txt
```

### Now starting to build something
lets start with GET/health
```python
@app.get("/health")
	def  health_check():
		return  {"Status":  "OK"}
```
Running this curl command gives the feedback
```bash
curl.exe -X GET http://127.0.0.1:8000/health
```
