from flask import Flask, render_template, request, redirect, url_for
import sys

app = Flask(__name__)

@app.route('/main')
def main():
    return render_template("main.html")

@app.route("/coach")
def coach():
    return render_template("coach.html")

@app.route("/result_coach", methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result_coach.html", result = result)

@app.route("/apply_coach")
def applycoach():
    name = request.args.get("name")
    type1 = request.args.get("type1")
    years = request.args.get("years")
    intro = request.args.get("intro")
    print(name, type1, years, intro)
    
    database.save(name, type1, years, intro)
    return render_template("apply_coach.html")

@app.route("/court")
def court():
    return render_template("court.html")

@app.route("/partner")
def partner():
    return render_template("partner.html")

if __name__ == '__main__':
    app.run(debug=True)