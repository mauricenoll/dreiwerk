import platform


def get_path(file_path_from_app_directory: str):
    if file_path_from_app_directory.startswith("/"):
        file_path_from_app_directory = file_path_from_app_directory[1:]

    if platform.system() == "Linux":
        return f"/code/app/{file_path_from_app_directory}"

    return file_path_from_app_directory
