# -*- coding: utf-8 -*-
from bitcoin import *
import time

print ('Taiwan local time:', time.ctime())

password = "Enter your password !"

priv = sha256(password)
print ("priv : ", priv)

pub = privtopub(priv)
print ("pub : ", pub)

addr = pubtoaddr(pub)
print ("addr : ", addr)