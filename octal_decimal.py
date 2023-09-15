# Un número octal a decimal
def octal_decimal(octal):
    if len(octal) == 0:
        return 0
    else:
        ultimo_digito = int(octal[-1])
        resto = octal[:-1]
        return (ultimo_digito + 8 * octal_decimal(resto))
    
# print(octal_decimal())


cadena = "1804"
print(cadena[:-1])