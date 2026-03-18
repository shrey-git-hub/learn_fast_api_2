from fastapi import FastAPI, Request

app = FastAPI(
    title="My Notes API",
    description="A simple API for managing notes, built with FastAPI.",
    version="1.0.0"
)

@app.middleware("http")
async def request_logging_middleware(request: Request, call_next):
    print(f"INFO: Request: {request.method} {request.url.path}")
    response = await call_next(request)
    return response


@app.get("/ping")
def read_root():
    return {"message": "Pong"}