# Replace 'owner', 'repo', and 'path_to_folder' with actual values
from github import Github

g = Github()
import json


def get_cover_photos():
    owner = "hunthinniap"
    repo_name = "portfolio_asset"
    path_to_folder = "Photography/cover_photos"
    repo = g.get_repo(f"{owner}/{repo_name}")

    # Get contents of the specified folder
    contents = repo.get_contents(path_to_folder)
    photo_collections = []
    cover_collections = []
    for content_file in contents:
        photo_info = {}
        photo_info["cover_url"] = content_file.download_url
        photo_info["title"] = content_file.name[:-4]
        photo_info["link"] = f'/photography/{photo_info["title"]}'
        photo_collections.append(photo_info)
        cover_collections.append(photo_info["title"])

    with open("photo_data/cover_photos.json", "w") as outfile:
        json.dump(photo_collections, outfile)
    return cover_collections


def get_collection_details(collection_name):
    owner = "hunthinniap"
    repo_name = "portfolio_asset"
    path_to_folder = f"Photography/{collection_name}"

    repo = g.get_repo(f"{owner}/{repo_name}")

    # Get contents of the specified folder
    contents = repo.get_contents(path_to_folder)
    photo_collections = []
    for content_file in contents:
        photo_info = {}
        photo_info["src"] = content_file.download_url
        photo_info["alt"] = ""
        photo_collections.append(photo_info)

    with open(f"photo_data/{collection_name}.json", "w") as outfile:
        json.dump(photo_collections, outfile)


if __name__ == "__main__":
    cover_collections = get_cover_photos()
    for collection_name in cover_collections:
        get_collection_details(collection_name)
