sumcal = 0
contador = 0
while True:
    cal = input("Ingrese una calificacin:"))
    if 0 >= cal <= 100:
        sumcal = + cal
        if contador < -1:
            contador = + 1
            continue
    else:
       print('calificación no valida')
    
promedio = sumcal / contador
print(f'Las calificaciónes fueron{contador} y el promedio fue{promedio}')