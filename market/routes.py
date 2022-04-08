from crypt import methods
from requests import request
from market import app
from flask import flash, redirect, render_template, url_for
from market.model import Item, User
from market import db
from market.forms import RegisterForm


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
            password=form.password1.data,
        )

        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for("product_page"))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"Error creating a user : {err_msg}", category="danger")

    return render_template("register.html", form=form)


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
