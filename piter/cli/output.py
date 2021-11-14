import typer


def log(message, environment_name=""):
    typer.echo(f"[piter][{environment(environment_name)}]{message}")


def success(message, environment=""):
    log(
        f"[{typer.style('SUCCESS', bold=True, fg=typer.colors.GREEN)}] - {message}",
        environment,
    )


def error(message, environment=""):
    log(
        f"[{typer.style('ERROR', bold=True, fg=typer.colors.RED)}] - {message}",
        environment,
    )


def info(message, environment=""):
    log(
        f"[{typer.style('INFO', bold=True, fg=typer.colors.BLUE)}] - {message}",
        environment,
    )


def path(path):
    return typer.style(path, italic=True)


def environment(name):
    return typer.style(name, bold=True)


def dependency(name):
    return typer.style(name, italic=True)
