import requests
import re

class Header():
	G = '\033[92m'  # green
	Y = '\033[93m'  # yellow
	B = '\033[94m'  # blue
	R = '\033[91m'  # red
	W = '\033[0m'   # white
	P = '\033[95m'  # purple

	def __init__(self):
		self.banner()

	def banner(self):
		print '''
        %s
            dP                           dP                       dP dP      
            88                           88                       88 88       
   .d8888b. 88d888b. .d8888b. .d8888b. d8888P dP  dP  dP .d8888b. 88 88  .dP  
   88'  `88 88'  `88 88'  `88 Y8ooooo.   88   88  88  88 88'  `88 88 88888"   
   88.  .88 88    88 88.  .88       88   88   88.88b.88' 88.  .88 88 88  `8b. 
   `8888P88 dP    dP `88888P' `88888P'   dP   8888P Y8P  `88888P8 dP dP   `YP 
        .88                                                           
    d8888P                                                            
          %s                                                                  
	'''%(self.P,self.W)

class DNSDumpster():

	def __init__(self,url):
		self.url = url
		x = self.goDNSDumpster(self.url)
		self.extractDNSDumpster(x)

	def goDNSDumpster(self,domain):
		durl = 'https://dnsdumpster.com'
		with requests.Session() as s:
			client = s.get(durl)
			csrftoken = client.cookies['csrftoken']
			param = {'csrfmiddlewaretoken':csrftoken,'targetip':domain}
			client = s.post(durl,data=param,headers={'Referer':durl})
			data = client.text
		return data

	def extractDNSDumpster(self,raw):
		links_regex = re.compile('<a name="hostanchor"><\/a>Host Records.*?<table.*?>(.*?)</table>', re.S)
		url_regex = re.compile('<tr><td class="col-md-4">(.*?)<br>',re.S)
		links = links_regex.findall(raw)[0]
		eurl = url_regex.findall(links)
		for url in eurl: print url

h = Header()
d = DNSDumpster("google.com")