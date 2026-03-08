from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from mysite.database.db import SessionLocal
from mysite.database.models import Category
from mysite.database.schema import CategoryOutSchema, CategoryInputSchema
from typing import List

category_router = APIRouter(prefix='/category', tags=['Category CRUD'])

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@category_router.post('/', response_model=CategoryOutSchema)
async def create(category: CategoryInputSchema, db: Session= Depends(get_db)):
    category_db = Category(**category.dict())
    db.add(category_db)
    db.commit()
    db.refresh(category_db)
    return category_db


@category_router.get('/', response_model=List[CategoryOutSchema])
async def list_category(db: Session= Depends(get_db)):
    return db.query(Category).all()


@category_router.get('/{category_id}', response_model=CategoryOutSchema)
async def detail_category(category_id: int, db: Session= Depends(get_db)):
    category_db = db.query(Category).filter(Category.id==category_id).first()
    if not category_db:
        raise HTTPException(detail='Мындай маалымат жок', status_code=400)
    return category_db


@category_router.put('/{category_id}', response_model=dict)
async def update_category(category_id: int, category: CategoryInputSchema,
                          db: Session= Depends(get_db)):
    category_db = db.query(Category).filter(Category.id==category_id).first()
    if not category_db:
        raise HTTPException(detail='Мындай маалымат жок', status_code=400)


    for category_key, category_value in category.dict().items():
        setattr(category_db, category_key, category_value)

    db.add(category_db)
    db.commit()
    db.refresh(category_db)
    return {'message': 'Категория озгорду'}


@category_router.delete('/{category_id}', response_model=dict)
async def delete_category(category_id: int, db: Session= Depends(get_db)):
    category_db = db.query(Category).filter(Category.id==category_id).first()
    if not category_db:
        raise HTTPException(detail='Мындай маалымат жок', status_code=400)
    db.delete(category_db)
    db.commit()
    return {'message': 'Маалымат жок болду'}






