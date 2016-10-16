# developed by petrk94
import urllib.request
import urllib
import os
from bs4 import BeautifulSoup


# Read the html content of the URL into the variable "soup"
soup = BeautifulSoup(urllib.request.urlopen("https://status.bytespeicher.org/"), "html.parser")

# Looking up for the title which is in the HTML content related to the information we want to read out and than write the html code into "result"
raw = soup.find_all("div", {"class":"grid_9"})


# read the result and strip the white spaces and the html code to get the text 
for result in raw:
     print(result.get_text().strip())
print()
	 

# stop the program, comandline window will not close after execution
os.system("pause")

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#strings-and-stripped-strings

# http://stackoverflow.com/questions/20889790/get-text-of-childrens-in-a-div-with-beautifulsoup

#EOF
