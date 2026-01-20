from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class UseCaseStatus(str, Enum):
    draft = "draft"
    pending = "pending"
    published = "published"

class UseCase(BaseModel):
    id: str
    title: str
    slug: str
    tool_name: str
    summary: str
    problem: str
    workflow: str
    prompting_strategy: str
    outcome: str
    author: str
    is_community: bool
    status: UseCaseStatus
    created_at: datetime
    updated_at: datetime
