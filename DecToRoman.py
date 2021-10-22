def DecToRoman(number):
    m = ["", "M"]
    c = ["", "C", "CC", "CCC", "CD", "D",
         "DC", "DCC", "DCCC", "CM "]
    x = ["", "X", "XX", "XXX", "XL", "L",
         "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]

    thousands = m[number // 1000]
    hundereds = c[(number % 1000) // 100]
    tens = x[(number % 100) // 10]
    ones = i[number % 10]

    answer = (thousands + hundereds +
              tens + ones)
    return answer


print(DecToRoman(25))
