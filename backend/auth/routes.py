from flask import Blueprint,render_template

auth_bp=Blueprint('auth_bp',__name__,
     template_folder='templates',
     static_folder='static'
)

@auth_bp.route('/auth')
def auth():
    render_template('/login.html')

@auth_bp.route('/auth/forgot')
def recover_password():
    return render_template('auth/recover.html')

    

