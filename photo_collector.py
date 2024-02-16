# Replace 'owner', 'repo', and 'path_to_folder' with actual values
import requests
import json
import os


def directory_process(pth):
    current_directory = os.getcwd()
    pth = os.path.join(current_directory, pth)
    if os.path.exists(pth):
        return pth
    pth = f"personal_portfolio/{pth}"
    pth = os.path.join(current_directory, pth)
    if os.path.exists(pth):
        return pth
    return None


def get_cover_photos():
    owner = "hunthinniap"
    repo = "portfolio_asset"
    path = "Photography/cover_photos"

    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    response = requests.get(url)
    # Get contents of the specified folder
    contents = response.json()
    photo_collections = []
    cover_collections = []
    for content_file in contents:
        photo_info = {}
        photo_info["cover_url"] = content_file["download_url"]
        photo_info["title"] = content_file["name"][:-4]
        photo_info["link"] = f'/photography/{photo_info["title"]}'
        photo_collections.append(photo_info)
        cover_collections.append(photo_info["title"])

    pth = "photo_data/cover_photos.json"
    pth = directory_process(pth)
    with open(pth, "w") as outfile:
        json.dump(photo_collections, outfile)
    return cover_collections


def get_collection_details(collection_name):
    owner = "hunthinniap"
    repo = "portfolio_asset"
    path = f"Photography/{collection_name}"

    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    response = requests.get(url)
    # Get contents of the specified folder
    contents = response.json()
    # Get contents of the specified folder
    contents = response.json()
    photo_collections = []
    for content_file in contents:
        photo_info = {}
        photo_info["src"] = content_file["download_url"]
        photo_info["alt"] = ""
        photo_collections.append(photo_info)
    pth = f"photo_data/{collection_name}.json"

    with open(pth, "w") as outfile:
        json.dump(photo_collections, outfile)


if __name__ == "__main__":

    cover_collections = get_cover_photos()

    for collection_name in cover_collections:
        get_collection_details(collection_name)
