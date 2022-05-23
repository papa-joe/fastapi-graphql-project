from orator.migrations import Migration


class CreateProductsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('products') as table:
            table.increments('id')
            table.integer('cat_id').unsigned()
            table.foreign('cat_id').references('id').on('categories')
            table.string('name')
            table.float('price')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('products')
