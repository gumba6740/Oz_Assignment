from flask import request, jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from db import DATABASE as db
from models import User

user_blp = Blueprint("users", "users", description="Operations on users", url_prefix="/user")


@user_blp.route("/")
class UserList(MethodView):

    def get(self):
        get_users = []
        users = User.query.all()
        user = User.query.first()
        print("===============", user.id)
        for user in users:
            get_user = {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "board_count": user.boards.count()
            }
            get_users.append(get_user)
        
        return get_users
    

    def post(self):
        data = request.get_json()
        new_user = User(name= data["name"], email = data["email"])
        db.session.add(new_user)
        db.session.commit()

        user = {
            "name": data["name"],
            "email": data["email"]
            }
        
        return jsonify(user)
    

@user_blp.route("/<int:user_id>")
class UserOne(MethodView):

    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        
        return {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "board_count": user.boards.count()
        }
    
    def put(self, user_id):
        data = request.get_json()
        user = User.query.get_or_404(user_id)
        user.name = data["name"]
        user.email = data["email"]
        db.session.add(user)
        db.session.commit()

        return {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "board_count": user.boards.count()
        }
    
    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()

        return "message: user deleted"