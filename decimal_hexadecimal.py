# # Un número decimal a hexadecimal

def decimal_hexa(decimal):
    if decimal == 0:
        return ''
    
    digitos_hexadecimales = '0123456789ABCDEF'
    
    residuo = decimal % 16
    cociente = residuo // 16
    
    resultado_f = decimal_hexa(cociente)
    
    hexadecimal = digitos_hexadecimales[residuo]
    
    resultado_final = resultado_f +  hexadecimal
    
    return resultado_final

print(decimal_hexa(10))

# print(10 % 16)
# print(10 // 16)