#Filename : User.py
import hashlib
import cPickle

class User:
	fileName = ".data"
	strIOError = "No such data file exists"
	strInputName = "Please input your name : "
	strInputPassword = "Please input your password : "
	def __init__(self,name='',password=''):
		if name == '' and password == '':
			try:
				file = open(User.fileName)
				self.user_name,self.user_password = cPickle.load(file)
				file.close()
			except IOError:
				print User.strIOError
				self.u_getNameAndPassword()
		else:
			self.user_name = name
			self.user_password = hashlib.md5(password).hexdigest()
		
	def u_setUserName(self,newName):
		self.user_name = newName
		
	def u_setPassword(self,newPassword):
		self.user_password = newPassword
		
	def u_getNameAndPassword(self):
		#get user name from the input
		self.user_name = str(raw_input(User.strInputName))
		self.user_password = hashlib.md5(str(raw_input(User.strInputPassword))).hexdigest()
		
	def u_saveNameAndPassword(self):
		try:
			file = open(User.fileName,"w") 
			cPickle.dump((self.user_name, self.user_password),file)
			file.close()
		except IOError,x:
			print x
