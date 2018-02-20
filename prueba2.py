import json

def cargaDiccio(contenido):
    lista={}
    lineas=contenido.split('\n')
    for linea in lineas:
        linea='#'+linea
        lista[linea]=1
    return lista

def analisis(texto):
    a = texto.split(' ')
    for b in a:
        if '#' in b:
            if b.strip('\n') in dicciototal:
                if b.strip('\n') in listaSI:
                    return 1
                    break
                elif b.strip('\n') in listaNO:
                    return -1
                    break
                return 0

    return 2

def tendenciaRetweet(retweet,tendTxt):
    if retweet ==  'false':
        return 0
    else:
        return tendTxt

def tendenciaFavorito(favorito,tendTxt):
    if favorito ==  'false':
        return 0
    else:
        return tendTxt


def darCabecera():
    datos = '@relation ConsolidatedTrainData'
    datos += '\n@attribute tendhashtag numeric'
    datos += '\n@attribute retweeted numeric'
    datos += '\n@attribute favourited numeric'
    datos += '\n@attribute tendencia numeric'
    datos += '\n@data'
    return datos

listaSI={}
listaNO={}
dicciototal={}

# cargo diccionario de datos SI
archivoSI=open('dileqsi.txt','r')
contenidoSI=archivoSI.read()
listaSI=cargaDiccio(contenidoSI)
archivoSI.close()

# cargo diccionario de datos NO
archivoNO=open('dileqno.txt','r')
contenidoNO=archivoNO.read()
listaNO=cargaDiccio(contenidoNO)
archivoNO.close()

# cargo diccionario de datos Total para filtrado
archivoNeutro=open('neutros.txt','r')
contenidoNeutro=archivoNeutro.read()
dicciototal=cargaDiccio(contenidoNeutro)
archivoNeutro.close()

dicciototal.update(listaSI)
dicciototal.update(listaNO)

print 'Creando arff'
# leo JSON y genero archivo ARFF
archivoJSON=json.loads(open('archivo.json').read())

i=0
archivoArff=open('','w')
archivoArff.write(darCabecera())
for leido in archivoJSON:
    i = i + 1
    # print i

    texto=leido['text']
    a=analisis(texto)
    if a!=2:
        if a!= 0:
            valorHash = 1
        else:
            valorHash = 0
        valorRetweet = tendenciaRetweet(leido['retweeted'] ,a)
        valorFavou = tendenciaFavorito(leido['favo'] ,a)
        valorConsulta = a

        linea=str(valorHash)+','\
              +str(valorRetweet)+','\
              +str(valorFavou)+','\
              +str(valorConsulta)

