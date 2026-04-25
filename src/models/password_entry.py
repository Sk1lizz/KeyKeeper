# src\models\password_entry.py

"""  """

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class EntryPassword:
    title: str
    username: str
    password: str
    url: str = ""
    notes: str = ""
    category: str = ""
    favorite: int = 0
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def to_dict(self) -> dict:
        """"""

        return {
            "title": self.title,
            "username": self.username,
            "password": self.password,
            "url": self.url,
            "notes": self.notes,
            "category": self.category,
            "favorite": self.favorite
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "EntryPassword":
        """"""

        return cls(
            id=data.get("id"),
            title=data["title"],
            username=data["username"],
            password=data["password"],
            url=data.get("url", ""),
            notes=data.get("notes", ""),
            category=data.get("category", "Другое"),
            favorite=data.get("favorite", 0),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at")
        )