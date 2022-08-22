from flask import Blueprint, request, render_template
from service import find_posts
from json import JSONDecodeError
import logging

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")


@main_blueprint.route("/")
def main_page():
    return render_template("index.html")


@main_blueprint.route("/search")
def search_page():
    search_word = request.args.get("s", "")
    logging.info(f"Выполняю поиск \"{search_word}\"")
    try:
        posts = find_posts(search_word)
    except FileNotFoundError:
        logging.info("Файл не найден")
        return "Файл не найден"
    except JSONDecodeError:
        return "Невалидный файл"
    return render_template("post_list.html", search_word=search_word, posts=posts)
