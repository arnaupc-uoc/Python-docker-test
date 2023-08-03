from flask import Blueprint
from flask.cli import with_appcontext
import click

bp = Blueprint('utils', __name__, cli_group='utils')

bp.cli.short_help = 'App Utilities'

# Util commands

@bp.cli.command('hello')
@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
@with_appcontext
def hello_cmd(count, name):
    # Simple program that greets NAME for a total of COUNT times.
    for _ in range(count):
        click.echo(f'Hello, {name}!')
