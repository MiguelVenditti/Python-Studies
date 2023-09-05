x = int(input("Digite seu Número para\ncalcular seu Fatorial: "))
count = x

for fatorial in range(x -1, 0, -1):
    count *= fatorial

print("{}! = {}".format(x, count))

"""import math
x = int(input("Digite seu Número para\ncalcular seu Fatorial: "))
f = math.factorial(x)
print("{}! = {}".format(x, f))"""
