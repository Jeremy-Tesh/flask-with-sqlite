from crypt import methods
from nis import cat
from requests import request
from market import app
from flask import flash, redirect, render_template, url_for
from market.model import Item, User
from market import db
from market.forms import LoginForm, RegisterForm
from flask_login import login_user


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/products")
def product_page():
    items = Item.query.all()

    return render_template("market.html", items=items)


@app.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(
            username=form.username.data,
            email=form.username.data,
            password_hash=form.password1.data,
        )

        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for("product_page"))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"Error creating a user : {err_msg}", category="danger")

    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password(
            attempted_password=form.password1.data
        ):
            login_user(attempted_user)
            flash(
                f"Success! Logged in as {attempted_user.username}", category="success"
            )
            return redirect(url_for("product_page"))

        else:
            flash("Username and password donot match!!", category="danger")

    return render_template("login.html", form=form)


# @app.route("/add", methods=["GET", "POST"])
# def add():
#     return render_template("add.html")
# item_name = request.form["name"]
# item_price = request.form["price"]
# item_barcode = request.form["barcode"]
# item_description = request.form["description"]
# new_item = Item(
#     name=item_name,
#     price=item_price,
#     barcode=item_barcode,
#     description=item_description,
# )
# db.session.add(new_item)
# db.session.commit()
# return redirect("/features")
