def PrimalNumbers(first):
    count = 4

    while first < 100:
        if(first % 2 == 0 or first % 3 == 0 or first % 5 == 0 or first % 7 == 0):
            first += 1
        else:
            first += 1
            count += 1

    return count-1


print(PrimalNumbers(1))
