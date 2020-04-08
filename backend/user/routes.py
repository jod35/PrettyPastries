from flask import Blueprint,render_template

user_bp=Blueprint('user_bp',__name__,
    template_folder='templates',
    static_folder='static')


@user_bp.route('/signup')
def create_account():
    return render_template('user/signup.html')

@user_bp.route('/forgot')
def reset_password():
    return render_template('user/reset.html')