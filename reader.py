import json
import os
from photo_collector import get_cover_photos, get_collection_details
from text_data import page_alt, page_description


def read_cover():
    pth = "photo_data/cover_photos.json"
    current_directory = os.getcwd()

    print("The current working directory is:", current_directory)
    if not os.path.exists(pth):
        get_cover_photos()
    with open(pth, "r") as file:
        cover_photos = json.load(file)
    return cover_photos


def read_collections(collection_name):
    pth = f"photo_data/{collection_name}.json"
    if not os.path.exists(pth):
        get_collection_details(collection_name)
    with open(pth, "r") as file:
        collections = json.load(file)
    return collections


def read_page_title(page):
    return page_alt.get(page, "")


def read_page_description(page):
    return page_description.get(page, "")
