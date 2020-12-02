from numbers import Number
from decimal import Decimal
from fractions import Fraction

print(isinstance(2.0,Number))
print(isinstance(Decimal('2.0'),Number))
print(isinstance(Fraction(2,4),Number))
print(isinstance("2",Number))

print(Fraction(10,4))
print(Decimal(5.2))

print(round(100.2565,2))
print(round(100.000056,3))
print((2.2+1.1)==3.3)

print(0b101)
print(0o10)
print(0x1F)