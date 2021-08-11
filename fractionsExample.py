"""
rasyonelsayılarda operatörler kullanımı
"""

import fractions

w = fractions.Fraction(2, 3)

x = fractions.Fraction(3, 5)

y = fractions.Fraction(6, 11)

z = fractions.Fraction(1, 8)

result = w + x + y + z

print(result)

"""
fractions kullanmadan

"""
import math

class Rational: 
    def __init__(self, a, b):
        
        if not isinstance(a, int) or not isinstance(b,int):
            raise ValueError('numerator and denominator must not be int')
        
        if b == 0:
            raise ValueError('Denominator must not be 0 (zero)')
            
        gcd = math.gcd(a, b)
        
        self.a = a // gcd
        self.b = b // gcd
    
    def __repr__(self):
        if self.b ==1:
            return str(self.a)
        return f'{self.a}/{self.b}'

r = Rational(4, 5)
print(r)    

#t = Rational(4, 0)
#print(t)        


x = Rational(4, 1)
print(x) 
