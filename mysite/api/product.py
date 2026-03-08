from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from mysite.database.db import SessionLocal
from mysite.database.models import Product
from mysite.database.schema import ProductOutSchema, ProductInputSchema
from typing import List

product_router = APIRouter(prefix='/product', tags=['Product CRUD'])

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@product_router.post('/', response_model=ProductOutSchema)
async def create(product: ProductInputSchema, db: Session = Depends(get_db)):
    product_db = Product(**product.dict())
    db.add(product_db)
    db.commit()
    db.refresh(product_db)
    return product_db


@product_router.get('/', response_model=List[ProductOutSchema])
async def list_product(db: Session = Depends(get_db)):
    return db.query(Product).all()


@product_router.get('/{product_id}', response_model=ProductOutSchema)
async def detail_product(product_id: int, db: Session = Depends(get_db)):
    product_db = db.query(Product).filter(Product.id==product_id).first()
    if not product_db:
        raise HTTPException(detail='Мындай маалымат жок', status_code=400)
    return product_db


@product_router.put('/{product_id}', response_model=dict)
async def update_product(product_id: int, product: ProductInputSchema,
                         db: Session= Depends(get_db)):
    product_db = db.query(Product).filter(Product.id==product_id).first()
    if not product_db:
        raise HTTPException(detail='Мындай маалымат жок', status_code=400)

    for k, v in product.dict().items():
        setattr(product_db, k, v)

    db.add(product_db)
    db.commit()
    db.refresh(product_db)
    return {'message': 'Категория озгорду'}


@product_router.delete('/{product_id}', response_model=dict)
async def delete_product(product_id: int, db: Session= Depends(get_db)):
    product_db = db.query(Product).filter(Product.id==product_id).first()
    if not product_db:
        raise HTTPException(detail='Мындай маалымат жок', status_code=400)
    db.delete(product_db)
    db.commit()
    return {'message': 'Маалымат жок болду'}