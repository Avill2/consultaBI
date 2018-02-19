# -*- coding: utf-8 -*-
import words as words

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
db_name = 'bdcuenca1'


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
url = 'http://localhost:5984/bdcuenca1/_design/vistacuencapais/_view/cuencapais'
req = urllib2.Request(url)
f = urllib2.urlopen(req)
d = json.loads(f.read())# esta variable manaje contenido

#print (d)
#archivo=open('archivo.txt','w')

text=''
#hashtags=''
retweeted=''
favorited=''
cont=0
for x in d['rows']:
    text=x['key']['text']
    hashtags=x['key']['entities']['hashtags']
    retweeted=x['key']['retweeted']
    favorited=x['key']['favorited']
    if len(hashtags) > 0:

        print "Texto",text,"Hashtag",hashtags,"rete",retweeted,"favorito",favorited
        print  hashtags
        cont+=1
        print cont

    #print total
#for x in f:
#    print(x)
#f.close()
