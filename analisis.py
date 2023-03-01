import statistics
import matplotlib.pyplot as plt
def graficar(lista):

    listaCantidades=[]
    listaPromedios=[]
    for i in lista:
        listaCantidades.append(i[0])
        listaPromedios.append(i[1])


    fig, ax = plt.subplots()
    ax.scatter(listaCantidades,listaPromedios)
    plt.show()
