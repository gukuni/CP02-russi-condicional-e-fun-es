


def juros_parcela(parcela):
    if parcela <= 6:
        return 0.05
    elif parcela <= 12:
        return 0.08
    elif parcela <= 24:
        return 0.10
def calculo_pmt(emprestimo, parcela):
    i = juros_parcela(parcela)
    pmt = emprestimo * (i * (1 + i)**parcela) / ((1 + i)**parcela - 1)
    return pmt



def idade_permitida(idade):
    return idade >= 18

def parcela_permitida(emprestimo, renda_mensal):
    return emprestimo <= renda_mensal *20


cliente = input("Digite o nome do cliente: ").strip()
idade = int(input("Digite a sua idade: "))
renda_mensal = float(input("Digite o valor da renda mensal: "))
emprestimo = float(input("Qual o valor desejado do emprestimo? "))
parcela = int(input("Você quer fazer em quantas parcelas (3 até 24)?"))
if idade_permitida(idade) and parcela_permitida(emprestimo, renda_mensal):
    taxa = juros_parcela(parcela) * 100
    pmt = calculo_pmt(emprestimo, parcela)
    print('Emprestimo aprovado!')
    print(cliente)
    print(emprestimo)
    print(f'{taxa}%')
    print(f'{pmt:.2f}')
    print(f'{pmt * parcela:.2f}')
    print(f'{(pmt * parcela) - emprestimo:.2f}')
else:
    print('Empréstimo negado!')
