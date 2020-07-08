import click
import logging
from logging import getLogger as newlog
from os import access,F_OK
from os.path import dirname,abspath as path


logging.basicConfig(filename=f'{dirname(__file__)}/log',
					level=logging.INFO,
					format='%(asctime)s | %(levelname)s | %(name)s | %(message)s')
log=newlog('xtd')


@click.group()
def CLI():
	"""===== X10D (extend) your CMD! ====="""
	pass


@CLI.command()
def now():
	"""What's time?"""
	log.info('now')
	from datetime import datetime as dt
	genzai=dt.today()
	print(f'{genzai.year}-{str(genzai.month).rjust(2,"0")}-{str(genzai.day).rjust(2,"0")} '
		  f'{str(genzai.hour).rjust(2,"0")}:{str(genzai.minute).rjust(2,"0")}:{str(genzai.second).rjust(2,"0")}')

@CLI.command()
@click.argument('files',nargs=-1,metavar='<file [file [...]]>')
def binv(files):
	"""Invert FILE(S) bitwisely."""
	log.info(f'binv {" ".join(files)}')
	_log=newlog('xtd.binv')
	for file in files:
		if not access(file,F_OK):
			log.info(f"'{file}' not found.")
			print(f"'{file}' not found.")
			continue
		_log.info(f"Inverting '{path(file)}'...")
		with open(file,'rb') as plain:
			plainbytes=list(plain.read())
			cryptbytes=[]
			for byte in plainbytes:
				cryptbytes.append(255-int(byte))
		with open(file,'wb') as crypt:
			crypt.write(bytes(cryptbytes))
		_log.info('SUCCESSFULLY INVERTED')
		print(f"'{file}' successfully inverted.")

@CLI.command(options_metavar='[-c / -d]')
@click.argument('files',nargs=-1,metavar='<file [file [...]]>')
@click.option('-c/-d','comp',default=True,help='Compress/decompress mode selectors.')
def hfm(files,comp):
	"""Compress or decompress FILE(S) using the Huffman compression.

	Use -c to compress and -d to decompress FILE(S).
	"""
	log.info(f'hfm {"-c"*comp}{"-d"*(not comp)} {" ".join(files)}')
	# _log=newlog('xtd.hfm')
	log.info("Importing 'huffman' module...")
	try:
		from _includes import huffman as hf
	except:
		log.fatal("'huffman' module not found.")
		return
	for file in files:
		if not access(file,F_OK):
			log.info(f"'{path(file)}' not found.")
			print(f"'{file}' not found.")
			continue
		if comp:
			hf.compress_file(path(file))
			print(f"'{file}' successfully compressed.")
		else:
			hf.decompress_file(path(file))
			print(f"'{file}' successfully decompressed.")


if __name__=='__main__':
	CLI()