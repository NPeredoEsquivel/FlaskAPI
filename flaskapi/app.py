from flask import Flask, jsonify, render_template, redirect, url_for, request, requests, json
from flask_wtf import FlaskForm
from forms import UserInfoForm

app = Flask(__name__, template_folder='templates')

@app.route('/')
def homepage():
    params = {
    'api_key': '{API_KEY}',
    }
    r = requests.get(
        'https://www.poemist.com/api/v1/randompoems',
        params=params)
    # return r.content
    return render_template('hola.html')
    # return render_template('persons.html', poems=json.loads(r.text)['poems'])
@app.route('/welcome', methods=['GET', 'POST'])
def welcome_person():
    error = None
    form = UserInfoForm()
    if request.method == 'POST':
        if request.form['fullname'] == '':
            error = 'You need to enter a name'
        else:
            return redirect(url_for('homepage'))
    return render_template('hola.html', error = error, form = form)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)