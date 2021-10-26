def DecimalToBinary(number):
    result = 0
    i = 0

    while (number >= 2):
        result = result + (int(number) % 2)*(10**i)
        number = int(number / 2)
        i += 1

    result += number * (10**i)
    return result


print(DecimalToBinary(10))
