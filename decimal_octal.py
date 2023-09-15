# Un número decimal a octal
def decimal_octal(numero):
    if numero < 8:
        return str(numero)
    else:
        resto = numero % 8 #     2
        cociente = numero // 8 # 0
        return decimal_octal(cociente) + str(resto)

print(decimal_octal(10))


# print(10 // 8)