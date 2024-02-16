from flask import Flask, render_template
import git
from reader import read_collections, read_cover, read_page_title, read_page_description

app = Flask(__name__)


@app.route("/git_update", methods=["POST"])
def git_update():
    repo = git.Repo("./personal_portfolio")
    origin = repo.remotes.origin
    repo.create_head("main", origin.refs.main).set_tracking_branch(
        origin.refs.main
    ).checkout()
    origin.pull()
    return "", 200


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/photography")
def photography():
    photo_collections = read_cover()
    return render_template("photography.html", collections=photo_collections)


"""
@app.route('/music')
def photography():
    photo_collections = get_music_cover_photos()
    return render_template('music.html', collections=photo_collections)
"""


@app.route("/photography/<collection_name>")
def photo_collection(collection_name):
    # Fetch the photo collection details based on collection_name
    photos = read_collections(collection_name)
    title = read_page_title(collection_name)
    description = read_page_description(collection_name)
    return render_template(
        "photo_collections.html",
        page=collection_name,
        photos=photos,
        title=title,
        description=description,
    )


@app.route("/template")
def template():
    return render_template("template.html")


if __name__ == "__main__":
    app.run(debug=True)
