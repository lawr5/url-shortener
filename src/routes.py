from flask import render_template, request, redirect, url_for, Blueprint, flash
from datetime import date

from .extensions import db
from .models import *
from .forms import *

main = Blueprint("main", __name__)

@main.route("/")
def index():
    url_details = db.session.query(Urls)
    return render_template("index.html", url_details=url_details, current_user=current_user)


@main.route("/add_url", methods=["GET","POST"])
def add_url():

    if request.method == 'POST':

        short_url = request.form["short_url"]
        url_present = db.session.query(Urls).filter_by(short_url=short_url).first()
        
        if url_present:
            flash('Short URL already exists.')
            return redirect(url_for("main.add_url"))

        else:
            short_url = request.form["short_url"]
            long_url = request.form["long_url"]
            description = request.form["description"]
            created_by = current_user["user"]
            edited_by = current_user["user"]
            updated_on = date.today()
            last_used = date.today()

            new_url = Urls(short_url=short_url,
                           long_url=long_url,
                           description=description,
                           created_by=created_by,
                           edited_by=edited_by,
                           updated_on=updated_on,
                           last_used=last_used)
                    
            db.session.add(new_url)
            db.session.commit()
        flash('Short URL has been added.')
        return redirect(url_for("main.index"))
    
    return render_template("add.html", current_user=current_user)

@main.route("/delete_url/<int:id>", methods=["POST"])
def delete_url(id):
    url = Urls.query.get(id)

    db.session.delete(url)
    db.session.commit()
    
    return redirect(url_for("main.index"))

    
@main.route("/edit_url/<int:id>", methods=["GET","POST"])
def edit_url(id):

    if request.method == 'GET':

        current_url = db.session.query(Urls).filter_by(id=id)
        return render_template("edit.html", current_url=current_url, current_user=current_user)
    
    if request.method == 'POST':

        updated_url = db.session.query(Urls).filter_by(id=id).first()

        updated_url.short_url = request.form["short_url"]
        updated_url.long_url = request.form["long_url"]
        updated_url.description = request.form["description"]
        updated_url.edited_by = current_user["user"]
        updated_url.updated_on = date.today()

        db.session.commit()
        return redirect(url_for("main.index", updated_url=updated_url))
    

@main.route("/<short_url>")
def url_redirection(short_url):
    url_query = db.session.query(Urls).filter_by(short_url=short_url).first()
    return redirect(url_query.long_url)
