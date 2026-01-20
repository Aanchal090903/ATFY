from fastapi import APIRouter, Request
from app.core.rate_limit import limiter

router = APIRouter(tags=["Submissions"])

@router.post("/submit-tool")
@limiter.limit("5/minute")
def submit_tool(request: Request, payload: dict):
    # store raw payload (JSON or file)
    return {"message": "Tool submitted for review"}

@router.post("/submit-usecase")
@limiter.limit("5/minute")
def submit_usecase(request: Request, payload: dict):
    return {"message": "Use case submitted for review"}
