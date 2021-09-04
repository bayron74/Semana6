#1) Una farmacia desea un programa para ingresar el valor de 
# compra y calcular lo siguiente: si el pago se efectúa al 
# “contado”, calcular un descuento del 
# 5%; pero si el pago es con “tarjeta” se incrementa un recargo 
# del 3% al valor de compra. 
# Calcular y visualizar el descuento o recargo según 
# sea el caso y el total a pagar de la compra.

x = 1 
while x ==1:
#While signfica un bucle o un ciclo que so se detiene hasta que hay sierto limite

#Input significa escribir datos atraves del teclado y posteriormente se guardan
    valor = int(input("Ingresar valor de compra"))
    #le imprimos en pantalla si al contado o tarjeta
    print("al contado o tarjeta")
    #Le decimos al usuario que escribael metodo(contado o tarjeta)
    metodo = input("Ingrese el metodo de pago que realizara a comprar")
#si metodo es igaul a contado 
    if metodo == "contado":
        des = valor * 0.05
        valor = valor  - des
        print("se aplico descuento", valor)
        #El elif va existir solo si existe un if antes
    elif metodo == "tarjeta":
        aumento = valor * 0.03
        valor = valor  + aumento
        print("se aplico aumento", aumento)

    else:
        print("No seleccionaste el metodo correcto")
        x=2 #finalizacion del bucle 