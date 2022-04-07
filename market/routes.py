from crypt import methods

from requests import request
from market import app
from flask import redirect, render_template
from market.model import Item
from market import db


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/features")
def features():
    items = Item.query.all()

    return render_template("market.html", items=items)


@app.route("/add", methods=["GET", "POST"])
def add():
    return render_template("add.html")
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
