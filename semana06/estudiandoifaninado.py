#Si gasto hasta $100, pago con dinero en efectivo. Si no, si gasto más de $100 pero menos de $300, pago con tarjeta de débito. Si no, pago con tarjeta de crédito

#obtencion de datos
compra = int(input("Coloque el valor de su compra"))

#EN el primer if vamos a comparar si se cumple ese dato
#que sean igaules o menores que 100
#print significa imprimir un mensaje
if compra <= 100:
    print ("Pago en efectivo")
#elif significa que vamos a evaluar otra condicion
#And significa que vamos a evaluar 2 condiciones o 2 resultados
#Que se cumplan las condiciones de la izquierda y la derecha
elif compra > 100 and compra < 300: 
    print ("Pago con tarjeta de débito")
#Else significa que si no se cumplen las demas que se cumpla la siguiente
else:
    print ("Pago con tarjeta de crédito")