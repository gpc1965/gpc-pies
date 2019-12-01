import math
def of(n):
      n = 1/math.factorial(n)
      return n

e = 0
for i in range (1000):
      e = of(i) + e
print ("2.7182818284590452353602874713527", e)
