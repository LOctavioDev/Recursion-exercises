# Un número decimal a Zn.
def decimal_Zn(base, decimal):
    if decimal < base:
        return [decimal]
    
    else:
        cociente = decimal // base
        residuo = decimal % base
        listarec = decimal_Zn(cociente, base)
        
        listarec.append(residuo)
        
        return listarec
        
    
print(decimal_Zn(3,8))