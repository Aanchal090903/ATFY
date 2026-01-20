from fastapi import APIRouter, HTTPException
from app.services.content_loader import load_collection, load_by_slug

router = APIRouter(prefix="/usecases", tags=["UseCases"])

@router.get("")
def get_usecases():
    return load_collection("usecases")

@router.get("/{slug}")
def get_usecase(slug: str):
    usecase = load_by_slug("usecases", slug)
    if not usecase:
        raise HTTPException(status_code=404, detail="Use case not found")
    return usecase
