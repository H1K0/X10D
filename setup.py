try:
	import PyInstaller.__main__ as build
except:
	print("PyInstaller is not installed. Let's install it using 'pip install pyinstaller' and run me again!")
	exit()
from os.path import dirname,join
from os import system
import winreg


def add_to_path(path, root=winreg.HKEY_CURRENT_USER, key_path='Environment', access=winreg.KEY_ALL_ACCESS):
    root_key = winreg.ConnectRegistry(None, root)
    key = winreg.OpenKey(root_key, key_path, 0, access)
    value, value_type = winreg.QueryValueEx(key, 'path')
    value = value.rstrip(';') + ';' + path
    winreg.SetValueEx(key, 'path', 0, value_type, value)
    winreg.CloseKey(key)
    winreg.CloseKey(root_key)


with open('_includes/config.py','w',encoding='utf-8') as config:
	config.write(f'''
path=r'{dirname(__file__)}'
''')

build.run([
    '--onefile',
    '--distpath=.',
    '--icon=icon.ico',
    'xtd.py'
])

add_to_path(dirname(__file__))

system('pause')