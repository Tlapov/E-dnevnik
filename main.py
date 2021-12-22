
from flask import Flask, render_template, request, make_response, redirect, url_for
from models import db, Ucenik
import datetime

app = Flask(__name__)

db.create_all()

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "GET":
       year = datetime.datetime.now().year
       return render_template("index.html", year=year)
    elif request.method == "POST":
        name = request.form.get("name")
        birth = request.form.get("godina")
        direction = request.form.get("smjer")
        classroom = request.form.get("razred")
        average = request.form.get("prosjek")
        year = datetime.datetime.now().year

        ucenik = Ucenik(ime_prezime=name, god_rod=birth, smjer=direction, razred=classroom, prosjek=average)
        ucenik.save()
        return render_template("uspjeh.html", year=year)

@app.route("/E-dnevnik")
def e_dnevnik():
    diary = db.query(Ucenik).all()
    year = datetime.datetime.now().year
    return render_template("E-dnevnik.html", diary=diary, year=year)

@app.route("/Kontakt")
def kontakt():
    year = datetime.datetime.now().year
    return render_template("Kontakt.html", year=year)

if __name__ == "__main__":
    app.run(use_reloader=True)