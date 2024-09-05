def menu_banco():
    print("Bienvenido a su Sucursal Virtual Bancaria.")
    print("Elija el banco: ")
    print("1. Banco de Bogotá")
    print("2. Bancolombia")
    print("3. AV Villas")
    print("4. Otros: ")
menu_banco()
if True:
    OPCIONES = int(input("Ingresar el banco: "))
    if OPCIONES ==1:
        print("Haz elegido Banco de Bogotá")
    if OPCIONES ==2:
        print("Haz elegido Bancolombia")
    if OPCIONES ==3:
        print("Haz elegido AV Villas")
    if OPCIONES ==4:
        print("Haz elegido otro banco")
        BANCO = input("Ingresar otro banco: ")
        print("El banco elegido es " + BANCO)
        

NOMBRE = input("Por favor, ingrese su nombre: ")

def opciones_documento():
     print("Elija su tipo de documento de identificación: ")
     print("1. Tarjeta de identidad.")
     print("2. Cédula de ciudadanía.")
     print("3. Cédula de extranjería.")
     print("4. PPT.")
opciones_documento()
if True:
    OPCIONESDOCUMENTO = int(input("Ingresar tipo de documento de identidad: "))
    if OPCIONESDOCUMENTO ==1:
        print("Elegiste tarjeta de identidad.")
        TI = int(input("Digíte su numero: "))
    if OPCIONESDOCUMENTO ==2:
        print("Elegiste Cédula de ciudadanía")
        CC = int(input("Digíte su numero: "))
    if OPCIONESDOCUMENTO ==3:
        print("Elegiste Cédula de extranjería")
        CE = int(input("Digíte su numero: "))
    if OPCIONESDOCUMENTO == 4:
        print("Elegiste PPT")
        PPT= int(input("Digíte su numero: "))
        
INTENTOS = 3
for i in range(INTENTOS):
    CONTRASEÑA = int(input("Ingrese su contraseña: "))
    if CONTRASEÑA == 2024:
        def menu_opciones_bancarias():
            print("Elija la transaccion que desea realizar:")
            print("1. Retiros.")
            print("2. Avance de tarjeta de crédito con código de seguridad.")
            print("3. Depósitos.")
            print("4. Consultar saldo.")
            print("5. Pagar facturas.")
            print("6. Registrar cuenta.")
        menu_opciones_bancarias()
        if True:
            OPB= int(input("Seleccione la transacción a realizar:"))
            if OPB == 1:
                SALDO = 2528000
                RETIRO= float(input("Digíte la cantidad del retiro: $"))
                RETIRO1=(SALDO-RETIRO)
                if (RETIRO <= SALDO):
                    print(f"Su saldo actual es de {RETIRO1} ")
                    print("Se ha completado su transacción. Se ha cerrado la sesión. ¡Vuelva pronto!")
                else:
                    print ("Saldo insuficiente")
                    print("Se ha cerrado la sesión. ¡Vuelva pronto!")
            if OPB == 2:
                CODIGO = int(input("Digite el código de seguridad(que es de 4 digitos): "))
                RETIRO2 = int(input("Digite la cantidad a retirar: $"))
                SALDO = 2528000
                SALDO -= RETIRO2
                if (RETIRO2 <= SALDO):
                    print(f"Su saldo actual es de: ${SALDO}")
                    print("Su tarjeta de crédito fue avanzada.")
                    print("Se ha completado su transacción. Se ha cerrado la sesión. ¡Vuelva pronto!")
                else:
                    print("El saldo es insuficiente.")
                    print("Se ha cerrado la sesión. ¡Vuelva pronto!")
            if OPB == 3:
                def bancos_depositos():
                    print("Elija el banco al que desea realizar el deposito")
                    print("1.Banco seleccionado.")
                    print("2.Otro banco.")
                bancos_depositos()
                if True:
                    OBD = int(input("Seleccione el banco: "))
                    if OBD == 1:
                        print("Haz elegido el mismo banco.")
                        NC = int(input("Ingrese el número de cuenta: "))
                        VALOR = float(input("Digite el valor a depositar: "))
                        print(F"El valor  depositado es ${VALOR}")
                        print("Se ha completado la transacción. Se ha cerrado sesión. ¡Vuelva Pronto!")
                    if OBD == 2:
                        print ("Haz elegido otro banco")
                        BD = input("Ingrese el nombre del banco: ")
                        CE = int(input("Digite el numero de cuenta: "))
                        VALORE = float(input("Digite el valor a depositar: "))
                        print(F"El valor depositado en la cuenta {CE} es de ${VALORE} . EL DEPOSITO SE REFLEJARA EN LA CUENTA DESPUES DE 12 HORAS.")
                        print("Se ha completado la transacción. Se ha cerrado sesión. ¡Vuelva peonto!")
            if OPB == 4:
                SALDO = 2528000
                print(f"Su saldo es de ${SALDO}")
                print("Se ha completado la transacción. Se ha cerrado sesión. ¡Vuelva pronto!")
            if OPB == 5:
                NF = int(input("Ingrese el número de la factura: "))
                VF = float(input("Digite la cantidad a pagar: "))
                SALDO = 2528000
                if (VF <= SALDO):
                    print("Su factura ha sido pagada con exito")
                    RESTA =(SALDO-VF)
                    print(F"Su saldo es de {RESTA}")
                    print("Se ha completado la transacción. Se ha cerrado sesión. ¡Vuelva Pronto!")
                else:
                    print("El valor a pagar supera el saldo de la cuenta")
                    print("Se ha cerrado sesión. ¡Vuelva pronto!")
            if OPB == 6:
                print("Ingrese los siguientes datos para registrar cuenta")
                NOMBRE_C = input("Ingrese su nombre completo: ")
                ND2 = int(input("Digite su número de documento: "))
                NCE = int(input("Digite su número de celular: "))
                CONTRASEÑA2 = int(input("Cree una contraseña: "))
                CONTRASEÑA3 = int(input("Confirme la contraseña: "))
                print("Su cuenta ha sido registrada con exito.")
                print("Se ha cerrado sesión. ¡Vuelva pronto!")
                break
            break
    else:
        if i < INTENTOS - 1:
            print(f"Error. Te quedan {INTENTOS - i - 1} intentos.")
        else:
            print("Los intentos se han agotado. El acceso ha sido denegado")
                
                
                        
