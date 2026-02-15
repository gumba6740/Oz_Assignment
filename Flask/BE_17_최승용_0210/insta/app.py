from flask import Flask, request, render_template

app = Flask(__name__)



users = [
    {
        "username": "leo",
        "posts": [{"title": "Town House", "likes": 120}]
    },
    {
        "username": "alex",
        "posts": [{"title": "Mountain Climbing", "likes": 350}, {"title": "River Rafting", "likes": 200}]
    },
    {
        "username": "kim",
        "posts": [{"title": "Delicious Ramen", "likes": 230}]
    }
]

@app.get("/")
def index():
    # 모든 사용자 정보를 JSON 형태로 반환
    return render_template('index.html')

@app.get("/users")
def get_users():
    # 모든 사용자 정보를 JSON 형태로 반환
    return {"users": users}


@app.post("/users")
def create_user():
    
    request_data = request.get_json()
    
    new_user = {"username": request_data["username"], "posts": [{"title": "My First Post", "likes": 0}]}
    
    users.append(new_user)
    
    return new_user, 201

@app.post("/users/post/<string:username>")
def add_post(username):
    
    request_data = request.get_json()
    
    for user in users:
        if user["username"] == username:
            new_post = {"title": request_data["title"], "likes": request_data["likes"]}
            user["posts"].append(new_post)
            return new_post
        
    return {"message": "User not found"}, 404

@app.get("/users/post/<string:username>")
def get_posts_of_user(username):
    
    for user in users:
        if user["username"] == username:
            return {"posts": user["posts"]}
    
    return {"message": "User not found"}, 404

@app.put("/users/post/like/<string:username>/<string:title>")
def like_post(username, title):
    
    for user in users:
        if user["username"] == username:
            for post in user["posts"]:
                if post["title"] == title:
                    post["likes"] += 1
                    return post
    
    return {"message": "Post not found"}, 404

@app.delete("/users/<string:username>")
def delete_user(username):
    
    global users
    users = [user for user in users if user["username"] != username]
    
    return {"message": "User deleted"}, 200


if __name__ == '__main__':
    app.run(debug=True)