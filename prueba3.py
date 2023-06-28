listaTipo = []
listaDest = []
listaRut = []
listaPrecio = []
listaPeso = []
listaCiud = []
menuPaq = '''
Ingrese el tipo de paquete:
1. Sobre
2. Paquete
'''

def grabar ():
    #while Tipo
    while True:
        try:
            tipo = int(input(menuPaq))
            if tipo == 1:
                listaTipo.append('SOBRE')
                break
            elif tipo == 2:
                listaTipo.append('PAQUETE')
                break
            else:
                print('Ingrese un tipo correcto')
        except:
            print('Excepcion en tipo de encomienda')
    #while Nombre Destinatario
    while True:
        try:
            dest = input('Ingrese el nombre del destinatario: ').upper()
            if len(dest)>= 2 or len(dest)<= 30:
                listaDest.append(dest)
                break
            else:
                print('Ingrese un destinatario valido')
        except:
            print('Excepcion en destinatario')
    #while Rut Destinatario
    while True:
        try:
            rut = input('Ingrese el rut del destinatario: ')
            if rut[-2] == '-':
                listaRut.append(rut)
                break
            else:
                print('Ingrese un rut valido')
        except:
            print('Excepcion en rut destinatario')
    #while Precio
    while True:
        try:
            precio = int(input('Ingrese el precio de la encomienda: '))
            if precio>=2000:
                listaPrecio.append(precio)
                break
            else:
                print('Ingrese un precio correcto')
        except:
            print('Excepcion en precio')
    #while Peso
    while True:
        try:
            peso = int(input('Ingrese el peso de la encomienda en kilos: '))
            if peso>=0.1:
                listaPeso.append(peso)
                break
            else:
                print('Ingrese un peso correcto')
        except:
            print('Excepcion en peso')
    #while Ciudad de destino
    while True:
        try:
            ciudad = input('Ingrese la ciudad de destino: ').upper()
            if len(ciudad)>=3:
                listaCiud.append(ciudad)
                break
            else:
                print('Ingrese una ciudad correcta')
        except:
            print('Excepcion en ciudad de destino')

def buscar():
    run = input('Ingrese el rut que desea buscar: ')
    if run in listaRut:
        print(f'LISTA ENCOMIENDAS')
        print('--------------------------------------------------------------------------------')
        print('TIPO     RUT             NOMBRE                 CIUDAD            PESO    PRECIO')
        print('--------------------------------------------------------------------------------') #50c
        for i in range(len(listaRut)):
            if listaRut[i] == run:
                print(f'{listaTipo[i]:8s}|{listaRut[i]:11s}|{listaDest[i]:25s}|{listaCiud[i]:20s}|{listaPeso[i]:3d}|{listaPrecio[i]:7d} ')
                print('--------------------------------------------------------------------------------')
    else:
        print('Rut no encontrado.')

def listar():
    contSobres = 0
    contPaquetes = 0
    print(f'LISTA ENCOMIENDAS')
    print('--------------------------------------------------------------------------------')
    print('TIPO     RUT             NOMBRE                 CIUDAD            PESO    PRECIO')
    print('--------------------------------------------------------------------------------')
    for i in range(len(listaRut)):
        if listaTipo[i] == 'SOBRE':
            contSobres += 1
        elif listaTipo[i] == 'PAQUETE':
            contPaquetes += 1
        print(f'{listaTipo[i]:8s}|{listaRut[i]:11s}|{listaDest[i]:25s}|{listaCiud[i]:20s}|{listaPeso[i]:3d}|{listaPrecio[i]:7d} ')

    print('--------------------------------------------------------------------------------')
    print(f'Total Sobres: {contSobres}')
    print(f'Total Paquetes: {contPaquetes}')

def salida():
    print('Saliendo del programa...')
    print('Software Caracol Express v1.0.0 por Barbara Poblete')

constmenu = '''
    MENU
------------
1. Grabar
2. Buscar
3. Listar
4. Salir
'''

def menu():
    while True:
        try:
            opcion = int(input(constmenu))
            if opcion == 1:
                grabar()
            elif opcion == 2:
                buscar()
            elif opcion == 3:
                listar()
            elif opcion == 4:
                salida()
                break
        except:
            print('Excepcion en menu')

menu()