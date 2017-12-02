import string
import random
import hashlib
import datetime


shahash = hashlib.sha256()

def mining():
    answer = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for x in range(30))
    shahash.update(answer.encode('utf-8'))
    solution = shahash.hexdigest()
    if solution.startswith('0'):
        endtime = datetime.datetime.now()
        print (solution)
        print ("endtime : ", endtime)
        print ("spend : ", (endtime - starttime).seconds, " sec")
        exit()

starttime = datetime.datetime.now()
print ("starttime : ", starttime)
while True:
    mining()