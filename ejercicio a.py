import simpy
import random
import statistics
import procesos
import matplotlib.pyplot as plt
import analisis
env = simpy.Environment()
#Se inicializa la ram con n espacios, inicialmente son 100
ram = simpy.Container(env, capacity=100, init=0)

tiempos = []

##################################
#           Procesador 1         #
##################################
def llegada(env, contenedor, tiempos):
    while True:
        #Intervalo
        yield env.timeout(9) 
        if contenedor.level < contenedor.capacity:
            contenedor.put(procesos.proceso())
            print(f'Memoria llenada en {env.now} con {contenedor.level} memoria.')
            tiempo = env.now - start_time
            tiempos.append(tiempo)

def salida(env, container):
    while True:
        #Intervalo
        yield env.timeout(9)  
        if container.level > 0:
            container.get(procesos.proceso())
            print(f'Memoria vaciada en {env.now} con {container.level} espacios restantes.')

##################################
#           Procesador 2         #
##################################
def llegada2(env, contenedor, tiempos):
    while True:
        #Intervalo
        yield env.timeout(9) 
        if contenedor.level < contenedor.capacity:
            contenedor.put(procesos.proceso())
            print(f'Memoria llenada en {env.now} con {contenedor.level} memoria.')
            tiempo = env.now - start_time
            tiempos.append(tiempo)

def salida2(env, container):
    while True:
        #Intervalo
        yield env.timeout(9)  
        if container.level > 0:
            container.get(procesos.proceso())
            print(f'Memoria vaciada en {env.now} con {container.level} espacios restantes.')
listaGraficar=[]

for cantidad in [25, 50, 100, 150, 200]:
    #Reseteo del entorno de simulacion
    env = simpy.Environment()
    ram = simpy.Container(env, capacity=100, init=0)
    tiempos = []
    
    for i in range(cantidad):
        start_time = env.now
        #Si el proceso es impar se va al procesador 1
        if i%2!=0:
            env.process(llegada(env, ram, tiempos))
            env.process(salida(env, ram))
        #Si el proceso es par se va al procesador 2
        else:
            env.process(llegada2(env, ram, tiempos))
            env.process(salida2(env, ram))
    
    env.run(until=100)
    # Seccion estadistica
    promedio = statistics.mean(tiempos)
    desviacion = statistics.stdev(tiempos)
    
    print(f'Con {cantidad} procesos:')
    print(f'Promedio de tiempo de espera: {promedio:.2f}')
    print(f'Desviación estándar del tiempo de espera: {desviacion:.2f}')
    
    #Grafica
    
    l=[]
    l=[cantidad,promedio]
    listaGraficar.append(l)

print(listaGraficar)
analisis.graficar(listaGraficar)