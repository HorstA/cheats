import tomllib


def get_version_from_pyproject():
    with open("pyproject.toml", "rb") as f:
        data = tomllib.load(f)
    return data["tool"]["poetry"]["version"]


# Example usage
version = get_version_from_pyproject()
print(f"Version: {version}")
