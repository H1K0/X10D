import click
from os import access,F_OK
from datetime import datetime as dt


@click.group()
def cli():
	pass


@click.command()
def now():
	"""What's time?"""
	print(f'Right now: {dt.utcnow()}')
cli.add_command(now)

@click.command()
@click.argument('files',nargs=-1,metavar='<file [file [...]]>')
def binv(files):
	"""Invert FILE(S) bitwisely."""
	for file in files:
		if not access(file,F_OK):
			print(f"'{file}' not found.")
			continue
		with open(file,'rb') as plain:
			plainbytes=list(plain.read())
			cryptbytes=[]
			for byte in plainbytes:
				cryptbytes.append(255-int(byte))
		with open(file,'wb') as crypt:
			crypt.write(bytes(cryptbytes))
		print(f"'{file}' successfully inverted.")
cli.add_command(binv)


if __name__=='__main__':
	cli()