from fastapi import APIRouter, HTTPException
from app.services.content_loader import load_collection, load_by_slug

router = APIRouter(
    prefix="/tools",
    tags=["Tools"]
)

@router.get("/")
def list_tools():
    """
    List all published AI tools.

    Used for:
    - Homepage discovery
    - Tool listing pages
    """
    tools = load_collection("tools")
    return {
        "count": len(tools),
        "items": tools
    }

@router.get("/{slug}")
def get_tool(slug: str):
    tool = load_by_slug("tools", slug)
    if not tool:
        raise HTTPException(status_code=404, detail="Tool not found")
    return tool
