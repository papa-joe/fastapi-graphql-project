from orator.orm import has_many

from db import Model


class Category(Model):

    @has_many
    def products(self):
        from .product import Product

        return Product
