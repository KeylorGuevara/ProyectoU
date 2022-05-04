def ejercicio_1():
    valor_entrada= int(input('Por favor escriba un número entero: '))
    while valor_entrada % 2 == 0:
        valor_entrada= int(input('Por favor escriba un número entero: '))
    print('Muchas gracias.')

def ejercicio_2():
    monto_total_cuenta = int(input('Por favor escriba el saldo inicial: '))
    monto_solicitado_por_el_usuario = int(input('Por favor escriba su retiro: '))
    while monto_total_cuenta >= monto_solicitado_por_el_usuario:
        monto_total_cuenta -= monto_solicitado_por_el_usuario
        monto_solicitado_por_el_usuario= int(input(f'Transacción realizada. Su monto actual es de: {str(monto_total_cuenta)}. Por favor escriba su nuevo retiro: '))
    print('Se terminaron sus fondos.')

def ejercicio_3():
    total_capitulos_libro = 0
    total_dias_leidos =1
    cantidad_capitulos_leidos = int(input('¿Cuántos capítulos leyó hoy? '))
    finaliza_lectura_libro = input('¿Terminó el libro? ')
    while finaliza_lectura_libro != 'S':
        total_dias_leidos +=1
        total_capitulos_libro+= cantidad_capitulos_leidos
        cantidad_capitulos_leidos = int(input('¿Cuántos capítulos leyó hoy? '))
        finaliza_lectura_libro = input('¿Terminó el libro? ')
    print(f'Felicidades, usted leyó un libro de {str(total_capitulos_libro)} en {str(total_dias_leidos)} días.')

def ejercicio_4():
    numero_evaluado = int(input('¿Cuál número desea evaluar? '))
    evaluador =2
    while evaluador < numero_evaluado:
        if numero_evaluado%evaluador == 0:
            print(f'No es un número primo. Pues es divisible por: {str(evaluador)}.')
            break
        evaluador+=1
    if evaluador == numero_evaluado:
        print('¡Felicidades! Descubriste un número primo.')

def es_primo(num):
    for n in range(2, num):#incluye el 2 no incluye el num
        if num % n == 0:
            print("No es primo. Pues", n, "es divisor")
            return False
    print("Es primo")
    return True



# if main
# if __name__ == '__main__':
#     #ejercicio1()
#     #ejercicio2()
#     #ejercicio3()
#     #es_primo(37)
#     ejercicio_4()

# Por hacer:
# 1. Resolver los ejercicios que yo llevo.
# 2. Hacer un ejercicio largo.
# 3. Mandarlos en grupos a resolver 3 ejercicios, 2 fáciles y 1 difícil.
# 4. Revisar los ejercicios.
# 5. Tiempo de trabajo en tarea.