users = [
    {"username": "leo", "posts": [{"title": "Town House", "likes": 120}]},
    {"username": "alex", "posts": [{"title": "Mountain Climbing", "likes": 350}, {"title": "River Rafting", "likes": 200}]},
    {"username": "kim", "posts": [{"title": "Delicious Ramen", "likes": 230}]}
]

def add_user(request_data):
    new_user = {"username": request_data["username"], "posts": []}
    users.append(new_user)
    return new_user, 201

def add_post_to_user(username, request_data):
    for user in users:
        if user["username"] == username:
            new_post = {"title": request_data["title"], "likes": 0}
            user["posts"].append(new_post)
            return new_post, 201
    return {"message": "User not found"}, 404

def get_user_posts(username):
    for user in users:
        if user["username"] == username:
            return {"posts": user["posts"]}
    return {"message": "User not found"}, 404

def like_user_post(username, title):
    for user in users:
        if user["username"] == username:
            for post in user["posts"]:
                if post["title"] == title:
                    post["likes"] += 1
                    return post, 200
    return {"message": "Post not found"}, 404

def delete_user(username):
    global users
    users = [user for user in users if user["username"] != username]
    return {"message": "User deleted"}, 200