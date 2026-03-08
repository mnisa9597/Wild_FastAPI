from .db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Enum, DateTime, Date, ForeignKey, Text, SmallInteger
from typing import Optional, List
from enum import Enum as PyEnum
from datetime import  date, datetime


class StatusChoices(str, PyEnum):
    gold = 'gold'
    silver = 'silver'
    bronze = 'bronze'
    simple = 'simple'



class UserProfile(Base):
    __tablename__ = 'profile'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String, unique=True)
    first_name: Mapped[str] = mapped_column(String(32), nullable=True)
    last_name: Mapped[str] = mapped_column(String(32), nullable=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String)
    age: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    phone_number: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    avatar: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    status: Mapped[StatusChoices] = mapped_column(Enum(StatusChoices), nullable=False, default=StatusChoices.simple)
    created_date: Mapped[date] = mapped_column(Date, default=date.today)

    review_user: Mapped[List['Review']] = relationship(back_populates='user',
                                                       cascade='all, delete-orphan')
    refresh_token: Mapped[List['RefreshToken']] = relationship(back_populates='user',
                                                               cascade='all, delete-orphan')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class RefreshToken(Base):
    __tablename__ = 'refresh_token'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('profile.id'))
    user: Mapped[UserProfile] = relationship(back_populates='refresh_token')
    token: Mapped[str] = mapped_column(String)
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class Category(Base):
    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    category_name: Mapped[str] = mapped_column(String(32), unique=True)
    category_image: Mapped[str] = mapped_column(String)

    category_sub: Mapped[List['SubCategory']] = relationship(back_populates='category',
                                                             cascade='all, delete-orphan')

    def __str__(self):
        return self.category_name



class SubCategory(Base):
    __tablename__ = 'subcategory'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    subcategory_name: Mapped[str] = mapped_column(String(32), unique=True)
    category_id: Mapped[int] = mapped_column(ForeignKey('category.id'))
    category: Mapped[Category] = relationship(back_populates='category_sub')

    product_sub: Mapped[List['Product']] = relationship(back_populates='subcategory',
                                                        cascade='all, delete-orphan')

    def __str__(self):
        return self.subcategory_name



class Product(Base):
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    product_name: Mapped[str] = mapped_column(String(32), unique=True)
    price: Mapped[int] = mapped_column(Integer)
    article: Mapped[int] = mapped_column(Integer, unique=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    subcategory_id: Mapped[int] = mapped_column(ForeignKey('subcategory.id'))
    subcategory: Mapped[SubCategory] = relationship(back_populates='product_sub')
    product_video: Mapped[Optional[str]] = mapped_column(String)
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    product_image: Mapped[List['ProductImage']] = relationship(back_populates='product')
    review_product: Mapped[List['Review']] = relationship(back_populates='product')

    def __str__(self):
        return f'{self.product_name} {self.product_image}'




class ProductImage(Base):
    __tablename__ = 'product_image'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'))
    product: Mapped[Product] = relationship(back_populates='product_image')
    image: Mapped[str] = mapped_column(String)

    def __str__(self):
        return self.image



class Review(Base):
    __tablename__ = 'review'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('profile.id'))
    user: Mapped[UserProfile] = relationship(back_populates='review_user')
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'))
    product: Mapped[Product] = relationship(back_populates='review_product')
    rating: Mapped[int] = mapped_column(SmallInteger)
    text: Mapped[str] = mapped_column(Text)
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    def __str__(self):
        return self.rating















