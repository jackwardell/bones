import click
from magus.app import CliApp
from magus.app import CliAppOutput


@click.group()
@click.pass_context
def app(ctx: click.Context) -> None:
    ctx.obj = {"app": CliApp()}


@app.command()
@click.pass_context
def init(ctx: click.Context) -> None:
    click.echo("initialising project")
    output: CliAppOutput = ctx.obj["app"].init()
    for msg in output:
        click.echo(msg)
    click.echo("project initialised")


if __name__ == "__main__":
    app()
