cp1 = float(input("Digite a nota do CP1: "))
cp2 = float(input("Digite a nota do CP2: "))
cp3 = float(input("Digite a nota do CP3: "))
sp1 = float(input("Digite a nota da Sprint 1: "))
sp2 = float(input("Digite a nota da Sprint 2: "))
gs = float(input("Digite a nota da Global Solution: "))

menor = cp1

if cp2 < menor:
    menor = cp2

if cp3 < menor:
    menor = cp3

media = ((cp1 + cp2 + cp3 - menor + sp1 + sp2) / 4) * 0.4 + gs * 0.6

mediaPeso = media * 0.4

print(f"Média do semestre: {media:.1f}")
print(f"Média do semestre com peso: {mediaPeso:.1f}")