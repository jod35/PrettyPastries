from flask import Blueprint,render_template


product_bp=Blueprint('product_bp',__name__,
    template_folder='templates',
    static_folder='static'
)


@product_bp.route('/products')
def products():
    return render_template('products/index.html')


@product_bp.route('/products/buy')
def buy_product():
    return render_template('products/buy.html')

    