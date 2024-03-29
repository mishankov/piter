# PITER - virtual environments management tool for Python projects

[![PyPI](https://img.shields.io/pypi/v/piter)](https://pypi.org/project/piter/)
[![codecov](https://codecov.io/gh/mishankov/piter/branch/main/graph/badge.svg?token=13EL00ZJO9)](https://codecov.io/gh/mishankov/piter)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/mishankov/piter.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/mishankov/piter/alerts/)

## Idea
While working on Python project you may need multiple virtual environments. You can divide your development and test environments, have multiple environments to test against different version of libraries or any other use cases

## Minimal configuration

Install `piter` with

```bash
pip install piter
```

Create or update `pyproject.toml` file with following configuration

```toml
[tool.piter]

[tool.piter.env.test]
dependencies = [
	"pytest==6.2.4", 
]
scripts.test = "pytest"

[tool.piter.env.dev]
dependencies = [
	"black==21.5b1",
]

scripts.lint = "black ."
scripts.check = "black --check ."
```

Available commands with this configuration

```bash
# install, remove and reinstall env 
piter env dev --install
piter env dev -i

piter env dev --remove
piter env dev -r

piter env dev --reinstall
piter env dev -ri


# run script without specifying env
piter run test

# run script
piter run dev:lint
```
