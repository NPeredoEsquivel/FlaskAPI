from flask import jsonify, render_template, redirect, url_for, request
from datetime import datetime as dt
from flask import current_app as app
from .forms import PersonInfoForm
import requests, json
from datetime import datetime
from .models import db, Person
from dateutil.relativedelta import relativedelta
import random


#Return the days remaining to bithday
def calculate_dates(birthday, now):
    delta1 = datetime(now.year, birthday.month, birthday.day).date()
    delta2 = datetime(now.year+1, birthday.month, birthday.day).date()
    days = (max(delta1, delta2) - now).days
    if days >= 365:
        days = 0
    return days

def jsonManipulation(content):
    data = json.loads(content)
    length = len(data[0])
    randomPoem = data[random.randint(0,length)]['content']
    return randomPoem

#Home route
@app.route('/', methods=['GET', 'POST'])
def homepage():
    error = None
    #Obtain the poems Json from page
    params = {
    'api_key': '{API_KEY}',
    }
    r = requests.get(
        'https://www.poemist.com/api/v1/randompoems',
        params=params)

    content = r.content

    randomPoem = jsonManipulation(content)

    # length = len(content[0]['title'])
    form = PersonInfoForm()
    personCount = Person.query.count()
    if request.method == 'POST':
        if form.validate_on_submit():
            #Obtain values from form
            fullname = request.form.get('fullname')
            date = request.form.get('date')

            datetime_object = datetime.strptime(date, '%Y-%m-%d').date()
            today = datetime.now().date()

            difference_in_years = relativedelta(today, datetime_object).years
            days = calculate_dates(datetime_object,today)

            fullNameSplit = fullname.split()
            if days == 0:
                birthday = True
                poem=randomPoem
            else:
                birthday = False
                poem = ""
            # Create an instance of the User class
            new_user = Person(firstname=fullNameSplit[0],
                        lastname = fullNameSplit[1],
                        date=datetime_object,
                        age = difference_in_years,
                        daystobirthday = days,
                        birthday=birthday,
                        poem=poem)
            db.session.add(new_user)  # Adds new User record to database
            db.session.commit()
            persons = Person.query.all()
            return render_template('person.html', persons = persons, form= form, content = days)

    if personCount > 0:
        db.session.query(Person).delete()
        db.session.commit()
    return render_template('person.html', error = error, form = form)


    # return render_template('persons.html', poems=json.loads(r.text)['poems'])