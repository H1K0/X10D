from datetime import datetime as dt

class Log:
	def __init__(self,path,name):
		self.path=path
		self.name=name

	def log(self,msg,name=None):
		if name is None:
			name=self.name
		now=dt.today()
		with open(self.path,'a',encoding='utf-8') as file:
			file.write(f'{now.year}-{str(now.month).rjust(2,"0")}-{str(now.day).rjust(2,"0")} '
							f'{str(now.hour).rjust(2,"0")}:{str(now.minute).rjust(2,"0")}:{str(now.second).rjust(2,"0")},{str(now.microsecond)[:3]}'
							' | '
							f'{name}'
							' | '
							f'{msg}\n')