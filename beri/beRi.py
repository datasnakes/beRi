import click


@click.group()
@click.option("--install", nargs=-1)
@click.option("--global")
def beri(install):
    packages = list(install)


@beri.command()
@beri.option("packages")
def install():
    pass
