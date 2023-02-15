from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/rendeles")
def etlap():
    return render_template("rendeles.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/meretek")
def meretek():
    return render_template("meretek.html")

@app.route("/pizzak")
def pizzak():
    return render_template("pizzak.html")

@app.route("/elerhetoseg")
def elerhetoseg():
    return render_template("elerhetoseg.html")

@app.route("/kepek")
def kepek():
    return render_template("kepek.html")


if __name__=="__main__":
    app.run(debug=True)