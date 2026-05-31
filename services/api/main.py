from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok", "service": "api"}


@app.get("/")
def root():
    return {"message": "DevOps Monorepo API"}
