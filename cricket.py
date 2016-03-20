import subprocess as notify
import time
import urllib.request

while True:
	url = "http://scores.sify.com/"

	handle = urllib.request.urlopen(url)

	content = str(handle.read())

	start = content.find("<title>") + 7

	end = content.find("</title>")

	start1 = content.find("<h3>") + 4

	end1 = content.find("</h3>")

	start1 = content.find("<h3>", start1 + 1) + 4

	end1 = content.find("</h3>", end1 + 1)

	scores = content[start:end] + "\n" + content[start1:end1]
	
	notify.call(['notify-send', "Cricket Alerts", scores, '--icon=None', '--expire-time=20000'])
	
	time.sleep(120)