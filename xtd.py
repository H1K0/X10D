import click
import _includes.config as config
from _includes.logger import Log
from os import access,F_OK
from os.path import dirname,join,abspath as path


log=Log(join(config.path,'log'),'xtd')


@click.group()
def CLI():
	"""===== X10D (extend) your CMD! ====="""
	pass


@CLI.command()
def now():
	"""What's time?"""
	log.log('now')
	from datetime import datetime as dt
	genzai=dt.today()
	print(f'{genzai.year}-{str(genzai.month).rjust(2,"0")}-{str(genzai.day).rjust(2,"0")} '
		  f'{str(genzai.hour).rjust(2,"0")}:{str(genzai.minute).rjust(2,"0")}:{str(genzai.second).rjust(2,"0")}')

@CLI.command()
@click.argument('files',nargs=-1,metavar='<file [file [...]]>')
def binv(files):
	"""Invert FILE(S) bitwisely."""
	log.log(f'binv {" ".join(files)}')
	for file in files:
		if not access(file,F_OK):
			log.log(f"'{file}' not found.")
			print(f"'{file}' not found.")
			continue
		log.log(f"Inverting '{path(file)}'...",'xtd.binv')
		with open(file,'rb') as plain:
			plainbytes=list(plain.read())
			cryptbytes=[]
			for byte in plainbytes:
				cryptbytes.append(255-int(byte))
		with open(file,'wb') as crypt:
			crypt.write(bytes(cryptbytes))
		log.log('SUCCESSFULLY INVERTED','xtd.binv')
		print(f"'{file}' successfully inverted.")

@CLI.command(options_metavar='[-c / -d]')
@click.argument('files',nargs=-1,metavar='<file [file [...]]>')
@click.option('-c/-d','comp',default=True,help='Compress/decompress mode selectors.')
def hfm(files,comp):
	"""Compress or decompress FILE(S) using the Huffman compression.

	Use -c to compress and -d to decompress FILE(S).
	"""
	log.log(f'hfm {"-c"*comp}{"-d"*(not comp)} {" ".join(files)}')
	log.log("Importing 'huffman' module...")
	try:
		from _includes.huffman import compress_file,decompress_file
	except:
		log.log("'huffman' module not found.")
		return
	for file in files:
		if not access(file,F_OK):
			log.log(f"'{path(file)}' not found.")
			print(f"'{file}' not found.")
			continue
		if comp:
			compress_file(path(file))
			print(f"'{file}' successfully compressed.")
		else:
			decompress_file(path(file))
			print(f"'{file}' successfully decompressed.")


if __name__=='__main__':
	CLI()