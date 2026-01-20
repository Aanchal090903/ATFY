from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class PromptStatus(str, Enum):
    draft = "draft"
    published = "published"

class Prompt(BaseModel):
    id: str
    title: str
    slug: str
    summary: str
    description: str
    pattern: str
    examples: str
    when_to_use: str
    when_not_to_use: str
    status: PromptStatus
    created_at: datetime
    updated_at: datetime
