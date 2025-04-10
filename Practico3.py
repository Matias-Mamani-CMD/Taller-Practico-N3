import random

def ingreso_numeros(lista):
    numero = int(input("Ingrese un número: "))
    lista.append(numero)
    
def mostrar_maximo(lista):
    print(f"El número máximo es: {max(lista)}")

def ejercicio1():
    # Para realizar el ejercicio se utilizó unicamente procedimientos
    lista = []
    for _ in range(3):
        ingreso_numeros(lista)
    mostrar_maximo(lista)

def ejercicio2():
    lista = []
    for _ in range (10):
        ingreso_numeros(lista)
    mostrar_maximo(lista)

def suma_vectores(Vector_A, Vector_B):
    vector_resultante = []
    for i in range (len(Vector_A)):    
        vector_resultante.append(Vector_A[i]+Vector_B[i])
    print(f"Vector resultante: {vector_resultante}")
    
def mostrar_vector(Vector):
    print(f"Vector: {Vector}")

def cargar_vector(C, Vector):
    for _ in range(C):
        numero = random.randint(1,99)
        Vector.append(numero)
    
def longitud_vector(nombre_vector):
    return int(input(f"Ingrese la longitud del vector {nombre_vector}: \n"))    

def ejercicio3():
    Vector_A = []
    Vector_B = []
    N = longitud_vector("A")
    M = longitud_vector("B")
    cargar_vector(N, Vector_A)
    cargar_vector(M, Vector_B)
    mostrar_vector(Vector_A)
    mostrar_vector(Vector_B)
    if N == M:
        suma_vectores(Vector_A, Vector_B)
    else:
        print("N y M no son iguales")
    
def contar_vocales(oracion):
    cont_voc = 0
    for letra in oracion.lower():
        if letra in ('a','e','i','o','u','á', 'é', 'í', 'ó', 'ú'):
            cont_voc += 1
    return cont_voc
def contar_consonantes(oracion):
    cont_cons = 0
    for letra in oracion.lower():
        if letra.isalpha() and letra not in ('a','e','i','o','u','á', 'é', 'í', 'ó', 'ú'):
            cont_cons += 1
    return cont_cons

def ingreso_oraciones(oraciones):
    while True:
        oracion = input("Ingrese una oración: ")
        oraciones.append(oracion)
        print("S/N") 
        op = input("¿DESEA INGRESAR OTRA ORACIÓN? ").upper()
        if op != 'S':
            break
                      
def ejercicio4():
    oraciones = []
    ingreso_oraciones(oraciones)
    for oracion in oraciones:
        print(f"Vocales en la oración: {contar_vocales(oracion)}\n Consonantes en la oración: {contar_consonantes(oracion)}")

def menu():
    ejercicio1()
    ejercicio2()
    ejercicio3()
    ejercicio4()
if __name__ == '__main__':
    menu()  