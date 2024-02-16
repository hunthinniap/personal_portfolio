import json
import requests

from text_data import page_alt, page_description


def read_cover():
    url = "https://raw.githubusercontent.com/hunthinniap/portfolio_asset/main/Photography/cover_photos/photos.json"
    response = requests.get(url)
    cover_photos = json.loads(response.text)
    return cover_photos


def read_collections(collection_name):
    url = f"https://raw.githubusercontent.com/hunthinniap/portfolio_asset/main/Photography/{collection_name}/photos.json"

    response = requests.get(url)
    collections = json.loads(response.text)
    return collections


def read_page_title(page):
    return page_alt.get(page, "")


def read_page_description(page):
    return page_description.get(page, "")



