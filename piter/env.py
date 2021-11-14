import venv
import os
import subprocess

from piter.config import config
import piter.env


def env_path_by_name(name: str):
    return os.path.join(config.env_root, name, "venv")


def env_lockfile_by_name(name: str):
    return os.path.join(config.env_root, name, "dependencies.lock")


def env_execs(name: str) -> list[str]:
    return [
        file
        for file in os.listdir(os.path.join(piter.env.env_path_by_name(name), "bin"))
        if os.path.isfile(
            os.path.join(os.path.join(piter.env.env_path_by_name(name), "bin"), file)
        )
    ]


def generate_lockfile(name: str):
    dependencies: bytes = subprocess.check_output(
        [os.path.join(env_path_by_name(name), "bin", "python"), "-m", "pip", "freeze"]
    )
    lock_file = open(env_lockfile_by_name(name), "w")
    lock_file.write(dependencies.decode("utf-8"))
    lock_file.close()


def install_dependencies(name: str):
    deps: list[str] = []

    try:
        lockfile = open(env_lockfile_by_name(name))
        deps = lockfile.readlines()
    except FileNotFoundError:
        deps = config.env[name].dependencies

    if deps and len(deps) > 0:
        subprocess.check_call(
            [
                os.path.join(piter.env.env_path_by_name(name), "bin", "python"),
                "-m",
                "pip",
                "install",
            ]
            + deps
        )


def create_env(name: str):
    # TODO: all params must be configurable
    new_venv = venv.EnvBuilder(
        system_site_packages=False,
        clear=False,
        symlinks=True,
        upgrade=False,
        with_pip=True,
        prompt=name,
        upgrade_deps=False,
    )
    new_venv.create(env_path_by_name(name))
