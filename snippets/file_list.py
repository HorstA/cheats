import os
from datetime import datetime


def list_files(directory, recursive):
    file_list = []
    if recursive:
        for root, dirs, files in os.walk(directory):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                last_modified_date = datetime.fromtimestamp(os.path.getmtime(file_path))
                file_list.append((file_path, last_modified_date))
    else:
        for file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)
            if os.path.isfile(file_path):
                last_modified_date = datetime.fromtimestamp(os.path.getmtime(file_path))
                file_list.append((file_path, last_modified_date))
    return file_list


def print_file_list(file_list):
    for file_path, last_modified_date in file_list:
        print(f"{file_path} - {last_modified_date}")


if __name__ == "__main__":
    directory = input("Bitte geben Sie das Verzeichnis ein: ")
    recursive_choice = (
        input("Soll das Verzeichnis rekursiv durchsucht werden? (y/n): ")
        .strip()
        .lower()
    )
    recursive = recursive_choice == "y"
    file_list = list_files(directory, recursive)
    print_file_list(file_list)
