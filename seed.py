from app import app, db
from data.products_data import products_list
from data.categories_data import categories_list
from data.users_data import users_list
from data.comments_data import comments_list
from data.images_data import images_list
from data.baskets_data import baskets_list
from data.basket_item_data import basket_item_list

with app.app_context():
    try:
        print('Creating database...')
        db.drop_all()
        db.create_all()

        print('Seeding the database!')

        db.session.add_all(categories_list)
        db.session.commit()

        db.session.add_all(users_list)
        db.session.commit()

        db.session.add_all(baskets_list)
        db.session.commit()

        db.session.add_all(products_list)
        db.session.commit()

        db.session.add_all(basket_item_list)
        db.session.commit

        db.session.add_all(comments_list)
        db.session.commit()

        db.session.add_all(images_list)
        db.session.commit()


        print('Database seeded!')
    except Exception as e:
        print(e)