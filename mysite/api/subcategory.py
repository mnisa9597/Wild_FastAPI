from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from mysite.database.db import SessionLocal
from mysite.database.models import SubCategory
from mysite.database.schema import SubCategoryOutSchema, SubCategoryInputSchema
from typing import List

subcategory_router = APIRouter(prefix='/subcategory', tags=['SubCategory CRUD'])

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@subcategory_router.post('/', response_model=SubCategoryOutSchema)
async def create(subcategory: SubCategoryInputSchema, db: Session = Depends(get_db)):
    subcategory_db = SubCategory(**subcategory.dict())
    db.add(subcategory_db)
    db.commit()
    db.refresh(subcategory_db)
    return subcategory_db


@subcategory_router.get('/', response_model=List[SubCategoryOutSchema])
async def list_subcategory(db: Session = Depends(get_db)):
    return db.query(SubCategory).all()


@subcategory_router.get('/{subcategory_id}', response_model=SubCategoryOutSchema)
async def detail_subcategory(subcategory_id: int, db: Session = Depends(get_db)):
    subcategory_db = db.query(SubCategory).filter(SubCategory.id==subcategory_id).first()
    if not subcategory_db:
        raise HTTPException(detail='Мындай маалымат жок', status_code=400)
    return subcategory_db


@subcategory_router.put('/{subcategory_id}', response_model=dict)
async def update_subcategory(subcategory_id: int, subcategory: SubCategoryInputSchema,
                             db: Session= Depends(get_db)):
    subcategory_db = db.query(SubCategory).filter(SubCategory.id==subcategory_id).first()
    if not subcategory_db:
        raise HTTPException(detail='Мындай маалымат жок', status_code=400)

    for k, v in subcategory.dict().items():
        setattr(subcategory_db, k, v)

    db.add(subcategory_db)
    db.commit()
    db.refresh(subcategory_db)
    return {'message': 'Категория озгорду'}


@subcategory_router.delete('/{subcategory_id}', response_model=dict)
async def delete_subcategory(subcategory_id: int, db: Session= Depends(get_db)):
    subcategory_db = db.query(SubCategory).filter(SubCategory.id==subcategory_id).first()
    if not subcategory_db:
        raise HTTPException(detail='Мындай маалымат жок', status_code=400)
    db.delete(subcategory_db)
    db.commit()
    return {'message': 'Маалымат жок болду'}

