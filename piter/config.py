from dataclasses import dataclass

import toml


def shrink_dependencies(dependencies: list[str]) -> list[str]:
    return list(map(lambda a: a.replace(" ", ""), dependencies))


@dataclass
class EnvConfig:
    dependencies: list[str] = None
    scripts: dict[str, list[str]] = None


class Config:
    def __init__(self) -> None:
        self._config_from_file = toml.load("pyproject.toml")["tools"]["piter"]

        self.env: dict[str, EnvConfig] = {}

        for env_name, env_config in self._config_from_file["env"].items():
            self.env[env_name] = EnvConfig(**env_config)
            if self.env[env_name].dependencies and len(self.env[env_name].dependencies) > 0:
                self.env[env_name].dependencies = shrink_dependencies(
                    self.env[env_name].dependencies
                )

            for script_name, script in self.env[env_name].scripts.items():
                if isinstance(script, str):
                    self.env[env_name].scripts[script_name] = [script]

    def to_toml(self) -> str:
        output = {
            "tools": {
                "piter": {
                    "env_root": self.env_root,
                    "dependencies": self.dependencies,
                    "env": {
                        env_name: env_config.__dict__
                        for env_name, env_config in self.env.items()
                    },
                }
            }
        }
        return toml.dumps(output)

    @property
    def env_root(self) -> str:
        try:
            return self._config_from_file["env_root"]
        except:
            return "piter_envs"

    @property
    def dependencies(self) -> list:
        try:
            return shrink_dependencies(self._config_from_file["dependencies"])
        except:
            return []


config = Config()
