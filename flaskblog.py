from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm, RegistrationForm

app = Flask(__name__)
# Random string to help encrypt logins
app.config['SECRET_KEY'] = '354407a449af675d04fe830449b9ee9b'
posts = [
    {
        'author': 'Sean Connors',
        'title': 'Blog Post 1',
        'date_posted': 'August 23rd',
        'content': 'A star is born.'
    },
    {
        'author': 'Jack Skellington',
        'title': 'Blog Post 2',
        'date_posted': 'October 31st',
        'content': "Wouldn't you like to see something strange?"
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')

# Enable this route to accept GET and POST requests, important for


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful. Please check username and/or password.', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
