import json


def load_posts():
    with open("posts.json", "r",  encoding="utf-8") as i:
        return json.load(i)


def find_posts(word):
    suitable_posts = []
    for post in load_posts():
        if word.lower() in post["content"].lower():
            suitable_posts.append(post)
    return suitable_posts


def save_picture(picture):
    filename = picture.filename
    picture.save(f"./uploads/images/{filename}")
    return f"./uploads/images/{filename}"


def add_post(post):
    posts = load_posts()
    posts.append(post)
    with open("posts.json", "w", encoding="utf-8") as i:
        json.dump(posts, i)
    return post
