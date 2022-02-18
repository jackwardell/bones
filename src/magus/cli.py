import click


@click.group()
def app() -> None:
    pass


@app.command()
def hello():
    print("hello")


@app.command()
def greet():
    click.echo("Hello, World!")


if __name__ == "__main__":
    app()
