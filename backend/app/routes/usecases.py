from fastapi import APIRouter, HTTPException
from app.services.content_loader import load_collection, load_by_slug

router = APIRouter(
    prefix="/usecases",
    tags=["UseCases"]
)

@router.get("/")
def list_usecases():
    usecases = load_collection("usecases")
    return {
        "count": len(usecases),
        "items": usecases
    }

@router.get("/{slug}")
def get_usecase(slug: str):
    usecase = load_by_slug("usecases", slug)
    if not usecase:
        raise HTTPException(status_code=404, detail="Use case not found")
    return usecase

@router.get("/by-tool/{tool_name}")
def usecases_by_tool(tool_name: str):
    """
       Relationship endpoint.

       Returns all workflows that use a given tool.
       """
    usecases = load_collection("usecases")
    return [
        u for u in usecases
        if u.get("tool_name") == tool_name
    ]
