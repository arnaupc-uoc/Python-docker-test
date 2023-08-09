from flask import Blueprint
import click

bp = Blueprint('utils', __name__, cli_group='utils')

bp.cli.short_help = 'App Utilities'


# Util commands

@bp.cli.command('hello')
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your first name', help='The person to greet.')
def hello_cmd(count, name):
    # Simple program that greets NAME for a total of COUNT times.
    for _ in range(count):
        click.echo(f'Hello, {name}!')
