from flask import Flask
from db import make_engine, make_session
import yaml
from flask_smorest import Api
import os
from posts_routes import create_posts_blueprint

BASE_DIR = os.path.dirname(__file__)
yaml_path = os.path.join(BASE_DIR, "db.yaml")

with open(yaml_path) as f:
    db_info = yaml.load(f, Loader=yaml.FullLoader)
engine = make_engine(db_info)

SessionLocal = make_session(engine)

app = Flask(__name__)

app.config['API_TITLE'] = "Blog API List"
app.config["API_VERSION"] = '1.0'
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
posts_blp = create_posts_blueprint(SessionLocal)
api.register_blueprint(posts_blp)


from flask import render_template

@app.route("/blog")
def manage_blogs():
    return render_template("posts.html")

if __name__ == "__main__":
    app.run(debug=True)








"""
app = Flask(__name__)

db_info = yaml.load(open("db.yaml"), Loader=yaml.FullLoader)
mysql-host: "localhost"
.
.
.

app.config[“MYSQL_HOST”] = db_info["mysql-host"]
app.config["MYSQL-USER"]
app.config["MYSQL_PASSWORD"]
app.config["MYSQL_DB"]
"""