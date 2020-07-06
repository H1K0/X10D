import click
from datetime import datetime as dt


@click.group()
def cli():
	pass


@click.command()
def now():
	"""What's time?"""
	print(f'Right now: {dt.utcnow()}')
cli.add_command(now)


if __name__=='__main__':
	cli()