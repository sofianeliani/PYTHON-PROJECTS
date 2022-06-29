# Sinus
# sin x = Σ ((-1)^n * X^(2n + 1)) / (2n +1) 

# Cosinus
# cos x = Σ (- 1)^n * x^(2n) / (2n)
import math 

def sin(x):
    for n in range(9):
        sinX = (((-1)**(n)) * (x**(2 * n + 1))) / (math.factorial(2 * n + 1))
    print(sinX)

def cos(x):
    for n in range(9):
        cosX = (- 1)**n * x**(2 * n) / (2 * n)
        print(cosX)

def pi(x):
    x = 19000000
    pi4 = 0
    for i in range(x):
        pi4 += float( 4 * ((-1) ** i) / ((2 * i) + 1))
        print(pi4)
        print(math.pi)

x = math.radians(90)
sin(x)
# cos(x)