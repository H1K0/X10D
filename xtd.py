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
@click.option('-c/-d','comp',required=True,default=True)
def hfm(files,comp):
	"""Compress or decompress FILE(S) using the Huffman compression.

	Use -c to compress and -d to decompress FILE(S).

	"""
	from _includes import huffman as hfm
	for file in files:
		if not access(file,F_OK):
			print(f"'{file}' not found.")
			continue
		if comp:
			hfm.compress_file(file)
			print(f"'{file}' successfully compressed.")
		else:
			table=file+'.tbl'
			if not access(table,F_OK):
				table=input(f"Table file '{file}.tbl' was not found.")
				continue
			hfm.decompress_file(file)
			print(f"'{file}' successfully decompressed.")

'''
@CLI.command()
@click.argument('files',nargs=-1,metavar='<file [file [...]]>')
def md(files):
	pass
'''


if __name__=='__main__':
	CLI()