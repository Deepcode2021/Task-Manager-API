# Task Manager API
This is a Task Manager API the further extension of the Student Managment CLI 
[Repository](https://github.com/Deepcode2021/student-managment-cli)

#### I will be documenting what i am building here from what i learned and how i created this

## PHASE 0
In this i have learn about some of the basics of what i have to know like 

What is **GET  POST  PUT  PATCH  DELETE**

 - GET is a like getting information from the API
 - POST is to create something in the API server 
 - PUT is used to fully replace something in the server
 - PATCH is for modifing specific data in the server
 - DELETE as name suggests to delete a data
 
 so this is about the the methods we can use
### There is status codes like **200 201 204 400 404 500**
 this are reponse from the server side through API

Now what is a path parameters vs query parameters vs request bodies

  
|Path Parameter| Query Parameter | Request Body |
|--|--|--|
| Inside the URL pathAt  | the end of URL after `?` | Separate HTTP payload |

also i am learning the the markdown editing things 
so did some practice over the json module 

| Action | HTTP Verb | Resource URL | Request Body | Success Status |
|---|---|---|---|---|
| Get all tasks | GET | `/tasks` | None | 200 OK |
| Get specific task | GET | `/tasks/:id` | None | 200 OK |
| Create new task | POST | `/tasks` | `{ "title": "..." }` | 201 Created |
| Replace full task | PUT | `/tasks/:id` | Full `{ "title": "...", ... }` | 200 OK |
| Update partial task | PATCH | `/tasks/:id` | Partial `{ "completed": true }` | 200 OK |
| Delete task | DELETE | `/tasks/:id` | None | 204 No Content 


## API endpoints 


| Method | Endpoint | Behavior |
| --- | --- | --- |
| GET | `/health` | Health response |
| POST | `/tasks` | Create task |
| GET | `/tasks` | List tasks |
| GET | `/tasks/{task_id}` | Retrieve one task |
| PUT | `/tasks/{task_id}` | Update task |
| DELETE | `/tasks/{task_id}` | Delete task |

now consider i ID doesn't exits what will i do 
: maybe throw an **ERROR** saying "ID NOT FOUND"
everything comes under the edge cases here 

so lets start building the API 

## Installation
    
First i need to install the Fast API and Uvicorn 
    
Running this command install the Fast api but here i choose the bare pakage as this way i can learn what is this things easily *as per the AI(Gemini)*
 
    ```bash
    pip install fastapi uvicorn
    ```
