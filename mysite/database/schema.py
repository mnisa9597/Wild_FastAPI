from typing import Optional
from datetime import date
from pydantic import BaseModel, EmailStr
from .models import StatusChoices


class UserLoginSchema(BaseModel):
    login: str
    password: str

class UserProfileListSchema(BaseModel):
    id: int
    username: str
    avatar: Optional[str]
    status: StatusChoices

class UserProfileOutSchema(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    age: Optional[int]
    phone_number: Optional[str]
    avatar: Optional[str]
    status: StatusChoices
    created_date: date


class UserProfileInputSchema(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    age: Optional[int]
    phone_number: Optional[str]
    avatar: Optional[str]
    status: StatusChoices


class CategoryOutSchema(BaseModel):
    id: int
    category_image: str
    category_name: str


class CategoryInputSchema(BaseModel):
    category_image: str
    category_name: str


class SubCategoryOutSchema(BaseModel):
    id: int
    subcategory_name: str
    category_id: int


class SubCategoryInputSchema(BaseModel):
    subcategory_name: str


class ProductOutSchema(BaseModel):
    id: int
    product_name: str
    price: int
    article: int
    description: str
    subcategory_id: int
    product_video: str
    created_date: date


class ProductInputSchema(BaseModel):
    product_name: str
    price: int
    article: int
    description: str
    product_video: str


class ProductImageOutSchema(BaseModel):
    id: int
    product_id: int
    image: str


class ProductImageInputSchema(BaseModel):
    image: str


class ReviewOutSchema(BaseModel):
    id: int
    user_id: int
    product_id: int
    rating: int
    text: str
    created_date: date


class ReviewInputSchema(BaseModel):
    rating: int
    text: str
