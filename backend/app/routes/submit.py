from fastapi import APIRouter
from datetime import datetime
from slugify import slugify
import uuid
from app.services.md_writer import write_draft

router = APIRouter(prefix="/submit", tags=["Submit"])

@router.post("/")
def submit_usecase(payload: dict):
    """
    Submit a use case.
    Content is published immediately with low confidence
    and marked as community-generated.
    """

    slug = slugify(payload["title"])

    metadata = {
        "id": str(uuid.uuid4()),
        "title": payload["title"],
        "slug": slug,
        "tool_name": payload["tool_name"],
        "summary": payload["summary"],

        # 🔓 Open publishing model
        "status": "published",
        "confidence": "low",
        "source": "community",

        "created_at": datetime.utcnow().isoformat(),
        "updated_at": datetime.utcnow().isoformat(),
    }

    write_draft(
        collection="usecases",
        slug=slug,
        metadata=metadata,
        content=payload["content"]
    )

    return {
        "status": "published",
        "slug": slug,
        "confidence": "low"
    }
