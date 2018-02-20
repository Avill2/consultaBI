import json

def cargaDiccio(contenido):
    lista={}
    lineas=contenido.split('\n')
    for linea in lineas:
        linea='#'+linea
        lista[linea]=1
    return lista

def contieneConsulta(text):
    if 'consulta' in text.lower():
        return 1
    else:
        return 0

def analisis(text):
    a = text.split(' ')
    for b in a:
        if '#' in b:
            if b.strip('\n') in dicciototal:
                if b.strip('\n') in listaSI:
                    return 1

                elif b.strip('\n') in listaNO:
                    return -1

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

def contieneSI(text):
    if 'SI' in text:
        return 1
    elif 'Si ' in text:
        return 0.6
    elif 'si ' in text:
        return 0.3
    else:
        return 0

def contieneNO(text):
    if 'NO' in text:
        return 1
    elif 'No ' in text:
        return 0.6
    elif 'no' in text:
        return 0.3
    else:
        return 0


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
#archivoJSON=json.loads(open('viewCuencaT.json').read())
#archivoJSON=json.loads(open('viewQuitoT.json').read())
#archivoJSON=json.loads(open('viewGuayaquilT.json').read())
archivoJSON=json.loads(open('viewTodoT.json').read())
i=0
#archivoArff=open('dataCuenca.arff','w')
#archivoArff=open('dataQuito.arff','w')
#archivoArff=open('dataGuayaquil.arff','w')
archivoArff=open('dataTodo.arff','w')
archivoArff.write(darCabecera())
for leido in archivoJSON:
    i = i + 1
    print i

    texto = repr(leido['value'])
    a = analisis(texto)
    if a != 2:

        if a != 0:
            valorConsulta = 1
        else:
            valorConsulta = a

        valorRetweet = contieneSI(texto)
        valorFavou = contieneNO(texto)
        valorHash = a
        valorTieneConsult=contieneConsulta(texto)

        linea = '\n'+repr(valorHash) + ',' \
                + repr(valorRetweet) + ',' \
                + repr(valorFavou) + ',' \
                + repr(valorTieneConsult)+','\
                +repr(valorConsulta)

        print linea
        archivoArff.write(linea)
print 'FIN'