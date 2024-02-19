import json
import requests

from text_data import page_alt, page_description

base_url = "https://raw.githubusercontent.com/hunthinniap/portfolio_asset/main/"


def read_cover():
    url = f"{base_url}Photography/cover_photos/photos.json"
    response = requests.get(url)
    cover_photos = json.loads(response.text)
    return cover_photos


def read_collections(collection_name):
    url = f"{base_url}Photography/{collection_name}/photos.json"

    response = requests.get(url)
    collections = json.loads(response.text)
    return collections


def read_music_cover():
    url = f"{base_url}music_cover/photos.json"
    response = requests.get(url)
    cover_photos = json.loads(response.text)
    return cover_photos


def read_music_specs(music_name):
    url = f"{base_url}/music/{music_name}/specs.json"
    response = requests.get(url)
    specs = json.loads(response.text)
    return specs


def read_page_title(page):
    return page_alt.get(page, "")


def read_page_description(page):
    return page_description.get(page, "")

def read_blog_spces():
    url = f"{base_url}/Blog/blog_specs.json"
    response = requests.get(url)
    specs = json.loads(response.text)
    return specs

def read_blog_content(blog_name):
    url = f"{base_url}Blog/{blog_name}.txt"
    return requests.get(url).text

def read_video_specs():
    url = f"{base_url}/videography/specs.json"
    response = requests.get(url)
    specs = json.loads(response.text)
    return specs

def read_video_link(video_name):
    url = f"{base_url}/videography/specs.json"
    response = requests.get(url)
    specs = json.loads(response.text)
    for spec in specs:
        if spec['title'] == video_name:
            return spec['ytb_id']
