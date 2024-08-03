while True:
    try:
        peso = float (input("Ingrese su peso:"))
        if peso <= 0:
            print("El peso debe ser mayor a 0")
        else:
            break
    except ValueError:
        print("El peso debe ser un numero")
        
    while True:
        try:
            altura = float(input("Ingrese su altura:"))
            if altura <= 0:
                print("La altura debe ser mayor que cero")
            else:
                break
        except ValueError:
            print("La altura debe ser un numero")
            
    IMC = peso / (altura **2)
    
    print("Su IMC es: {:2f}".format(IMC))

    if IMC < 18.5:
        print("Usted tiene bajo peso")
    elif IMC < 25:
        print ("Usted tiene un peso normal")
    elif IMC < 30:
        print("Usted tiene sobrepeso")
    else:
        print("Usted tiene obesidad")
        