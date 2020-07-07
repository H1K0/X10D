import click
from os import access,F_OK


@click.group()
def CLI():
	"""===== X10D (extend) your CMD! ====="""
	pass


@CLI.command()
def now():
	"""What's time?"""
	from datetime import datetime as dt
	genzai=dt.today()
	print(f'{genzai.year}-{str(genzai.month).rjust(2,"0")}-{str(genzai.day).rjust(2,"0")} '
		  f'{str(genzai.hour).rjust(2,"0")}:{str(genzai.minute).rjust(2,"0")}:{str(genzai.second).rjust(2,"0")}')

@CLI.command()
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

@CLI.command(options_metavar='[-c / -d]')
@click.argument('files',nargs=-1,metavar='<file [file [...]]>')
@click.option('-c/-d','comp',default=True,help='Compress/decompress mode selectors.')
def hfm(files,comp):
	"""Compress or decompress FILE(S) using the Huffman compression.

	Use -c to compress and -d to decompress FILE(S).
	"""
	from _includes import huffman as hf
	for file in files:
		if not access(file,F_OK):
			print(f"'{file}' not found.")
			continue
		if comp:
			hf.compress_file(file)
			print(f"'{file}' successfully compressed.")
		else:
			hf.decompress_file(file)
			print(f"'{file}' successfully decompressed.")


if __name__=='__main__':
	CLI()