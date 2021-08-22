from flask import Flask, render_template, session, redirect, url_for

from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

# To deploy
# https://realpython.com/flask-by-example-part-1-project-setup/ 
class NameForm(FlaskForm):
    user_name = StringField('Ingresa tu nombre de usuario', validators=[DataRequired()])
    user_pass = PasswordField('Ingresa tu contraseña', validators=[DataRequired()])
    submit = SubmitField('INGRESAR')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', 
                           current_time=datetime.utcnow(), 
                           form=form, 
                           name=session.get("name"))
    

@app.route('/user/<name>') #dynamic part
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500