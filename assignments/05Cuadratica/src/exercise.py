import math

def main():
    # Escribe tu código abajo de esta línea
    a=int(input("Da el valor de a: "))
    b=int(input("Da el valor de b: "))
    c=int(input("Da el valor de c: "))
    if a == 0 and b == 0:
        print("No tiene solucion")
    elif a == 0 and b != 0:
        print((-1*c)/b)
    elif a != 0 and b != 0:
        if ((b**2) - 4*a*c) < 0:
            print("Raices complejas")
        elif ((b**2) - 4*a*c) == 0:
            print((-1*b)/(2*a))
        elif ((b**2) - 4*a*c) > 0:
            print(((-1*b) + math.sqrt(b**2 - (4*a*c)))/(2*a))
            print(((-1*b) - math.sqrt(b**2 - (4*a*c)))/(2*a))
    pass

if __name__ == '__main__':
    main()
