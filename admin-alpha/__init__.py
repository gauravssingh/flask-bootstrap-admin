from flask import Flask
from flask import render_template
from flask import redirect, url_for, request
from flask import session


app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/index')
def index():
    username = session['username']
    return render_template('/pages/index.html', user=username)


@app.route('/', methods=['GET', 'POST'])
def login():
    error_message = None
    if request.method == 'POST':
        if request.form['password'] != 'password':
            error_message = 'Invalid Credentials. Please try again.'
        else:
            session['username'] = request.form['username']
            return redirect(url_for('index'))
    return render_template('/pages/login.html', error=error_message)

@app.route('/flot')
def flot():
    return render_template('/pages/flot.html')


@app.route('/morris')
def morris():
    return render_template('/pages/morris.html')


@app.route('/tables')
def tables():
    return render_template('/pages/tables.html')


@app.route('/forms')
def forms():
    return render_template('/pages/forms.html')


@app.route('/forms')
def blank():
    return render_template('/pages/blank.html')


@app.route('/icons')
def icons():
    return render_template('/pages/icons.html')


@app.route('/buttons')
def buttons():
    return render_template('/pages/buttons.html')

if __name__ == "__main__":
    app.run()
