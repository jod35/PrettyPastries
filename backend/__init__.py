from flask import Flask

from backend.auth.routes import auth_bp
from backend.products.routes import product_bp
from backend.user.routes import user_bp

app=Flask(__name__)


#register the blueprints

app.register_blueprint(auth_bp,url_prefix='/auth')
app.register_blueprint(user_bp,url_prefix='/user')
app.register_blueprint(product_bp,url_prefic='/products')

