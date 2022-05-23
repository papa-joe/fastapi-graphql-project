
from typing import List, Optional

from graphene_pydantic import PydanticInputObjectType, PydanticObjectType
from pydantic import BaseModel


class ProductsModel(BaseModel):
    id: int
    category_id: int
    name: str
    price: float


class CategoryModel(BaseModel):
    id: int
    title: str
    products: Optional[List[ProductsModel]]


class ProductGrapheneModel(PydanticObjectType):
    class Meta:
        model = ProductsModel


class CategoryGrapheneModel(PydanticObjectType):
    class Meta:
        model = CategoryModel


class ProductGrapheneInputModel(PydanticInputObjectType):
    class Meta:
        model = ProductsModel
        exclude_fields = ('id', )


class CategoryGrapheneInputModel(PydanticInputObjectType):
    class Meta:
        model = CategoryModel
        exclude_fields = ('id', 'products')