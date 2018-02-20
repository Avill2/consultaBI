import json

print "Leer archivos"
leer = json.loads(open('viltrada.json').read())
#print leer

print "Imprimir elemento isActive"

i=0
for leido in leer:
    print leido['value']['hashtags']
    print i
    i+=1