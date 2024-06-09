from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(min_length=8)


class User(UserBase):
    id: int

    class Config:
        from_attributes = True


class PostBase(BaseModel):
    text: str = Field(max_length=1024)


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True
