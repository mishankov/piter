import toml


def shrink_dependencies(dependencies: list[str]) -> list[str]:
    return list(map(lambda a: a.replace(" ", ""), dependencies))


def load_config():
    return toml.load("pyproject.toml")["tools"]["piter"]
