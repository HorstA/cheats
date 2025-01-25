import os
import re
from datetime import datetime


def list_files(directory, recursive):

    path = "/your/directory/path"
    exclude_patterns = r".*\.(jpg|png|gif|wav|avi|mp4|mkv|mov|pst|zip)$"  # Match files ending with the specified extensions
    include_patterns = r".*\.(txt|doc|docx|pdf)$"

    file_list = []
    if recursive:
        for root, dirs, files in os.walk(directory):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                if re.search(include_patterns, file_path):
                    file_list.append(
                        {
                            "file_name": file_path,
                            "file_size": os.path.getsize(file_path),
                            "last_modified": datetime.fromtimestamp(
                                os.path.getmtime(file_path)
                            ),
                        }
                    )
    else:
        for file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)
            if os.path.isfile(file_path) and re.search(include_patterns, file_path):
                file_list.append(
                    {
                        "file_name": file_path,
                        "file_size": os.path.getsize(file_path),
                        "last_modified": datetime.fromtimestamp(
                            os.path.getmtime(file_path)
                        ),
                    }
                )
    return file_list


def print_file_list(file_list):
    for file in file_list:
        print(f"{file["file_name"]} - {file["file_size"]} - {file["last_modified"]}")


if __name__ == "__main__":
    directory = input("Bitte geben Sie das Verzeichnis ein: ")
    recursive_choice = (
        input("Soll das Verzeichnis rekursiv durchsucht werden? (y/n): ")
        .strip()
        .lower()
    )
    recursive = recursive_choice == "y"
    file_list = list_files(directory, recursive)
    # Sort by the 'age' key
    sorted_list = sorted(file_list, key=lambda x: x["file_size"], reverse=True)
    print_file_list(sorted_list[:20])
