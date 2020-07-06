import click
from os import access,F_OK


@click.group()
def cli():
	"""===== X10D (extend) your CMD! ====="""
	pass


@click.command()
def now():
	"""What's time?"""
	from datetime import datetime as dt
	genzai=dt.today()
	print(f'Right now: {genzai.year}-{str(genzai.month).rjust(2,"0")}-{str(genzai.day).rjust(2,"0")} '
		  f'{str(genzai.hour).rjust(2,"0")}:{str(genzai.minute).rjust(2,"0")}:{str(genzai.second).rjust(2,"0")}')
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

'''
@click.command()
@click.argument('files',nargs=-1,metavar='<file [file [...]]>')
def md(files):
	pass
cli.add_command(md)
'''


if __name__=='__main__':
	cli()