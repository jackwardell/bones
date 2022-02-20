import click

from .app import XYZApp


@click.group()
@click.pass_context
def app(ctx: click.Context) -> None:
    ctx.obj = {"app": XYZApp()}


@app.command()
@click.option("user_id", type=str)
@click.option("email_address", type=str)
@click.pass_context
def get_user(ctx: click.Context, user_id: str, email_address: str) -> None:
    user = ctx.obj["app"].get_user(
        user_id=user_id,
        email_address=email_address,
    )
    click.echo(user)


@app.command()
@click.option("email_address", type=str)
@click.option("password_hash", type=str)
@click.pass_context
def create_user(
    ctx: click.Context, email_address: str, password_hash: str
) -> None:
    user = ctx.obj["app"].create_user(
        email_address=email_address,
        password_hash=password_hash,
    )
    click.echo(user)


if __name__ == "__main__":
    app()
