import click


@click.command()
@click.option("--install", nargs=-1)
def beri(install):
    packages = list(install)
    pass
