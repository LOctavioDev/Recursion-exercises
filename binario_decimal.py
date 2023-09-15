# Un número binario a decimal

def binario_decimal(binario):
    if binario < 2:
        return binario
    
    else:
        ultimo_digito = binario % 10        
        decimal =  2 * binario_decimal(binario // 10) + ultimo_digito 

        return decimal

print(binario_decimal(1010))