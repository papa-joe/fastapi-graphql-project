import graphene
import uuid

from serializers import (
    CategoryGrapheneInputModel,
    CategoryGrapheneModel,
    ProductGrapheneInputModel,
    ProductGrapheneModel,
    ProductsModel,
)

from models.product import Product
from models.category import Category


class Query(graphene.ObjectType):
    say_hello = graphene.String(name=graphene.String(default_value='Test Driven'))

    list_products = graphene.List(ProductGrapheneModel)
    total_products = graphene.Field(graphene.Int)
    total_price = graphene.Field(graphene.Int)
    get_single_product = graphene.Field(ProductGrapheneModel, product_id=graphene.NonNull(graphene.Int))

    list_categories = graphene.List(CategoryGrapheneModel)
    get_single_category = graphene.Field(CategoryGrapheneModel, category_id=graphene.NonNull(graphene.Int))

    @staticmethod
    def resolve_say_hello(parent, info, name):
        return f'Hello {name}'

    @staticmethod
    def resolve_list_categories(parent, info):
        return Category.all()

    @staticmethod
    def resolve_list_products(parent, info):
        return Product.all()

    @staticmethod
    def resolve_total_products(parent, info):
        return Product.all().count()

    @staticmethod
    def resolve_total_price(parent, info):
        tp = 0
        for i in Product.all():
            tp += i.price

        return tp

    @staticmethod
    def resolve_get_single_product(parent, info, product_id):
        return Product.find_or_fail(product_id)

    @staticmethod
    def resolve_get_single_category(parent, info, category_id):
        return Category.find_or_fail(category_id)


class CreateCategory(graphene.Mutation):
    class Arguments:
        cat_details = CategoryGrapheneInputModel()

    Output = CategoryGrapheneModel

    @staticmethod
    def mutate(parent, info, cat_details):
        cat = Category()
        cat.title = cat_details.title

        cat.save()

        return cat


class CreateProduct(graphene.Mutation):
    class Arguments:
        product_details = ProductGrapheneInputModel()

    Output = ProductGrapheneModel

    @staticmethod
    def mutate(parent, info, product_details):
        cat = Category.find_or_fail(product_details.category_id)
        product = Product()
        product.name = product_details.name
        product.price = product_details.price

        cat.products().save(product)

        return product



class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    create_product = CreateProduct.Field()