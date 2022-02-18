import click
from magus.app import CliApp


@click.group()
@click.pass_context
def app(ctx: click.Context) -> None:
    ctx.obj = {"app": CliApp()}


@app.command()
@click.pass_context
def init(ctx: click.Context) -> None:
    click.echo("initialising project")
    ctx.obj["app"].init()
    click.echo("project initialised")


if __name__ == "__main__":
    app()
