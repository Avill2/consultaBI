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
db_name = 'dbcuenca1'


'''========couchdb'=========='''
server = couchdb.Server('http://localhost:5984/')  #('http://245.106.43.184:5984/') poner la url de su base de datos
try:
    print db_name
    db = server[db_name]
    print 'success'

except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()



#url = 'http://127.0.0.1:5984/tweetsuio/_design/tweets/_view/user_tweets'
url = 'http://localhost:5984/dbcuenca1/_design/vistacuencapais/_view/cuencapais'
req = urllib2.Request(url)
f = urllib2.urlopen(req)
d = json.loads(f.read())# esta variable manaje contenido

#print (d)
#archivo=open('archivo.txt','w')

diccioHash={}

for x in d['rows']:
    words=x['key'].split(' ')

    for word in words:
        if '#' in word:
            if '7' in word:
                word = word.strip('\n').strip('#').lower()
                diccioHash[word] = 1
            if 'Si'in word:
                word = word.strip('\n').strip('#').lower()
                diccioHash[word] = 1
            if 'vota'in word:
                word = word.strip('\n').strip('#').lower()
                diccioHash[word] = 1
            if 'consulta' in word:
                word = word.strip('\n').strip('#').lower()
                diccioHash[word] = 1

for x in diccioHash:
    print x

