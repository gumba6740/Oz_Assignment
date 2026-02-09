from flask import request, jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from db import DATABASE as db
from models import Board

board_blp = Blueprint("Boards", "boards", description="Operations on boards", url_prefix="/board")

@board_blp.route("/")
class BoardList(MethodView):
    
    def get(self):
        boards = Board.query.all()
        get_boards = []
        
        for board in boards:
            get_board = {
                "id": board.id,
                "title": board.title,
                "content": board.content,
                "user_id": board.user_id,
                "author_name": board.author.name,
                "email": board.author.email
                }
            get_boards.append(get_board)

        return jsonify(get_boards)


    def post(self):
        data = request.get_json()
        new_board = Board(title=data["title"], content=data["content"], user_id=data["user_id"])
        db.session.add(new_board)
        db.session.commit()
        
        return {"title": new_board.title, "content": new_board.content, "user_id": new_board.id}
    




@board_blp.route("/<int:board_id>")
class BoardOne(MethodView):

    def get(self, board_id):
        board = Board.query.get_or_404(board_id)

        return jsonify({"id": board.id,
                        "title": board.title,
                        "content": board.content,
                        "user_id": board.id
                        })

    def put(self, board_id):
        board = Board.query.get_or_404(board_id)
        data = request.get_json()
        board.title = data["title"]
        board.content = data["content"]

        db.session.commit()

        return jsonify({"id": board.id,
                "title": board.title,
                "content": board.content,
                "user_id": board.id
                })
    
    def delete(self, board_id):
        board = Board.query.get_or_404(board_id)
        db.session.delete(board)
        db.session.commit()

        return "message: board deleted"