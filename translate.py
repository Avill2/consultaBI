siHashtag={}
noHashtag={}

# Funciones extractoras
def tendenciaTexto(oracion):
    if oracion.contains(' si '):
        return 1
    elif oracion.contains(' no '):
        return -1
    elif oracion.contains('si'):
        return  1
    else:
        return -1

def tendenciaHash(hashtag):
    if hashtag in siHashtag:
        return 1
    elif hashtag in noHashtag:
        return -1
    else:
        return 0

def tendenciaRetweet(retweet,tendTxt):
    if retweet ==  False:
        return 0
    elif tendTxt == 1:
        return 1
    else:
        return -1

def tendenciaFavorito(favorito,tendTxt):
    if favorito ==  False:
        return 0
    elif tendTxt == 1:
        return 1
    else:
        return -1


archivoEntrenamiento=open('entrenamiento.arff','w')
linea="\n"
tTexto=tendenciaTexto()
linea+=str(tTexto)
try:
    tHash=tendenciaHash()
    linea += ',' + str(tHash)
except:
    linea+=',0'
tRetwet=tendenciaRetweet(,tTexto)
linea+=','+str(tRetwet)
tFavorito=tendenciaFavorito(,tTexto)
linea+=','+str(tRetwet)+','+str(tTexto)