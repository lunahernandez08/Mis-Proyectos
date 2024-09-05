def menu():
    print('Menú de bancos')
    print('1. Bancolombia')
    print('2. AV Villas')
    print('3. Banco Bogotá')
    print('Otros bancos')

if True:
    menu()
    OPTION = int(input('Elige una opción: '))
    if OPTION == 1:
        print('Elegiste Bancolombia')
    if OPTION == 2:
        print('Elegiste AV Villas')
    if OPTION == 3:
        print('Elegiste Banco Bogotá')
    if OPTION == 4:
        print('Otro banco')
        BANK= input('Ingresa el nombre del banco: ')
        print('Tu banco es: ' + BANK)

    INTENTOS = 0
    for INTENTOS in range (3):
        PASSWORD = int(input('Ingresa la contraseña: '))
        if PASSWORD == 1234:
            print ('Correcto')
            def menu():
                print('Menu de opciones')
                print('1. Consultar Saldo')
                print('2. Ingresar Saldo')
                print('3. Retirar saldo')
                print('Salir')
            if True:
                menu()
                CONSULTA = int(input('¿Qué quiere hacer?: '))
                if CONSULTA == 1:
                    SALDO = 700000
                    print('Tu saldo actual es: $700.000')
                if CONSULTA == 2:
                    SALDO = 700000
                    print ('Ingresa la cantidad a depositar')
                    DEPOSITO = int(input('Ingrese el valor: '))
                    DEPOSITO1 = SALDO + DEPOSITO
                    print ('Tu saldo actual es: ')
                    print (DEPOSITO1)
                if CONSULTA == 3:
                    SALDO = 700000
                    print ('Ingresa la cantidad a retirar')
                    RETIRO = int(input('Ingrese el valor: '))
                    RETIRO1 = (SALDO - RETIRO)
                    if (RETIRO1 < SALDO):
                        print ('Tu saldo actual es: ')
                        print(RETIRO1)
                    else:
                        SALDO = 700000
                        RETIRO2 = (SALDO - RETIRO)
                        print ('Tu cantidad supera el saldo')
                        print ('Tu saldo actual es: ')
                        print (SALDO)
                if CONSULTA == 4:
                    print ('Sesión Cerrada. Te esperamos pronto')
                break
        else:
            print ('Error. Intentálo de nuevo')
    if PASSWORD != 1234:
        print ('Se agotaron los intentos. Acceso denegado')
