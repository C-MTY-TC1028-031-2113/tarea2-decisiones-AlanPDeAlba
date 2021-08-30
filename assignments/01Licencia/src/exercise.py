def main():
    edad = int(input("Ingresa tu edad: "))
    if edad >= 18:
        id = input("¿Tienes identificación oficial? (s/n): ")
        if id == "s":
            print("Trámite de licencia concedido")
        elif id == "n":
            print("No cumples requisitos")
        elif id != "s" or "s":
            print("Respuesta incorrecta")
    else:
        print("No cumples requisitos")
    
    pass


if __name__ == '__main__':
    main()
