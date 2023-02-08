# projecty-4-backend

1. Clone repo
2. Add `.env` file in the root folder of this repo adn paste the code below

```
FLASK_DEBUG=True
FLASK_ENV=development
FLASK_SKIP_DOTENV=1
FLASK_RUN_PORT=4000
```

3. Run `pipenv install`
4. `CTRL + SHIT + P` on windows and select the right interpreter.
5. `pipenv run python seed.py` if you want to seed data.
6. `pipenv run flask run` to make http requests.