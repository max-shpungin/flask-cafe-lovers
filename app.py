import os
from dotenv import load_dotenv

from flask import Flask, g, render_template, redirect, abort, url_for, flash
from sqlalchemy.exc import IntegrityError
from flask_login import (
    LoginManager,
    login_user,
    login_required,
    logout_user,
    current_user)

from models import connect_db, db, User, Cafe
from forms import SignupForm, LoginForm, CafeForm, CSRFProtection

from flask_debugtoolbar import DebugToolbarExtension  # TODO:

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config["SQLALCHEMY_ECHO"] = True

gmaps_api_url = os.environ['GMAPS_API_URL']

connect_db(app)

debug = DebugToolbarExtension(app)  # TODO:
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False  # TODO:

login_manager = LoginManager()
login_manager.init_app(app)
# redirect view if not logged in and attempt to access @login_required
login_manager.login_view = 'login'

################################################################################
# session handling
@app.before_request
def add_csrf_form():
    """ add csrf form to global g for use in templates """
    g.csrf_form = CSRFProtection()

@app.before_request
def load_api_keys():
    """ load api keys needed for front end js """
    g.gmaps_api_url = gmaps_api_url

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


################################################################################
# Anon / Signup / Login / Dashboard


@app.route('/')
def home():
    """ Show all users and cafes"""
    users = User.query.all();
    cafes = Cafe.query.all();
    return render_template('home.html', users=users, cafes=cafes)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """ redirects to dashboard on signup """

    form = SignupForm()

    if form.validate_on_submit():

        new_user = User.signup(form.username.data, form.password.data)

        try:  # in case of duplicate name, show error message to user
            db.session.add(new_user)
            db.session.commit()

        except IntegrityError:
            flash("wow there bucko, name's taken", "warning")
            return render_template('signup.html', form=form)

        else:
            dashboard_url = '/users/' + new_user.username
            login_user(new_user)
            flash('great success, welcome to the party!', "success")
            return redirect(dashboard_url)

    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
        redirects to dashboard on login
    """

    form = LoginForm()

    if form.validate_on_submit():
        user = User.login(username=form.username.data,
                          password=form.password.data)

        if user:
            login_user(user)
            dashboard_url = '/users/' + user.username

            flash('logged in!', 'success')
            return redirect(dashboard_url)
        else:
            flash('bad username/password', 'danger')

    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/users/<username>')
@login_required
def dashboard(username):
    user = User.query.filter_by(username=username).one_or_404()

    return render_template('dashboard.html', user=user)

################################################################################
# CAFES Add/remove cafes and view user and cafe listings


@app.route('/cafes')
def cafes():
    """ Cafe Listings """
    cafes = Cafe.query.all()
    return render_template('/cafes/cafeslistings.html', cafes=cafes)


@app.route('/cafes/add', methods=['GET', 'POST'])
@login_required
def cafes_add():
    """ Cafe Listings """
    form = CafeForm()

    if form.validate_on_submit():
        new_cafe = Cafe.create(name=form.name.data,
                               address_street=form.address_street.data,
                               address_state=form.address_state.data)

        # cafes can have the same name
        db.session.add(new_cafe)
        db.session.commit()

        return redirect(f'/cafes/{new_cafe.id}')

    return render_template('/cafes/cafe_add.html', form=form)


@app.route('/cafes/<int:cafe_id>')
def cafe(cafe_id):
    """ Individual Cafe """

    # get cafe from db and pass to template

    cafe = Cafe.query.get_or_404(cafe_id)

    return render_template('/cafes/cafe.html', cafe=cafe)


@app.route('/users')
def users():
    """ User listings """

    users = User.query.all()
    return render_template('userslistings.html', users=users)

################################################################################
# User <> Cafe interactions

@app.post('/cafes/<int:cafe_id>/love')
@login_required
def cafe_love(cafe_id):
    """ add a cafe to user loves_cafes list """
    form = g.csrf_form

    if form.validate_on_submit:
        cafe = Cafe.query.get_or_404(cafe_id)
        current_user.loves_cafes.append(cafe)

        db.session.commit()

        flash('happy days, everyone knows about your <3', 'success')
        return redirect(url_for('cafes')) #TODO: get current page?

    abort(404)

@app.post('/cafes/<int:cafe_id>/unlove')
@login_required
def cafe_unlove(cafe_id):
    """ remove a cafe from user loves_cafes list """
    form = g.csrf_form

    if form.validate_on_submit:
        cafe = Cafe.query.get_or_404(cafe_id)
        current_user.loves_cafes.remove(cafe)
        db.session.commit()

        flash('somewhere, a heart lies broken', 'warning')
        return redirect(url_for('cafes'))

    abort(404)


#####TESTING
@app.route('/test')
def testroute():
    return render_template('cleantest.html')
