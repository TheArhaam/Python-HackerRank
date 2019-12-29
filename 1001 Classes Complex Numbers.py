import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        rres = self.real + no.real
        ires = self.imaginary + no.imaginary
        return Complex(rres,ires)

    def __sub__(self, no):
        rres = self.real - no.real
        ires = self.imaginary - no.imaginary
        return Complex(rres,ires)
        
    def __mul__(self, no):
        rres = (self.real * no.real) - (self.imaginary * no.imaginary)
        ires = (self.real * no.imaginary) + (self.imaginary * no.real)
        return Complex(rres,ires)

    def __truediv__(self, no):
        x=no.real**2+no.imaginary**2
        rres=(self.real*no.real+self.imaginary*no.imaginary)/x
        ires=(-no.imaginary*self.real+self.imaginary*no.real)/x
        return Complex(rres,ires)

    def mod(self):
        rres = math.sqrt((self.real**2)+(self.imaginary**2))
        ires = 0
        return Complex(rres,ires)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')