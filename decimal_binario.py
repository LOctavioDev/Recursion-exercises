# Un número decimal a binario

def decimal_binario(num):
    if num > 0: 
        if num < 2:
            print(num)
        else:
            decimal_binario(num // 2)
            print(num % 2) 
    else:
        raise ValueError('----------NUMERO NEGATIVO----------')
    
print(decimal_binario(15))