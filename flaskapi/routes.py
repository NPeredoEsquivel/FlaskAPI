from flask import jsonify, render_template, redirect, url_for, request
from datetime import datetime as dt
from flask import current_app as app
from .forms import PersonInfoForm
import requests, json
from datetime import datetime
from .models import db, Person

def days_between(d1, d2):

    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    params = {
    'api_key': '{API_KEY}',
    }
    r = requests.get(
        'https://www.poemist.com/api/v1/randompoems',
        params=params)
    # return r.content
    content = r.content

    error = None
    form = PersonInfoForm()
    personCount = Person.query.count()
    if request.method == 'POST':
        if form.validate_on_submit():
            fullname = request.form.get('fullname')
            date = request.form.get('date')
            today = datetime.now().date()
            # daysDiff = days_between(today, date)

            new_user = Person(username=fullname,
                        date=date,
                        birthday=False,
                        poem="In West Philadelphia born and raised, on the playground is where I spent most of my days")  # Create an instance of the User class
            db.session.add(new_user)  # Adds new User record to database
            db.session.commit()
            persons = Person.query.all()
            if fullname:
                return render_template('person.html', persons = persons, form= form, date = daysDiff)
            else:
                return render_template('person.html', fullname = "error", date = "error", form = form)
    if personCount > 0:
        db.session.query(Person).delete()
        db.session.commit()
    return render_template('person.html', error = error, form = form)


    # return render_template('persons.html', poems=json.loads(r.text)['poems'])