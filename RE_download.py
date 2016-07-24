#  Decription:   
#       A Python script used to download the txts from Internet.  
#  Author:  
#       kuritan  
#  Date:  
#       2016-07-24 11:34:00  
#  
import urllib
import urllib2
import re

episode_true = int(raw_input("From 1st to what episode do you want? "))

#episode_temp = range(1, episode_true+1)

def download():
	"""This function will download txt."""
	local_dir = "/Volumes/Macintosh HD2/PythonData/test/"
	url_list = []
	for eachURL in range(1, episode_true+1):
		eachURL_str = str(eachURL)
		url_true = BASE_URL + eachURL_str + TXT_FORMAT
		url_list.append(url_true)
		for everyURL in url_list:
#			wordItems = everyURL
#			for item in wordItems:
#				if re.match('.*\.txt$', item):
#					TXTName = item
			txtname = eachURL_str + ".txt"
			local_txt = local_dir + txtname
			try:
				urllib.urlretrieve(everyURL, local_txt)
			except Exception, e:
				continue

#add URL
BASE_URL = "http://ncode.syosetu.com/txtdownload/dlstart/ncode/302237/?no="  
TXT_FORMAT="&hankaku=0&code=utf-8&kaigyo=CRLF.txt"  
  
#print var on screen   
print "Beginning TXT download..."  
print '..' * 10  

download()