import click


@click.group()
@click.pass_context
def app(ctx: click.Context) -> None:
    ctx.obj = {"app": app}


@app.command()
@click.pass_context
def init(ctx: click.Context) -> None:
    click.echo("initialising project")


if __name__ == "__main__":
    app()
