from fastapi import FastAPI

app = FastAPI(
    title="AlgoVault API",
    description="Intelligent Algorithm & Data Structure Engine",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "name": "AlgoVault",
        "message": "Intelligent Algorithm & Data Structure Engine",
        "version": "0.1.0",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "algovault-api",
    }