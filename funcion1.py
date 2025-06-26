#Creacion de una funcion de Tatiana

def Tatiana():
    # Esta funcion recibirá 5 numeros por pantalla y los ordenará de menor a mayor
    #  y luego la ordenará de mayor a menor y las imprimira ambas
    # declaro la lista que usaré
    listanum=[]
    for i in range(5):
        numero = int(input(f"Ingrese el número {i + 1}: "))
        listanum.append(numero)
    print(f"Lista de números ingresados:{listanum}")
    lista_de_menor_a_mayor=sorted(listanum)
    print(f"Lista Ordenada de menor a mayor:{lista_de_menor_a_mayor}")
    lista_de_mayor_a_menor=sorted(listanum,reverse=True)
    print(f"Lista Ordenada de mayor a menor :{lista_de_mayor_a_menor}")

Tatiana()

