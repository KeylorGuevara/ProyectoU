def ejercicio_1():
    print('Este es el ejercicio #1')
    numero_entrada = int(input('Por favor, escriba un número entero par: '))
    while numero_entrada % 2 == 0:
        #n cantidad de instrucciones
        numero_entrada = int(input('¡Excelente! Escriba un nuevo número entero par: '))
    print('Muchas gracias pero eso es un número impar.')

def ejercicio_2():
    monto_total_cuenta = int(input('Por favor, escriba el monto total inicial de su cuenta: '))
    monto_solicitado_por_el_usuario = int(input('Por favor, escriba el monto de su primer retiro: '))
    while monto_total_cuenta >= monto_solicitado_por_el_usuario:
        monto_total_cuenta -= monto_solicitado_por_el_usuario # 55600 - 5600 = 50000
        monto_solicitado_por_el_usuario = int(input('Por favor, digite el monto a retirar: '))
        #Agregar una condicion para saber si ya la cuenta esta en 0, de ser asi 
        #aqui terminar el ciclo.
    print('No cuenta con fondos suficientes')

def ejercicio_3():
    cantidad_capitulos_leidos = int(input('¿Cuántos capítulos leyó hoy? '))
    finaliza_lectura_libro = input('¿Terminaste de leer libro? ')
    total_capitulos_del_libro, total_de_dias = 0, 1
    while finaliza_lectura_libro != 'S' and finaliza_lectura_libro != 's':
        total_de_dias += 1
        total_capitulos_del_libro += cantidad_capitulos_leidos
        cantidad_capitulos_leidos = int(input('¿Cuántos capítulos leyó hoy? '))
        finaliza_lectura_libro = input('¿Terminaste de leer libro? ')
    total_capitulos_del_libro += cantidad_capitulos_leidos
    print(f'¡Felicidades! Usted leyó un libro de {str(total_capitulos_del_libro)} capítulos, en {total_de_dias} días. Super rápido')
          









if __name__ == '__main__':
    #ejercicio_1()
    ejercicio_2()
    #ejercicio_3()
