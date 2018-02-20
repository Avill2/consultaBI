from textblob import TextBlob
import threading
import requests


def traducirporpartes(lim1, lim2, result):
    global oraciones

    for i in range(lim1, lim2):
        print str(i)
        #esta linea hace todoo, calcula polaridad al final
        try:
            pol = float(TextBlob(oraciones[i]).translate(from_lang="es", to='en').sentiment.polarity)
        except:
            pol = 0.99

        result.append(pol)
    return result

def startjoin_all(thread_array):
    for t in thread_array:
        t.start()
    for t in thread_array:
        t.join()



archivo=open('filtradoTweets.txt','r')
contenido=archivo.read()


oraciones=[]
oraciones=contenido.splitlines()
n = len(oraciones)
p=4
threads =[]
resultados = []
for i in range(p):
   resultados.append([]*n)

for i in range(p):
    threads.append(threading.Thread(target=traducirporpartes, args=(i*n/p, (i+1)*n/p, resultados[i])))

startjoin_all(threads)

archJSON=open('jsonquito.json','w')
archJSON.write('[')
i=0
for oracion in oraciones:
    lineaJSON = '{\"text\":\"' + oracion + '\",\"label\":"'
    neutros, positivos, negativos = 0, 0, 0

    if resultados[i] == 0.0:
        vpol = 'neutro'
        # vpol=0
        neutros += 1
    elif resultados[i] > 0.0:
        vpol = 'pos'
        # vpol=1
        positivos += 1
    else:
        vpol = 'neg'
        # vapol=-1
        negativos += 1
    lineaJSON += vpol + '\"},'
    # print lineaJSON
    if lineaJSON != '{"text":"","label":"neutro"},':
        print
        archJSON.write(lineaJSON + '\n')

archJSON.write(']')
archJSON.close()


# grafico
from pylab import *
figure(1, figsize=(8,8))
ax = axes([0, 0, 0.9, 0.9])
labels = 'positivo','negativo','neutro'
fracs = [positivos,negativos,neutros]
explode=(0.1, 0, 0)
pie(fracs, explode=explode,labels=labels, autopct='%10.0f%%', shadow=True)
legend()
title('Pie sentimiento', bbox={'facecolor':'0.8', 'pad':5})

savefig("pie.png")
show()#mostrar grafico
