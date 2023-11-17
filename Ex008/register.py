from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
import secrets
from forms import RegistrationForm
from data_base import db, Base
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex()
csrf = CSRFProtect(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
db.init_app(app)

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("OK")

@app.route('/reg/', methods=['GET', 'POST'])
def reg():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        password = generate_password_hash(form.password.data)
        user = Base(name = form.name.data, last_name = form.lastname.data, email = form.email.data, password = password)
        db.session.add(user)
        db.session.commit()
        return 'Registration - OK'
    return render_template('reg.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)