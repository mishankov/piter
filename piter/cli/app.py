import shutil
import os
import sys
import subprocess

import typer

import piter.env
from piter.cli.utils import check_path_is_dir
import piter.cli.output as output
from piter.config import config

app = typer.Typer()

# TODO: analyze config for potential hiccups like pip install stuff
@app.command("config")
def print_config():
    typer.echo(f"{config.to_toml()}")


@app.command()
def env(
    name: str,
    install: bool = typer.Option(False, "--install", "-i"),
    remove: bool = typer.Option(False, "--remove", "-r"),
    reinstall: bool = typer.Option(False, "--reinstall", "-ri"),
):
    if remove or reinstall:
        try:
            shutil.rmtree(piter.env.env_path_by_name(name))
        except FileNotFoundError:
            output.info(f"Environment not found", name)
        else:
            output.info(f"Environment removed", name)

    if install or not check_path_is_dir(piter.env.env_path_by_name(name)):
        piter.env.create_env(name)
        output.info(f"Environment created", name)

    if install or reinstall:
        piter.env.install_dependencies(name)
        output.info(f"Dependencies installed", name)
        piter.env.generate_lockfile(name)
        output.info(f"Lockfile generated", name)


# TODO: try to determine env for run script on if no environment arg provided
# TODO: if environment does not exists, create it and install dependencies
# TODO: error like this (pytest was already installed and has executable): [piter][ci][ERROR] - Script line finished with error: piter_envs/ci/venv/bin/pip install piter_envs/ci/venv/bin/pytest pyyaml
# TODO: error like this (pip was already installed): [piter][ci][ERROR] - Script line finished with error: piter_envs/ci/venv/bin/pip install --upgrade piter_envs/ci/venv/bin/pip
@app.command("run")
def execute_script(
    script: str, environment: str = typer.Option("", "--environment", "-e")
):
    exec_status = 0
    
    for script_line in config.env[environment].scripts[script]:
        env_execs = piter.env.env_execs(environment)
        command = []
        for command_part in script_line.split(" "):
            if command_part in env_execs:
                command_part = os.path.join(
                    piter.env.env_path_by_name(environment), "bin", command_part
                )
            command.append(command_part)

        try:
            subprocess.check_call(command)
            output.success(
                f"Script line executed successfully: {output.path(' '.join(command))}",
                environment,
            )
        except subprocess.CalledProcessError:
            output.error(
                f"Script line finished with error: {output.path(' '.join(command))}",
                environment,
            )
            exec_status = 1

    sys.exit(exec_status)
