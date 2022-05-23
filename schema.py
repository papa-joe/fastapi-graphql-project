import graphene

from serializers import (
    CategoryGrapheneInputModel,
    CategoryGrapheneModel,
    ProductGrapheneInputModel,
    ProductGrapheneModel,
)

from models.product import Product
from models.category import Category


class Query(graphene.ObjectType):
    say_hello = graphene.String(name=graphene.String(default_value='Test Driven'))
    list_categories = graphene.List(CategoryGrapheneModel)
    list_products = graphene.List(ProductGrapheneModel)
    get_single_product = graphene.Field(ProductGrapheneModel, product_id=graphene.NonNull(graphene.Int))
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
        cat = Category.find_or_fail(product_details.cat_id)
        product = Product()
        product.name = product_details.name
        product.price = product_details.price

        cat.products().save(product)

        return product



class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    create_product = CreateProduct.Field()