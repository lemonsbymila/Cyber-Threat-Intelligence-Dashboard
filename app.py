from flask import Flask, render_template, request

app = Flask(__name__)

# simple in-memory storage
cases = []

@app.route("/")
def dashboard():
    return render_template("dashboard.html", cases=cases)

@app.route("/new-case", methods=["GET", "POST"])
def new_case():
    if request.method == "POST":
        case = {
            "id": request.form["case_id"],
            "analyst": request.form["analyst"],
            "risk": request.form["risk"]
        }
        cases.append(case)
        return render_template("dashboard.html", cases=cases)

    return render_template("new_case.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    result = None

    if request.method == "POST":
        search_id = request.form["search_id"]
        result = next((c for c in cases if c["id"] == search_id), None)

    return render_template("search.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)