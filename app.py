from flask import Flask, render_template
from sqlalchemy import create_engine

# database setup 
engine = create_engine("sqlite:///titanic.sqlite")

# flask app setup
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/names")
def names():
    results = [
        {
            "id": list(row)[0],
            "name": list(row)[1],
            "pclass": list(row)[2],
            "age": list(row)[3],
            "sex": list(row)[4],
            "survived": list(row)[5],
        } for row in engine.execute("select * from passenger").all()]

    return {"passengers":results}

if __name__ == '__main__':
    app.run(debug=True)
