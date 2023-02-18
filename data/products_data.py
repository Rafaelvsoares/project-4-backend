from models.products import ProductModel

products_list = [
    ProductModel(title="Cube", price=0, polygons=6, description="It's a free cube with 6 polygons", user_id=2, category_id= 4),
    ProductModel(title= "Triangle", price= 0, polygons= 4, description= "It's a free triangle with 4 polygons", user_id=1, category_id= 4),
    ProductModel(title= "Car", price= 10, polygons= 2300, description= "Low poly car model", user_id=1, category_id= 2),
    ProductModel(title= "Plane", price= 250.50, polygons= 5000, description= "Game ready low poly plane model", user_id=1, category_id= 2),
    ProductModel(title= "Cog", price= 0, polygons= 140, description= "Free cog model", user_id=3, category_id= 4),
    ProductModel(title= "House", price= 81, polygons= 8000, description= "Game ready house model", user_id=1, category_id= 6),
    ProductModel(title= "Cat", price= 20, polygons= 12000, description= "Cat model", user_id=3, category_id= 1),
    ProductModel(title= "Syringe", price= 5, polygons= 50, description= "Octane syringe. Cheap model for £5", user_id=4, category_id= 4),
    ProductModel(title= "Kunai", price= 5, polygons= 60, description= "Wraith kunai from Apex Legends", user_id=4, category_id= 4),
    ProductModel(title= "Gloves", price= 8, polygons= 200, description= "Pathfinder boxing gloves", user_id=4, category_id= 4)
]
