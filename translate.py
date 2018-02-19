siHashtag={}
noHashtag={}

# Funciones extractoras
def tendenciaTexto(oracion):
    if ' si ' in oracion:
        return 1
    elif ' no ' in oracion:
        return -1
    elif 'si' in oracion:
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


def crearlineaARF(texto,hashtag,retweeted,favourited):

    linea = "\n"
    tTexto = tendenciaTexto(texto)
    linea += str(tTexto)
    try:
        tHash = tendenciaHash(hashtag)
        linea += ',' + str(tHash)
    except:
        linea += ',0'
    tRetwet = tendenciaRetweet(retweeted, tTexto)
    linea += ',' + str(tRetwet)
    tFavorito = tendenciaFavorito(favourited, tTexto)
    linea += ',' + str(tRetwet) + ',' + str(tTexto)

    return linea