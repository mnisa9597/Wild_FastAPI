import uvicorn
from fastapi import FastAPI
from mysite.api import user, category, subcategory, product, product_image, review, auth
from mysite.admin.setup import setup_admin


store_app = FastAPI()

setup_admin(store_app)
store_app.include_router(auth.auth_router)
store_app.include_router(user.user_router)
store_app.include_router(category.category_router)
store_app.include_router(subcategory.subcategory_router)
store_app.include_router(product.product_router)
store_app.include_router(product_image.product_image_router)
store_app.include_router(review.review_router)



if __name__ == '__main__':
    uvicorn.run(store_app, host='127.0.0.1', port=8001)