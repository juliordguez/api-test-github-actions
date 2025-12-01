from pydantic import BaseModel
from typing import Dict, Optional


# ---- Modelos ----
class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None


class Item(ItemBase):
    id: int

