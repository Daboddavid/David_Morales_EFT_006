peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],
}


cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3],
}


def cupos_genero(genero):
    total=0
    for key, value in peliculas.items():
        if peliculas[key][1].lower()==genero.lower():
            if cartelera[key][1]!=0:
                total=total+cartelera[key][1]
    print(f"El total de cupos disponibles es: {total} en peliculas de {genero}")
                

def mostrarpel():
    for key,value in peliculas:
        print(key,value[0])



def eliminar_pelicula(codigo):
    if codigo in peliculas:
        peliculas.pop(codigo)
        cartelera.pop(codigo)
        return True
    else:
        return False
    



def busqueda_precio(p_min,p_max):
    listapr=[]
    for key,value in peliculas.items():
        if cartelera[key][1]!=0:
            if p_min<=cartelera[key][0]<=p_max:
                listapr.append(f"{value[0]} -- {key}")
    print(listapr)


def actualizar_precio(codigo,nuevo_precio):
    if codigo in cartelera:
        cartelera[codigo]=nuevo_precio
        return True
    else:
        return False

def codigon(codigo):
    if codigo not in peliculas:
        return True
    else:
        return False
def duracionn(duracion):
    if duracion>0:
        return True
    else:
        return False
def clasificacionn(clasificacion):
    if clasificacion is "A" or "B" or "C":
        return True
    else:
        return False

def es_3dd(es_3d):
    if es_3d is "s":
        return True
    else:
        return False

def precioo(precio):
    if precio>0:
        return True
    else:
        return False

def cuposs(cupo):
    if cupo>0:
        return True
    else:
        cupo<=0
        return False





def menu():
    while True:
        try:
            print("==== Menu Principal ====")
            op=int(input("Bienvenido al menu, seleccione una opcion con los numeros \n1)Cupos por genero \n2)Busqueda de peliculas por rango de precio \n3)Actualizar precio de pelicula \n4)Agregar pelicula \n5)Eliminar pelicula \n6)Salir \n"))
            print("========================")
        except ValueError:
            print("ingrese numeros porfavor")
        match op:
            case 1:
                genero=input("Que genero de la pelicula busca: ")
                cupos_genero(genero)
            case 2:
                try:
                    min=int(input("ingrese el precio minimo: "))
                    max=int(input("ingrese el precio maximo: "))
                    busqueda_precio(min,max)
                except ValueError:
                    print("debe ingresar valores enteros")
            case 3:
                next=0
                while next!="n":
                    codigo=input("ingrese el codigo que va actualizar: ")
                    try:
                        nuevo_precio=int(input("ingrese el nuevo precio: "))
                    except ValueError:
                        print("ingrese numeros enteros")
                    if actualizar_precio(codigo,nuevo_precio):
                        print("precio actualizado")
                    else:
                        print("El codigo no existe")
                    next=input("¿Desea actualizar otro precio (s/n)?: ")
            case 4:
                salir=0
                while salir!="yes":
                    codigo=input("ingrese el codigo del producto: ")
                    if codigon(codigo):
                        print("ingresando codigo")
                    else:
                        print("codigo ya en sistema")
                        salir="yes"
                    titulo=input("ingrese el titulo: ").title().replace(" ","")
                    generon=input("ingrese el genero de la pelicula: ").lower()
                    try:
                        duracion=int(input("ingrese la duracion de la pelicula: "))
                        if duracionn(duracion):
                            print("ingresando duracion")
                        else:
                            print("codigo incorrecto")
                            salir="yes"
                    except ValueError:
                        print("ingrese solo numeros")
                    clasificacion=input("ingrese la clasificacion: ").upper()
                    if clasificacionn(clasificacion):
                        print("ingresando clasificacion")
                    else:
                        print("clasificacion incorrecta")
                        salir="yes"
                    idioma=input("ingrese el idioma de la pelicula: ").title().replace(" ","")
                    es_3d=input("la pelicula es 3d (s/n): ").lower()
                    if es_3dd(es_3d):
                        print("ingresando datos")
                    else:
                        print("datos erroeneos")
                        salir="yes"
                    try:
                        precio=int(input("ingrese el precio de la pelicula: "))
                        if precioo(precio):
                            print("ingresando precio")
                        else:
                            print("precio incorrecto,saliendo")
                            salir="yes"
                        cupos=int(input("cuantos cupos hay disponibles?: "))
                        if cuposs(cupos):
                            print("ingresando")
                        else:
                            print("cupos incorrectos")
                            salir="yes"
                    except ValueError:
                        print("ingrese solo numeros")
                    peliculas.setdefault(codigo,[]).append(f"{titulo},{generon},{duracion},{clasificacion},{idioma},{es_3d},{es_3dd(es_3d)}")
                    cartelera.setdefault(codigo,[]).append(f"{precio},{cupos}")
                    print(peliculas)
                    print(cartelera)
                    
            case 5:
                mostrarpel()    
                codigo=input("ingrese el codigo de la pelicula que desea eliminar: ")
                if eliminar_pelicula(codigo):
                    print("Pelicula eliminada")
                else:
                    print("El codigo no existe")
            case 6:
                print("Programa finalizado")
                break
            case _:
                print("opcion invalida")


menu()