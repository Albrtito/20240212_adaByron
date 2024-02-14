
# Segunda Versión
# Tablero nxn y grafos basados en diccionarios
# Vértices: v = Tupla (x,y), 0 <= x,y < n
# Aristas: dict[v] = (x,y,z), donde v, x, y, z son vértices
# Búsqueda en profundidad (Queremos encontrar un cámino)
#      En n muy elevados el factor de ramificación puede llegar a ser 8 (demasiado eleveado para amplitud)
# Profundidad máxima -> n (El camino tiene que tener n casillas, ni más ni menos)

import time
import sys

#sys.setrecursionlimit(16000) # Hay que modificar el límite de recursion para N mayores que 20 mas o menos
N = 2 # Constante N, que define el tamaño del tablero nxn 

# Funcion que sirve para establecer los valores iniciales para luego usar la busqueda
def busqueda_profundidad(grafo: dict) -> list:
    # Como no se si el camino se puede lograr desde todos las casillas iniciales, voy a ir iterando hasta que se encuentre 
    for x in range(N):
        for y in range(N):
            # Vamos probando con todos los nodos iniciales
            nodo_inicial = (x,y)
            # Y llamamos a la funcion recursiva hasta que lo encontremos
            camino_solucion = _busqueda_profundidad(grafo, nodo_inicial, [], N*N, N*N)
            if len(camino_solucion) == N*N:
                return camino_solucion
    # Si el camino no existiera (en un 2x2 por ejemplo), devolvemos la lista vacia
    return []

# Funcion de búsqueda recursiva
def _busqueda_profundidad(grafo: dict, nodo: tuple, lista_camino: list, longitud: int, prof: int):
    # En este caso no haría falta comprobar la profundidad (Nunca va a ser mayor que NxN), pero por si acaso
    if prof <= 0:
        return []
    # Si el camino es tan largo como la longitud que le marcaramos (NxN), entonces hemos encontrado el camino
    if len(lista_camino) == longitud:
        return lista_camino
    # Si aun no hemos encontrado el camino, añadimos el nodo a la lista y probamos con sus sucesores
    lista_camino.append(nodo)
    
    for adyacente in grafo[nodo]:
        # No hace falta tener una lista de visitados porque los nodos visitados ya están en el camino
        if adyacente not in lista_camino:
             # Volvemos a llamar a la función con profundidad -1 y un nodo adyadcente
            _busqueda_profundidad(grafo, adyacente, lista_camino, longitud, prof-1) 
    # Si llegamos a un nodo que no tiene adyacentes válidos, devolvemos el camino que tenga hasta entonces
    return lista_camino

def main():
    # Creamos el diccionario con los vértices unicamente
    grafo = dict()
    for x in range(N):
        for y in range(N):
            grafo[(x,y)] = []

    # Añadimos las aristas
    # Este paso se puede hacer con la creación de vértices, pero así queda más ordenado
    for vertice in grafo:
        for dx in range(-2, 3):
            for dy in range(-2,3):
                if abs(dx) + abs(dy) == 3:
                    pos_salto = (vertice[0] + dx, vertice[1] + dy)
                    if 0 <= pos_salto[0] < N and 0 <= pos_salto[1] < N:
                        grafo[vertice].append(pos_salto)

    camino_solucion = busqueda_profundidad(grafo)
    if len(camino_solucion) == N*N:
        print(len(camino_solucion))
        print(camino_solucion)
    
        # Comprobacion de que el camino es correcto (que se pasa por todas las casillas)
        # Eliminar para aumentar la velocidad. Esto es solo para pruebas
        for x in range(N):
            for y in range(N):
                if (x,y) not in camino_solucion:
                    print("Error en el camino")
                    print((x,y))
    else:
        print("Camino no encontrado con N=", N)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
