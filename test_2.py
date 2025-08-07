from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Your sample endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, Prometheus!"}

# Instrumentation for /metrics
Instrumentator().instrument(app).expose(app)
