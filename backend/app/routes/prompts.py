from fastapi import APIRouter, HTTPException
from app.services.content_loader import load_collection, load_by_slug

router = APIRouter(
    prefix="/prompts",
    tags=["Prompts"]
)

@router.get("/")
def list_prompts():
    """
    List all published prompt patterns.
    """
    prompts = load_collection("prompts")
    return {
        "count": len(prompts),
        "items": prompts
    }


@router.get("/{slug}")
def get_prompt(slug: str):
    """
    Get a single prompt by slug.
    """
    prompt = load_by_slug("prompts", slug)
    if not prompt:
        raise HTTPException(404, "Prompt not found")
    return prompt

@router.get("/by-usecase/{usecase_slug}")
def prompts_by_usecase(usecase_slug: str):
    """
    Get prompts used in a specific use case.
    """
    usecases = load_collection("usecases")
    usecase = next(
        (u for u in usecases if u["slug"] == usecase_slug),
        None
    )

    if not usecase:
        raise HTTPException(404, "Use case not found")

    prompt_slugs = usecase.get("prompts", [])

    prompts = load_collection("prompts")
    return [
        p for p in prompts
        if p["slug"] in prompt_slugs
    ]

