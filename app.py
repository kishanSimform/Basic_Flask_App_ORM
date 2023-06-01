from flask import Flask
from apps.author.models import *
from apps.book.models import *
from apps.user.models import *
from db import setup_with_app
from apps.user.urls import user_routes
from apps.author.urls import author_routes
from apps.book.urls import book_routes, category_routes


main_app = Flask(__name__, instance_relative_config=True, template_folder='templates')
main_app.config.from_pyfile(".env")
main_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
main_app.config['JSON_AS_ASCII'] = False
main_app.register_blueprint(user_routes)
main_app.register_blueprint(author_routes)
main_app.register_blueprint(book_routes)
main_app.register_blueprint(category_routes)
setup_with_app(main_app)


@main_app.route('/')
def hello():
    return "hello"

if __name__ == "__main__":
    main_app.url_map
    main_app.run()