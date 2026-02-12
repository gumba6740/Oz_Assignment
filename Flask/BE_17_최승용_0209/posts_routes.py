from flask import request, jsonify
from flask_smorest import Blueprint, abort
from sqlalchemy import text


def create_posts_blueprint(SessionLocal):
    posts_blp = Blueprint("posts", __name__, description="posts api", url_prefix="/posts")

    @posts_blp.route("/", methods=["GET", "POST"])
    def posts():
        db = SessionLocal()

        if request.method == "GET":
            sql = text("SELECT * FROM posts")
            posts = db.execute(sql).fetchall()
            
            post_list = []
            for post in posts:
                post_list.append({
                    "id": post[0],
                    "title": post[1],
                    "content": post[2]
                })
            
            db.close()
            return jsonify(post_list)
        
        if request.method == "POST":
            title = request.json.get("title")
            content = request.json.get("content")
            if not title or not content:
                abort(400, message="title or content cannot be empty")
            
            sql = text("INSERT INTO posts(title, content) VALUES(:title, :content)")
            db.execute(sql, {"title": title, "content": content})
            db.commit()
            db.close()

            return jsonify({"msg": "successfully created post data",
                            "title": title,
                            "content": content})
        
    @posts_blp.route("/<int:id>", methods=["GET", "PUT", "DELETE"])
    def post(id):
        db = SessionLocal()
        sql = text(f"SELECT * FROM posts WHERE id = {id}")
        post = db.execute(sql).fetchone()

        if request.method == "GET":
            db.close()

            if not post:
                abort(404, message="Post not found")
            
            return jsonify({"id": post[0],
                            "title": post[1],
                            "content": post[2]
                        })

        elif request.method == "PUT":
            title = request.json.get("title")
            content = request.json.get("content")

            if not post or not title or not content:
                db.close()
                abort(400, "Not found title or content")

            sql = text(f"UPDATE posts SET title = '{title}', content = '{content}' WHERE id = {id}")
            db.execute(sql)
            db.commit()
            db.close()

            return jsonify({"msg": "successfully updated title & content"})

        elif request.method == "DELETE":
            if not post:
                db.close()
                abort(404, message="Post not found")
            sql = text(f"DELETE FROM posts WHERE id = {id}")
            db.execute(sql)
            db.commit()
            db.close()

            return jsonify({"msg": "successfully deleted title & content"})
    
    return posts_blp

            
        # if request.method == "GET":
        #     sql = "SELECT * FROM posts"
        #     cursor.execute(sql)

        #     posts = cursor.fetchall()
        #     cursor.close()

        #     post_list = []

        #     for post in posts:
        #         post_list.append({
        #             "id": post[0],
        #             "title": post[1],
        #             "content": post[2]
        #         })
            
        #     return jsonify(post_list)


