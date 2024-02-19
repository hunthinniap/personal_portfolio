from flask import Flask, render_template
import git

import requests
from reader import (
    read_collections,
    read_cover,
    read_page_title,
    read_page_description,
    read_music_cover,
    read_music_specs,
    read_blog_spces,
    read_blog_content,
    read_video_link,
    read_video_specs,
)


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


@app.route("/music")
def music():
    cover_collections = read_music_cover()
    return render_template("music.html", collections=cover_collections)


@app.route("/music/<music_title>")
def music_template(music_title):
    music_specs = read_music_specs(music_title)
    lyrics = requests.get(music_specs['lyrics']).text
    motivation = requests.get(music_specs['Motivation']).text
    return render_template(
        "music_template.html",specs = music_specs,
        lyrics = lyrics,
        motivation=motivation,
    )


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

@app.route("/blog")
def blog():
    specs = read_blog_spces()
    return render_template("blog.html", specs = specs) 

@app.route("/blog/<blog_name>")
def blog_template(blog_name):
    blog = read_blog_content(blog_name)
    return render_template("blog_template.html", blog = blog, tilte=blog_name) 

@app.route("/videography")
def videography():
    specs = read_video_specs()
    return render_template("videography.html", videos = specs) 

@app.route("/about")
def about():
    # Read the content from the text file
    response = requests.get('https://raw.githubusercontent.com/hunthinniap/portfolio_asset/main/About/journal.txt')
    dev_journey_content = response.text

    response = requests.get("https://raw.githubusercontent.com/hunthinniap/portfolio_asset/main/About/description.txt")
    description = response.text 
        
    # Render the about.html template with the content of the text file
    return render_template('about.html', dev_journey_content=dev_journey_content, description=description)


@app.route("/template")
def template():
    return render_template("template.html")


if __name__ == "__main__":
    app.run(debug=True)
