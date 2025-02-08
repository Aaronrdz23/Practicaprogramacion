def get_float(s: str)-> float:
    while True:
        num = input(f'{s}:')
        try: 
            return float(num)
        except ValueError:
            print('ingrese un número valido')

def area(areac)-> float:
    pi =3.14
    areac = pi * (r**2)
    return(areac)

def circun(circu)-> float:
    pi =3.1416
    d = r*2

    circu = pi * d
    return(circu)

r =get_float('Ingrese el radio del circulo: ')
areac =area(r)
circu =circun(r)
print(f'El área es {areac} y la circunferencia es {circu}')