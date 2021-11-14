import toml
from pprint import pprint

a = toml.load("pyproject.toml")

pprint(a["tools"]["piter"])

file = open("py.toml", "w")
toml.dump(a, file)
file.close()