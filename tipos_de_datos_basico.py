
#Ejercicio 1
'''Escribir un programa que pregunte al usuario por el número de horas trabajadas por dia y el coste por hora. 
Después debe mostrar por pantalla la paga que le corresponde. Ademas, mostrar si esta trabajando muchas
horas, regulares, o pocas horas, y tambien calcular el promedio de horas trabajadas por semana y su paga,
considera que la semana comprende 6 dias habiles y un dia de descanso; ademas de que un horario laboral
regular es de 8 horas, menos o igual de 6 son pocas y mas o igual de 10 son muchas y por ultimo, debes
mostrar los ressultados en una cadena formateada'''
'''
#definiendo las variables iniciales solicitadas al usuario
horas_trabajadas_por_dia : str = input("Ingresa el numero de horas que trabajas al día: \n")
paga_hora_trabajada : str = input("Ingresa cuanto te pagan por cada hora trabajada \n")

#definiendo la funcion para calcular lo solicitado
def horas_trabajadas(horas_trabajadas_por_dia, paga_hora_trabajada):
    paga_por_dia : int = int(horas_trabajadas_por_dia) * int(paga_hora_trabajada)
    horas_trabajadas_semana : int = int(horas_trabajadas_por_dia) * 6
    paga_por_semana : int = int(paga_hora_trabajada) * horas_trabajadas_semana

    if int(horas_trabajadas_por_dia) <= 6:
        return (f"por día ganas {paga_por_dia} MXN, y a la semana trabajas {horas_trabajadas_semana} horas, \n \
                estas trabajando POCAS HORAS, y ganas en promedio a la semana {paga_por_semana} MXN")
    elif int(horas_trabajadas_por_dia) >= 7 and int(horas_trabajadas_por_dia) <= 9:
        return (f"por día ganas {paga_por_dia} MXN, y a la semana trabajas {horas_trabajadas_semana} horas, \n \
                estas trabajando con horario REGULAR, y ganas en promedio a la semana {paga_por_semana} MXN")
    elif int(horas_trabajadas_por_dia) >= 10:
        return (f"por día ganas {paga_por_dia} MXN, y a la semana trabajas {horas_trabajadas_semana} horas, \n \
                estas trabajando MUCHAS HORAS, y ganas en promedio a la semana {paga_por_semana} MXN")
    else:
        return ("Algo salio mal, vuelve a reiniciar")
#solicitando que la funcion se pinte por pantalla (Comentar si no se necesita en un momento dado)
# print(horas_trabajadas(horas_trabajadas_por_dia, paga_hora_trabajada))
'''

#Ejercicio 2
'''Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla
la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal 
calculado redondeado con dos decimales.'''
'''
#Solicitando al usuario sus datos y guardandolo en variables
user_peso = input("Ingresa tu peso en KG: ")
user_estatura = input("Ingresa tu estatura en M: ")

#Creando la funcion de calculo de imc
def imc_user (user_peso, user_estatura):
    imc = float(user_peso) / (float(user_estatura) ** 2)
    return f"Tu índice de masa corporal es {imc.__round__(2)}"

#solicitando que la funcion se imprima en consola
print(imc_user(user_peso, user_estatura))
'''

#Ejercicio 3
'''Escribir un programa que pida al usuario dos números enteros y muestre por pantalla 
la <n> entre <m> da una division <d> y un resto <r> donde <n> y <m> son los números introducidos
por el usuario, y <d> y <r> son el cociente y el resto de la división entera respectivamente.
'''
'''
#Define las variables a pedir
numerador = input("Introduce el numero a dividir ")
divisor = input("Introduce el numero divisor ")
#funcion de operacion
def division_resto(numerador,divisor):
    try: 
        div = int(numerador) / int(divisor)
        rest = int(numerador) % int(divisor)
        return f"El {numerador} entre {divisor} da una division de {round(div,2)} y un resto de {rest}"
    except:
        raise Exception (ZeroDivisionError)
print(division_resto(numerador, divisor))
'''
'''
#Ejercicio 4
"Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión."

#Se definen las variables a solicitar (por consola)

inversion_inicial = input("Ingresa la cantidad que deseas invertir: ")
interes_anual = input("Ingresa la tasa anual de interes: ")
tiempo_de_inversion = input("Ingresa los años que deseas invertir: ")
#Funcion operativa
def calculo_inversion(inversion_inicial, interes_anual, tiempo_de_inversion):
    calculo = int(inversion_inicial) * (int(interes_anual) * int(tiempo_de_inversion)) // 100
    return calculo
print(calculo_inversion(inversion_inicial, interes_anual, tiempo_de_inversion))
'''
'''
#Ejercicio 5
"""Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta
por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el
peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada 
muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido
y calcule el peso total del paquete que será enviado."""

#Se definen variables
peso_payasos: int = 112 
peso_munecas: int = 75
cantidad_payasos = input("Ingresa cuantos payasos vendiste: ")
cantidad_munecas = input("Ingresa cuantas munecas vendiste: ")

#Funcion
def peso_venta(cantidad_payasos, cantidad_munecas):
    calc_payasos = int(cantidad_payasos) * peso_payasos
    calc_munecas = int(cantidad_munecas) * peso_munecas
    peso_total = calc_payasos + calc_munecas
    peso_kilos = peso_total / 1000
    return f"Tu paquete pesa {peso_total} gramos o {peso_kilos} kilos"
print(peso_venta(cantidad_payasos, cantidad_munecas))
'''

#Ejercicio 6
'''Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final
de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en 
la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla 
la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.'''

#Variables
deposito_inicial = input("Ingrese el monto a depositar en MNX: ")

#funcion
def rendimientos_ahorro(deposito_inicial):
    primer_a = int(deposito_inicial) + (int(deposito_inicial) * 4 / 100)
    segundo_a = primer_a + (int(primer_a) * 4 / 100)
    tercer_a = segundo_a + (int(segundo_a) * 4 / 100)
    return f"Tus ahorros al primer año son {round(primer_a,2)} MNX, al segundo son {round(segundo_a,2)} MNX, y al tercer año son de {round(tercer_a, 2)} MNX"
print(rendimientos_ahorro(deposito_inicial))