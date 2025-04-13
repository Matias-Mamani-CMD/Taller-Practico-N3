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

def calcular_potencia(K, X):
    for i in range(X):
        potencia = K * K
    print(f"La potencia de {K} es {potencia}")

def cantidad_digitos(K):
    n_digitos = len(str(K))
    print(f"Cantidad de dígitos de {K}: {n_digitos}")

def es_capicua(K):
    n_original = K
    invertido = 0

    while K > 0:
        dig = K % 10
        invertido = invertido * 10 + dig
        K //= 10

    if n_original == invertido:
        print(f"{n_original} es un número capicúa.")
    else:
        print(f"{n_original} no es un número capicúa.")

def ejercicio5():
    print("1 - Calcular la potencia")
    print("2 - Obtener cantidad de dígitos")
    print("3 - Determinar si es capicúa")

    op = int(input("Ingrese una opción del menú: "))
    
    if op == 1:
        K = int(input("Ingrese un número: "))
        X = int(input("Ingrese otro número (potencia): "))
        calcular_potencia(K, X)

    elif op == 2:
        K = int(input("Ingrese un número: "))
        cantidad_digitos(K)

    elif op == 3:
        K = int(input("Ingrese un número: "))
        es_capicua(K)

def mostrar_matriz(Matriz):
    print("Vector resultante")
    for fila in Matriz:
        print(fila)

def suma_matriz(MatrizA, MatrizB):
    filas = len(MatrizA)
    columnas = len(MatrizA[0])
    MatrizC = []
    
    for i in range(filas):
        fila_suma = []
        for j in range(columnas):
            numero_suma = MatrizA[i][j] + MatrizB[i][j]
            fila_suma.append(numero_suma)
        MatrizC.append(fila_suma)
    return MatrizC
    
def producto_matriz(MatrizA, MatrizB):
    filas = len(MatrizA)
    columnas = len(MatrizA[0])
    MatrizC = []
    
    for i in range(filas):
        fila_suma = []
        for j in range(columnas):
            numero_suma = MatrizA[i][j] * MatrizB[i][j]
            fila_suma.append(numero_suma)
        MatrizC.append(fila_suma)
    return MatrizC
    
def cargar_matriz_A(A, B):
    matriz_A = []
    for i in range(A):
        fila = []
        for j in range(B):
            numero = random.randint(1,100)
            fila.append(numero)
        matriz_A.append(fila)
    
    print("Matriz A:")
    for fila in matriz_A:
        print(fila)    
    print("///////////")
    return matriz_A

def cargar_matriz_B(C,D):
    matriz_B = []
    for i in range(C):
        fila = []
        for j in range(D):
            numero = random.randint(1,100)
            fila.append(numero)
        matriz_B.append(fila)
    
    print("Matriz B:")
    for fila in matriz_B:
        print(fila)
    print("///////////")
    return matriz_B

def ejercicio6():
    M = random.randint(1,9)
    N = random.randint(1,9)
    MatrizA = cargar_matriz_A(M,N)
    MatrizB = cargar_matriz_B(M,N)
    print("¿Qué operación desea realizar?")
    print("1.Suma Matrices")
    print("2.Producto Matrices")
    opcion = int(input("Ingrese una opción: "))
    if opcion in [1,2]:
        if opcion == 1:
         MatrizC = suma_matriz(MatrizA, MatrizB)
         mostrar_matriz(MatrizC)
        else:
         MatrizD = producto_matriz(MatrizA, MatrizB)
         mostrar_matriz(MatrizD)
    else:
     print("Opción invalida")

def suma_diagonal_principal(matriz):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][i]
    return suma

def ejercicio7():
    M = random.randint(1,9)
    matriz = cargar_matriz_A(M)
    suma_diagonal = suma_diagonal_principal(matriz)
    print(f"Matriz {M}x{M}")
    for fila in matriz:
        print(fila)
    print(f"La suma de la diagonal principal es: {suma_diagonal}")

def convertir_int_a_str(matriz):
    for fila in matriz: 
        fila[2] = str(fila[2])
        fila[3] = str(fila[3])
    return

def seleccion_usuarios_proveedores(matriz):
    seleccion_proveedor = input("Seleccione un proveedor para visualizar sus productos:\n ").strip().lower()
    for fila in matriz:
        if seleccion_proveedor in fila[1].strip().lower():
            print(f"Productos del proveedor {fila[1]}: {fila[0]}")
               
def electrodomestico_menor_precio(matriz):
    menor = int(matriz[0][2])
    producto_menor = matriz[0][0]
    for fila in matriz:
       if int(fila[2]) <= menor:
            menor = int(fila[2])
            producto_menor = fila[0]
    print(f"El electrodoméstico más barato es {producto_menor}:\n Precio: {menor}")           
        
def mostrar_stock_positivo(matriz):
    electrodomestico_stock_positivo = []
    for fila in matriz:
       if int(fila[3]) > 0:
           electrodomestico_stock_positivo.append((fila[0],fila[3]))
    for fila in electrodomestico_stock_positivo:
        print(f"Productos con stock positivo:{fila}")               
        
def ejercicio8():
    matriz = [
       ["Licuadora", "Philips", 150,0],
       ["Plancha", "Atma", 160, 2],
       ["Equipo Música", "Sony", 850, 3],
       ["Heladera", "Dream", 1000, 2],
       ["Lavarropas", "Dream", 1500, 2],
       ["Televisor","Philips", 700, 0],
       ["DVD", "Sony", 250, 1],
       ["Microondas", "Dream",300,0] 
    ]
    convertir_int_a_str(matriz)
    seleccion_usuarios_proveedores(matriz)
    electrodomestico_menor_precio(matriz)
    mostrar_stock_positivo(matriz)

def rotar_vector(vector, posiciones):
    for _ in range(posiciones):
        primero = vector.pop(0)
        vector.append(primero)
    return vector

def ejercicio10():
    rodillo1 = ["X", "O", "7", "X", "O", "7", "X", "O", "7"]
    rodillo2 = ["O", "7", "X", "O","7", "X", "O", "7", "X"]
    rodillo3 = ["7", "X", "O", "7", "X", "O", "7", "X", "O"]

    while True:
        print("Jugada")
        giro1 = random.randint(0, 9)
        giro2 = random.randint(0, 9)
        giro3 = random.randint(0, 9)

        rodillo1_rotado = rotar_vector(rodillo1.copy(), giro1 % 9)
        rodillo2_rotado = rotar_vector(rodillo2.copy(), giro2 % 9)
        rodillo3_rotado = rotar_vector(rodillo3.copy(), giro3 % 9)

        print(f"Rodillos:")
        print(f"[{rodillo1_rotado[0]}] [{rodillo2_rotado[0]}] [{rodillo3_rotado[0]}]")

        combinacion = rodillo1_rotado[0] + rodillo2_rotado[0] + rodillo3_rotado[0]
        if combinacion == "XXX":
            print("Ganó 10 fichas")
        elif combinacion == "OOO":
            print("Gano 100 fichas")
        elif combinacion == "777":
            print("Ganó 1000 fichas")
        else:
            print("Vuelve a intentarlo!")

        seguir_jugando = input("¿Desea jugar otra vez? (s/n): ").lower()
        if seguir_jugando != 's':
            break

def menu():
    ejercicio1()
    ejercicio2()
    ejercicio3()
    ejercicio4()
    ejercicio5()
    ejercicio6()
    ejercicio7()
if __name__ == '__main__':
    menu()