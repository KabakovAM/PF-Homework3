from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
import secrets
from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex()
csrf = CSRFProtect(app)

@app.route('/reg/', methods=['GET', 'POST'])
def reg():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        return 'Registration - OK'
    return render_template('reg.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)