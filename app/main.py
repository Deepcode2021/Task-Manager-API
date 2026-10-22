from fastapi import FastAPI

app = FastAPI()

# adding the GET/health
# this is the real curl i have seen :)
# curl.exe -X GET http://127.0.0.1:8000/health
@app.get("/health")
def health_check():
    return {"Status": "OK"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "q": q}