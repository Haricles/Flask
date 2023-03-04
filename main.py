from flask import Flask,redirect,url_for,render_template,request
from pizzak import pizzak

app=Flask(__name__)


@app.route("/")
@app.route("/kezdolap")
def kezdolap():
    return render_template("kezdolap.html")

@app.route("/elerhetoseg")
def elerhetoseg():
    return render_template("elerhetoseg.html")

@app.route("/kepek")
def kepek():
    return render_template("kepek.html")

@app.route("/rolunk")
def rolunk():
    return render_template("rolunk.html")

@app.route("/rendeles")
def rendeles():
    return render_template("pizzak.html",pizzak=pizzak)



if __name__== "__main__":
    app.run(debug=True)