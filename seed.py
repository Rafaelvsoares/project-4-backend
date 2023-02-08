from app import app, db
from models.product import ProductModel
from models.comment import CommentModel
from models.product_data import products
from models.user import UserModel
from models.basket import BasketModel
from models.basket_item import BasketItemModel

with app.app_context():
    try:
        print('Creating database...')
        db.drop_all()
        db.create_all()

        print('Seeding the database!')
        for dictionary in products:
            product = ProductModel(**dictionary)
            product.save()

            comment = CommentModel(content=f'This is a comment of product id: {product.id}', product_id=product.id)
            comment.save()
            
        ##! Raf
        user_raf = UserModel(username="Rafael", password="Rafael123", email="raf@mail.com")
        user_raf.save()
        basket_raf = BasketModel(user_id=user_raf.id)
        basket_raf.save()
        basket_product1 = BasketItemModel(quantity=3, basket_id=basket_raf.id, product_id=6)
        basket_product1.save()
        basket_product2 = BasketItemModel(quantity=2, basket_id=basket_raf.id, product_id=1)
        basket_product2.save()
        

        ##! Fabio
        user_fab = UserModel(username="Fabio", password="Fabio123", email="fabio@mail.com")
        user_fab.save()
        basket_fab = BasketModel(user_id=user_fab.id)
        basket_fab.save()
        basket_product3 = BasketItemModel(quantity=2, basket_id=basket_fab.id, product_id=5)
        basket_product3.save()
        

        print('Database seeded!')
    except Exception as e:
        print(e)