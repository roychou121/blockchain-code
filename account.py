# -*- coding: utf-8 -*-

import requests
import time
from bs4 import BeautifulSoup

print ('Taiwan local time:', time.ctime())

addr = "3EhLZarJUNSfV6TWMZY1Nh5mi3FMsdHa5U"
res1 = requests.get("https://blockchain.info/address/" + addr)
soup1=BeautifulSoup(res1.text, "html5lib")
for n1 in soup1.select("#final_balance"):
	print ('Account = ', n1.text)