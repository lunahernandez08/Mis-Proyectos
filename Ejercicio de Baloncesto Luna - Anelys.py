# Dar la bienvenida a la convocatoria
print("Bienvenido a la convocatoria de jugadores de baloncesto.")

# Solicitar el nombre del jugador
nombre = input("Ingrese su nombre: ")

# Introducción de como se dara el puntaje
print("Para conocer cuál es su nivel y los minutos que jugara, responda las siguientes preguntas")

# Preguntas para conocer su nivel y los minutos
pregunta_1 = input("¿Con que frecuencia entrenas baloncesto? (nunca/a veces/regularmente/siempre): ")
pregunta_2 = input("¿Cuantos años de experiencia tienes jugando baloncesto? (0/1-2/3-5/mas de 5): ")
pregunta_3 = input("¿Participaste en algún campeonato de baloncesto? (ninguno/local/nacional/internacional): ")
pregunta_4 = input("¿cuantos partidos importantes has ganado? (ninguno/1-2/3-5/mas de 5): ")

# Asignar los valores a las respuestas
if pregunta_1.lower() == "nunca":
    valor_1 = 0
elif pregunta_1.lower() == "a veces":
    valor_1 = 3
elif pregunta_1.lower() == "regularmente":
    valor_1 = 6
elif pregunta_1.lower() == "siempre":
    valor_1 = 12
    

if pregunta_2.lower() == "0":
    valor_2 = 0
elif pregunta_2.lower() == "1-2":
    valor_2 = 3
elif pregunta_2.lower() == "3-5":
    valor_2 = 6
elif pregunta_2.lower() == "mas de 5":
    valor_2 = 12


if pregunta_3.lower() == "ninguno":
    valor_3 = 0
elif pregunta_3.lower() == "local":
    valor_3 = 3
elif pregunta_3.lower() == "nacional":
    valor_3 = 6
elif pregunta_3.lower() == "internacional":
    valor_3 = 12


if pregunta_4.lower() == "ninguno":
    valor_4 = 0
elif pregunta_4.lower() == "1-2":
    valor_4 = 3
elif pregunta_4.lower() == "3-5":
    valor_4 = 6
elif pregunta_4.lower() == "mas de 5":
    valor_4 = 12

# Calcular la habilidad del jugador de acuerdo al puntaje
suma_valores = valor_1 + valor_2 + valor_3 + valor_4
habilidad_jugador = suma_valores / 4
print(f"señor(a) {nombre}, el valor de su habilidad es de: {habilidad_jugador}")

#Verificar el valor de habilidad y asignar el grupo y miutos de juego
if 0 <= habilidad_jugador <= 2:
    print("El jugador no tiene minutos de juego.")
    print("´Pertence al grupo A (Novato)")
    print("Se debe enfocar en su entrenamiento ¡Sigue entrenando!.")
elif 2 < habilidad_jugador <= 5:
    print("El jugador podra participar en el partido 5 minutos.")
    print("Pertenece al grupo B (Principiante)")
    print("El jugador debera entrenar de 3 a 4 veces por semana ¡Sigue esforzandote!.")
elif 5 < habilidad_jugador <= 10:
    print("El jugador podra participar en el partido 10 minutos.")
    print("Pertencees al grupo C (Intermedio)")
    print("No cumple las expectativas, ¡Sigue mejorando!.")
elif 10 < habilidad_jugador <= 12:
    print("El jugador podra participar en el partido 30 minutos.")
    print("Pertencer a un rango superior (Experto) ¡Sigue asi!")
    print("Para no saturar su habilidad; tiene un merecido desanso.")
else:
    print("Error en el cálculo de la habilidad.")

# Opción para salir de la convocatoria
print("¿Desea salir de la convocatoria? (si/no)")
salir_convocatoria = input(" ").lower()

if salir_convocatoria == "si":
    print("Ha salido exitosamente de la convocatoria.")
else:
    print("Continúa en la convocatoria. ¡Sigue entrenando y mejorando!")

#Información adicional
print("Recuerde que el equipo no debe superar los 5 jugadores activos en la cancha.")
print("El total de candidatos seleccionados es de 20 jugadores.")
print("Si se superan los 5 jugadores en el campo, el equipo perderá por desacato")
print("Si hay menos de 5 jugadores en le campo, el equipo perderá por WO (Walkover).")

# Fin del programa
print("Gracias por participar en el sistema de distribucción de equipos de baloncesto")

    
 
 
