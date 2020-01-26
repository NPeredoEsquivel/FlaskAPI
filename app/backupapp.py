from flask import Flask, jsonify, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from forms import PersonInfoForm
import requests, json
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import Person

app = Flask(__name__, template_folder='templates')
# app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
config.from_object(Config)
db = SQLAlchemy()
migrate = Migrate(app, db)


#This is to get access to the db instane
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Person': Person}

@app.route('/')
def homepage():
    params = {
    'api_key': '{API_KEY}',
    }
    r = requests.get(
        'https://www.poemist.com/api/v1/randompoems',
        params=params)
    # return r.content
    content = r.content
    return render_template('information.html', content = content)
    # return render_template('persons.html', poems=json.loads(r.text)['poems'])


@app.route('/welcome', methods=['GET', 'POST'])
def welcome_person():
    error = None
    form = PersonInfoForm()
    if request.method == 'POST':
        if form.validate():
            return redirect(url_for('homepage'))
            # return 'Validated form'
    # if request.method == 'POST':
    #     if form.validate_on_submit():
    #         return redirect(url_for('homepage'))
    #         # return 'Validated form'
        #OJO ACA PORQUE NO ESTA VALIDO EL FORMULARIO

    return render_template('person.html', error = error, form = form)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)