from flask import jsonify, render_template, redirect, url_for, request
from datetime import datetime as dt
from flask import current_app as app
from .models import db, Person
import requests, json

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