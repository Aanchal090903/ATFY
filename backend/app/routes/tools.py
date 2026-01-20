from fastapi import APIRouter, HTTPException
from app.services.content_loader import load_collection, load_by_slug

router = APIRouter(prefix="/tools", tags=["Tools"])

@router.get("")
def get_tools():
    return load_collection("tools")

@router.get("/{slug}")
def get_tool(slug: str):
    tool = load_by_slug("tools", slug)
    if not tool:
        raise HTTPException(status_code=404, detail="Tool not found")
    return tool
