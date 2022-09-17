from pydantic import BaseModel, Field
from typing import Optional
import uuid

class Book(BaseModel):
    id: str = Field(default_factory=uuid.uuid4(), alias="_id")
    title: str = Field(...)
    author: str = Field(...)
    synopsis: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "123-4567-890",
                "title": "percy_jackson",
                "author": "Ryan Reynolds",
                "synopsis": "..."
            }
        }


class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    synopsis: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "Percy_2",
                "author": "abcdef",
                "synopsis": "Percy_2 is a novel by abcdef"
            }
        }




