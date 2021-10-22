def Power(number, power):
    answer, i = number, 1
    while i < power:
        answer *= number
        i += 1
    return answer
