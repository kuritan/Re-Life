#  Decription:   
#       A Python script used to download the txts from Internet.  
#  Author:  
#       kuritan  
#  Date:  
#       2016-07-24 11:34:00  
#  
import urllib

# import the episode No.
episode_true = int(raw_input("From 1st to what episode do you want? "))

def download():
	"""This function will download txt."""
	# set the download file's localpath
	local_dir = "/Volumes/Macintosh HD2/PythonData/test/"
	# creat a list to contain the URL
	url_list = []
	# make a loop and split the URL
	for eachURL in range(1, episode_true+1):
		eachURL_str = str(eachURL)
		url_true = BASE_URL + eachURL_str + TXT_FORMAT
		url_list.append(url_true)
		# split the localpath and txt name
		for everyURL in url_list:
			global txtname
			txtname = eachURL_str + ".txt"
			local_txt = local_dir + txtname
			# download begin
			try:
				urllib.urlretrieve(everyURL, local_txt, Schedule)
			except Exception, e:
				continue

# set reporthook function
def Schedule(a,b,c):
	'''''
	a:data's size that already download
	b:data's size
	c:remote file size
	'''''
	per = 100.0 * a * b / c
	if per > 100 :
		per = 100
	print "Downloading %s: %.2f%%" % (txtname, per)

# set the base URL and the URL's end
BASE_URL = "http://ncode.syosetu.com/txtdownload/dlstart/ncode/302237/?no="  
TXT_FORMAT = "&hankaku=0&code=utf-8&kaigyo=CRLF.txt"  
  
# print var on screen   
print "Beginning TXT download..."  
print '..' * 10  

# run the download function
download()