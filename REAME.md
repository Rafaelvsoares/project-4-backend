## Documentation
- [Flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/)

- [sqlalchemy](https://www.sqlalchemy.org/)


### File structure similar to Express
![ File Structure ](./assets/file_structure.png)

## Commands

- To seed database `pipenv run python seed.py`
- To run project `pipenv run flask run`


## BACKEND STRUCTURE

1. `pipenv install flask-sqlalchemy` <-- to create db/ models/ schemas  
2. `pipenv install psycopg2-binary` <-- extesions that tells sqlalchemy we are using postgresql
3. From the terminal do --> `createdb -U postgres <dbname>` <-- SQLALCHEMY does not automatically create a database for us like Mongodb.
4. Create `config/environment.py` in the root of project. 
5. In `environment.py` create a variable `db_URI = 'postgresql://{user}:{password}@localhost:{port number}/{db}'`
6. In `app.py` add:

![ app.py Structure ](./assets/app_py_structure.png)

## Model/Schema

1. Create `models/base.py`, `models/store.py` and any other relevant models/schemas.
In `base.py` is where all the columns you want to be filled in automatically by some logic will be at e.g id, created time, updated time, etc.

![ base.py model structure ](./assets/base_py_model.png)

2. In `models/store.py` is where you will create you schema/validation and necessary columns for the database. Note that the `models` in `flask_sqlalchemy` is the `schema` for `mongoose`.

![ store.py model structure ](./assets/store_py_model.png)

## Seeding

1. Create a `seed.py` file in the root of the project. This is the file that will be responsible for actually setting up the database with the correct tables/data. Once this file has been created, you can run it with `pipenv run python seed.py` to seed the DB.

![ seed.py structure ](./assets/seed_py_structure.png)

2. You can check if this worked by checking on TablePlus or pgAdmin it should create a table in your database with the data you provided for the seeding.

It can be quite overwhelming doing a whole backend and not knowing where to start. Here is the perfect example of how to test your models by seeding data to your database. Like this is easier to know where the errors are coming from as we are only working with 3 files and there is no need for `controllers` for now. 


## Serializer/ Deserializer

We will be using a library to convert json data into a format that sqlalchemy (model) can use to talk to postgresql database this is called SERIALIZATION. If we want to convert a model back to json we DESERIALIZE.
The library used for this is called Marshmallow.

DOCS for Marshmallow for Flask and Marshmallow on its own

- [flask marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
- [marshmallow](https://marshmallow.readthedocs.io/en/stable/)

---

1. Run `pipenv install flask_marshmallow marshmallow-sqlalchemy` to install.

2. In your app.py file. Import Marshmallow for flask and instantiate it as shown bellow:

![ how to import and instantiate marshmallow for flask ](./assets/marshmallow_app_file.png)

3. In your root folder create a folder called `serializers` and add `<file>.py`.

4. In here its were we will solve the problem of converting data formats (serialize and deserialize) into the right formats we need for our API requests to work. Note that the below code uses a `class` called `TeaSchema`. This is very different to what a mongoose schema does. So, don't get confused with the naming convention as we had to do this way because in the documentation for this library it used the word `schema` as its convention, so we could change to something else like `TeaSerialiser` ut this isn't reccomended for obvious reasons.


![ serializer file ](./assets/serializer_file.png)

## Views and Controllers with database

1. Inside your `views` folder will be your files with functions to do HTTP methods to your API. Also, here is also were we receive data to serialize/deserialize.

![ Views/Controllers ](./assets/views_with_real_db.png)

2. Whenever we need to save new data into postgresql we need to save the data. To do this do the following function in your `BaseModel` file:

![ Save data to db  ](./assets/basemodel_save.png)

3. Make sure this is nested inside the BaseModel class.

4. Also, here's also how to delete an item from the database.

![ Delete data to db  ](./assets/delete_from_db.png)

## Comments

1. Create a comment model.

![ Comment model ](./assets/comment_model.png)

2. Here it depends what you want to do with the comments. In this case the comment belongs to a certain tea/product ID so we are referencing the id from the tea table, make sure if you changed the name of the table to put the exact name otherwise it won't work.

3. Change tea/product model so they associated.

![ Product model v2 ](./assets/product_model_w_comment.png)

## Seeding with comments

1. To check if your models work we have to redo the seeding. The tea needs to be created before the comment as it relies on the tea ID to exist.

![ Seeding v2 ](./assets/seeding_w_comments.png)

2. If it did work you will be able to see a new table called `comments` in TablePlus with an ID which you can click and takes you to its related ID from the teas table.

## Serializers/ Deserializers

1. Create a comment schema. It's the same for the tea/products schema.

![ comment schema ](./assets/schema_comment.png)

2. Here we have to change the tea/product schema so it is aware that the comments with a related ID should be nested inside the product.

![ product schema ](./assets/schema_products_v2.png)

3. Run the project and test on insomnia. When you get the product the comments should return too. Also, when you post a new prodcust it should return the product + comment.


