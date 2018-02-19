# -*- coding: utf-8 -*-
__author__ = 'elikary'

'''
 QUITO
==============
'''
import couchdb
import sys
import urllib2
import json
import re

URL = 'localhost'
#db_name = 'tweetsuio'
db_name = 'twitterny'


'''========couchdb'=========='''
server = couchdb.Server('http://'+URL+':5984/')  #('http://245.106.43.184:5984/') poner la url de su base de datos
try:
    print db_name
    db = server[db_name]
    print 'success'

except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()



#url = 'http://127.0.0.1:5984/tweetsuio/_design/tweets/_view/user_tweets'
url = 'http://localhost:5984/twitterny/_design/Bi/_view/vistaNY'
req = urllib2.Request(url)
f = urllib2.urlopen(req)
d = json.loads(f.read())# esta variable manaje contenido

#print (d)
archivo=open('tweetsNY.txt','w')

for x in d['rows']:
    a = x['value']['text']
    # archivo.write(str(a)) # pasa contenido base a .txt
    total = ''
    for letra in a:
        if re.match('([A-Za-z0-9\s])',letra):
            total+= letra

    total += '\n'

    archivo.write(total)
    print total
#for x in f:
#    print(x)
#f.close()
