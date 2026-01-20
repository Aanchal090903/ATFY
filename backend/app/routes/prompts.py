from fastapi import APIRouter, HTTPException
from app.services.content_loader import load_collection, load_by_slug

router = APIRouter(prefix="/prompts", tags=["Prompts"])

@router.get("")
def get_prompts():
    return load_collection("prompts")

@router.get("/{slug}")
def get_prompt(slug: str):
    prompt = load_by_slug("prompts", slug)
    if not prompt:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return prompt
