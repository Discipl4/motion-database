from pydantic import BaseModel
from config.date import now

class User(BaseModel):
    left: int
    center: int
    right: int
    date= now