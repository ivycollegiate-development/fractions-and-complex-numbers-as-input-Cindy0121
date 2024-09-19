try:
    from fractions import Fraction
    a = Fraction(input ("Enter a fraction (ex: 3/4): "))
    print (a)
except ZeroDivisionError:
    print("Invaild fraction: denominator cannot be zero")