# FASTAPI AND GRAPHQL PROJECT

## OVERVIEW
Api that stores products by categoty, the project makes use of postgrsql db

## SETUP
Make sure you have python3 setup on your machine.
Clone the repo, start a new virtual enviroment in the root folder(recommended), change the db_name and user_name in db.py to the database name and username on your postgresql then run 

```
pip install -r packages.txt
```

The above command will install all packages needed for the project to work, after installation, start the server by running

```
uvicorn main:app --reload 
```

visit http://localhost:8000/graphql on your browser to test the programm

## COMMANDS

To create categories run the following command

```
mutation createCategory {
  createCategory(catDetails: {
    title: "Games"
  })
  {
    id,
    title
  }
}
```

To create product run

```
mutation createProduct {
  createProduct(productDetails: {
    categoryId: 3,
    name: "Pink Candy",
    price: 60
  })
  {
    name
  }
}
```

Get categories of products

```
query GetAllCategories {
  listCategories {
    id
    title
    products {
      name,
      price
    }
  }
}
```

Get single category of products


```
query getCategory {
  getSingleCategory(categoryId: 2) {
    title
    products {
      name
      price
    }
  }
}
```

Get all products

```
query GetAllProducts {
  listProducts {
    id
    name
    price
    categoryId
  }
  totalProducts
  totalPrice
}
```

Get single product

```
query getProduct {
  getSingleProduct(productId: 5) {
    name,
    price,
    categoryId
  }
}
```

