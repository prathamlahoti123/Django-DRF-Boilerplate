from main.env import env

DATABASES = {"default": env.db(default="sqlite:///db.sqlite3")}
