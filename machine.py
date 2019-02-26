import webbrowser, os, urllib
import urllib.request as webopen

class learning(object):
	def __init__(self):
		self.status = "not learning"
	def machin(self):
		connection = self.__check_connection()
		if  connection == True:
			print("Machín lernin")
			webbrowser.open('https://twitter.com/teosehacehacker/status/873161854088085506?lang=es')
		elif connection == False:
			print("Local Machín lernin")
			machin_path = os.path.abspath("machin.html")
			webbrowser.open("file://" + machin_path)

	def check_status(self):
		print(self.status)

	def __check_connection(self):
		host='http://google.com'
		try:
			webopen.urlopen(host)
			return True
		except:
			return False
