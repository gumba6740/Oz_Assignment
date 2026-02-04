from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def view():

    users = [
        {"username": "gumba", "name": "최승용"},
        {"username": "goomba", "name": "김벽돌"},
        {"username": "geumba", "name": "김짱돌"}
    ]

    return render_template("index.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)