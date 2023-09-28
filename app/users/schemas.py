from fastapi_users.schemas import BaseUserCreate, BaseUser


class UserRead(BaseUser[int]):
    name: str


class UserCreate(BaseUserCreate):
    name: str
