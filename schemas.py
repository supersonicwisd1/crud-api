import datetime as _dt
import pydantic as _pydantic
# from typing import List

class _UserBase(_pydantic.BaseModel):
    name: str
    email: str
    track: str
    gender: str
    github_profile: str

class UserCreate(_UserBase):
    password: str 

class User(_UserBase):
    id: int 
    is_active: bool
    date_created: _dt.datetime
    date_last_updated: _dt.datetime

    class Config:
        from_attributes = True