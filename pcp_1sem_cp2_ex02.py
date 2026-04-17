a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

if a >= b and a >= c:
    A = a
    B, C = max(b, c), min(b, c)
elif b >= a and b >= c:
    A = b
    B, C = max(a, c), min(a, c)
else:
    A = c
    B, C = max(a, b), min(a, b)

if A >= B + C:
    print("não forma triangulo")
else:

    if A**2 == B**2 + C**2:
        print("triangulo retangulo")
    elif A**2 > B**2 + C**2:
        print("triangulo obtusangulo")
    else:
        print("triangulo acutangulo")

    if A == B == C:
        print("trinagulo equilatero")
    elif A == B or B == C or A == C:
        print("triangulo isosceles")
