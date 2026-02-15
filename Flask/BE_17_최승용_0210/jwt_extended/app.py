from flask import Flask, render_template
from jwt_utils import configure_jwt
from routes.user import user_bp



app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "jwt-secret-key"

configure_jwt(app)

app.register_blueprint(user_bp, url_prefix="/user")

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)