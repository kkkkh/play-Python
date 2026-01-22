from pydantic import BaseModel, Field
from typing import List


class LanguageAnalysis(BaseModel):
    keywords: List[str] = Field(description="Key words or phrases")
    difficult_words: List[str] = Field(description="Words difficult for English learners")
    grammar_points: List[str] = Field(description="Important grammar points")
    chinese_summary: str = Field(description="Short Chinese summary")
