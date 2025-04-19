from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/version")
def app_version():
    return {"version": "1.0.0"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level="info", reload=True)