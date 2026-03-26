from fastapi import FastAPI
import uvicorn
from TypeDefinations.serverTypes import serverResponse


app = FastAPI()


@app.get("/")
def read_root():
    return serverResponse(success=True, message="Hello, World!")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)