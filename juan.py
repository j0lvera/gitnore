import zipfile
import argparse
import urllib.request
from pathlib import Path

from appdirs import AppDirs

"""
 ▐▄▄▄▄• ▄▌ ▄▄▄·  ▐ ▄
  ·███▪██▌▐█ ▀█ •█▌▐█
▪▄ ███▌▐█▌▄█▀▀█ ▐█▐▐▌
▐▌▐█▌▐█▄█▌▐█ ▪▐▌██▐█▌
 ▀▀▀• ▀▀▀  ▀  ▀ ▀▀ █▪
"""

# gitignore repo url
gitignore_url = "https://github.com/github/gitignore/archive/master.zip"

# Standard data directory
dirs = AppDirs("juan")
user_data_dir = dirs.user_data_dir

# Gitignore file destination full path
gitignore_zip_file = f"{user_data_dir}/main.zip"

# Gitignore contents directory
gitignore_directory = f"{user_data_dir}/gitignore-main/"

parser = argparse.ArgumentParser()
parser.add_argument("--update", action="store_true")
parser.add_argument("--list", action="store_true")
parser.add_argument("--generate")
args = parser.parse_args()


def download_gitignore(url: str):
    # Create folder if it doesn't exist
    if not Path.exists(Path(user_data_dir)):
        Path(user_data_dir).mkdir(parents=True, exist_ok=True)

    # Download files
    urllib.request.urlretrieve(url, f"{user_data_dir}/main.zip")


def extract_zip(file: str):
    with zipfile.ZipFile(file, mode="r") as archive:
        archive.extractall(user_data_dir)


def get_list_of_files():
    return Path(gitignore_directory).rglob("*.gitignore")


def format_name(file_name: str):
    file_name = file_name.replace(".gitignore", "")
    return file_name.lower()


def print_available_files():
    files = get_list_of_files()
    only_names = sorted([format_name(file.name) for file in files])
    print((",").join(only_names))


def find_file_by_names(file_names: str):
    search_queries = file_names.split(",")
    files = get_list_of_files()
    results = dict(found=[], not_found=[])

    if search_queries:
        for file in files:
            for query in search_queries:
                if query == format_name(file.name):
                    results["found"].append(file)

        for query in search_queries:
            if query not in [format_name(item.name) for item in results["found"]]:
                results["not_found"].append(query)

    return results


def convert_to_list_of_strings(posix_path_list):
    return [item.name for item in posix_path_list]


def print_gitignore(files):
    for file in files:
        with open(file) as f:
            print("#### juan made this: https://github.com/j0lv3r4/juan ####")
            print(f"\n### {file.name.replace('.gitignore', '')} ###\n")
            print(f.read())


def main():
    if args.update:
        print("Updating gitignore files...")
        download_gitignore(gitignore_url)
        extract_zip(gitignore_zip_file)

    if args.list:
        print_available_files()

    if args.generate:
        list_of_files = find_file_by_names(args.generate)

        if list_of_files.get("not_found"):
            print(f"Unsupported file(s): {(', ').join(list_of_files.get('not_found'))}")
            print(f"Run `juan --list` to see a list of available gitignores.")
        else:
            print_gitignore(list_of_files.get("found"))


if __name__ == "__main__":
    main()
