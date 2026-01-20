from pydantic import BaseModel, HttpUrl
from datetime import datetime
from enum import Enum

class ToolStatus(str, Enum):
    draft = "draft"
    published = "published"

class Tool(BaseModel):
    id: str
    name: str
    slug: str
    summary: str
    description: str
    website_url: HttpUrl
    category: str
    pricing: str
    status: ToolStatus
    created_at: datetime
    updated_at: datetime
