from sqladmin import ModelView
from mysite.database.models import UserProfile, Category, SubCategory, Product, ProductImage, Review



class UserProfileAdmin(ModelView, model=UserProfile):
    column_list = [UserProfile.first_name, UserProfile.last_name]


class CategoryAdmin(ModelView, model=Category):
    column_list = [Category.category_name]


class SubCategoryAdmin(ModelView, model=SubCategory):
    column_list = [SubCategory.subcategory_name]


class ProductAdmin(ModelView, model=Product):
    column_list = [Product.product_name, Product.product_image]


class ProductImageAdmin(ModelView, model=ProductImage):
    column_list = [ProductImage.image]


class ReviewAdmin(ModelView, model=Review):
    column_list = [Review.rating]