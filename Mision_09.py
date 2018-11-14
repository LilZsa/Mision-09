# Autor: Roberto Emmanuel González Muñoz
# Ejercicios con listas.


# Recibe como parámetro una lista de números enteros y regresa UNA
# NUEVA lista que contiene solo los valores pares de la lista original. La lista original no debe cambiar.
def extraerPares(listaEnteros):
    lista = []
    for k in listaEnteros:
        if (k%2) == 0:
            lista.append(k)
    return lista


# Recibe como parámetro una lista y regresa una nueva lista, con
# los valores que son mayores a un elemento previo. La lista original no debe cambiar.
def extraerMayoresPrevio(listaEnteros):
    lista = []
    numeroanterior = listaEnteros[0]
    for k in listaEnteros:
        if k > numeroanterior:
            lista.append(k)
            numeroanterior = k
        else:
            numeroanterior = k
    return lista


# Recibe una lista de valores y regresa una nueva lista con cada pareja
# de datos intercambiada. Si el número de datos es impar, el último elemento no cambia. La lista original no debe
# cambiar.
def intercamiarParejas(listaEnteros):
    lista = []
    contador = 0
    for k in range(len(listaEnteros)):
        if contador % 2 == 0:
            lista.insert(k+1, listaEnteros[k])
        else:
            lista.insert(k-1, listaEnteros[k])
        contador += 1
    return lista


# Recibe una lista de valores e intercambia el valor menor y mayor.
# Suponga que los valores mayor/menor son únicos. LA LISTA ORIGINAL DEBE MODIFICARSE.
def intercambiarMM(listaEnteros):
    menor = min(listaEnteros)
    indiceMenor = listaEnteros.index(menor)
    listaEnteros.remove(listaEnteros[indiceMenor])
    mayor = max(listaEnteros)
    indiceMayor = listaEnteros.index(mayor)
    listaEnteros.remove(listaEnteros[indiceMayor])

    listaEnteros.insert(indiceMayor, menor)
    listaEnteros.insert(indiceMenor, mayor)
    return listaEnteros



# Recibe una lista de valores enteros y regresa el promedio 'centro' de
# los valores. El promedio 'centro' se define como el promedio entero de la lista sin considerar el mayor y el menor
# de los datos. Si hay más de un mayor/menor solo se descarta uno. La lista original no debe cambiar.
def promediarCentro(listaEnteros):
    menor = min(listaEnteros)
    indiceMenor = listaEnteros.index(menor)
    listaEnteros.remove(listaEnteros[indiceMenor])
    mayor = max(listaEnteros)
    indiceMayor = listaEnteros.index(mayor)
    listaEnteros.remove(listaEnteros[indiceMayor])
    if len(listaEnteros) != 0:
        promedio = sum(listaEnteros)/len(listaEnteros)
        return int(promedio)


# Recibe una lista de números y regresa una dupla con la
# media y la desviación estándar. Tu código debe reflejar exactamente las fórmulas que se muestran a
# continuación.
def calcularEstadistica(listaEnteros):
    sumatoriaX = sum(listaEnteros)
    n = len(listaEnteros)
    mean = sumatoriaX/n

    sumatoriaCuadrada = 0
    for i in listaEnteros:
        sumatoriaCuadrada += ((i - mean)**2)

    deviation = (sumatoriaCuadrada/n-1)**.5
    return mean, "%.4f"%deviation


# Recibe como parámetro una lista y regresa la suma de los valores
# de la lista. Considere que en la suma participan todos los números, excepto los que están al lado de un número
# 13.
def calcularSuma(listaEnteros):
    pass


def imprimir(a,b,c,d,e,f,g):
    print("__________________________________________________________________________________________________________")
    print("Problema 1")
    print("Con la lista %s, regresa %s"%(g,a))
    print("__________________________________________________________________________________________________________")
    print("Problema 2")
    print("Con la lista %s, regresa %s" % (g, b))
    print("__________________________________________________________________________________________________________")
    print("Problema 3")
    print("Con la lista %s, regresa %s" % (g, c))
    print("__________________________________________________________________________________________________________")
    print("Problema 4")
    print("Con la lista %s, regresa %s" % (g, d))
    print("__________________________________________________________________________________________________________")
    print("Problema 5")
    print("Con la lista %s, regresa %s" % (g, e))
    print("__________________________________________________________________________________________________________")
    print("Problema 6")
    print("Con la lista %s, regresa %s" % (g, f))
    print("__________________________________________________________________________________________________________")


def main():
    listaEnteros = [9,2,5,4,12,7,8,11,9,3,7,4,12,5,4,10,9,6,9,4]
    sinPares = extraerPares(listaEnteros)
    sinMayoresPrevios = extraerMayoresPrevio(listaEnteros)
    interParejas = intercamiarParejas(listaEnteros)
    interMM = intercambiarMM(listaEnteros)
    promedio = promediarCentro(listaEnteros)
    estadistica = calcularEstadistica(listaEnteros)
    suma = calcularSuma(listaEnteros)
    imprimir(sinPares, sinMayoresPrevios, interParejas, interMM, promedio, estadistica, listaEnteros)


main()