# Un número hexadecimal a decimal

def hexa_decimal(hexa):
    equivalente_hexadecimal = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }

    if hexa == "0":
        return 0

    if len(hexa) == 1:
        return equivalente_hexadecimal[hexa]

    ultimo_digito = hexa[-1]

    decimal = equivalente_hexadecimal[ultimo_digito] + 16 * hexa_decimal(hexa[:-1])

    return decimal
         
print(hexa_decimal('1A3'))