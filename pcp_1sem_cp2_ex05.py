


def juros_parcela(parcela):
    if 3 <= parcela <= 6:
        return 0.05
    elif 7 <= parcela <= 12:
        return 0.08
    elif 13 <= parcela <= 24:
        return 0.10
     
def calculo_pmt(emprestimo, parcela):
    i = juros_parcela(parcela)
    pmt = emprestimo * (i * (1 + i)**parcela) / ((1 + i)**parcela - 1)
    return pmt


def pode_aprovar(idade, emprestimo, renda_mensal):
    return idade >= 18 and emprestimo <= renda_mensal *20



def valor_total (pmt, parcela):
    total = pmt * parcela
    return total

def valor_juros (total, emprestimo):
    juros = total - emprestimo
    return juros


cliente = input("Digite o nome do cliente: ").strip()
idade = int(input("Digite a sua idade: "))
renda_mensal = float(input("Digite o valor da renda mensal: "))
emprestimo = float(input("Qual o valor desejado do emprestimo? "))
parcela = int(input("Você quer fazer em quantas parcelas (3 até 24)?"))
while parcela < 3 or parcela > 24:
    parcela = int(input("Número de parcelas inválidos! Digite o número de parcelas novamente: "))
if idade_permitida(idade) and parcela_permitida(emprestimo, renda_mensal):
    taxa = juros_parcela(parcela) * 100
    pmt = calculo_pmt(emprestimo, parcela)
    total = valor_total(pmt, parcela)
    juros = valor_juros(total, emprestimo)
    print('Emprestimo aprovado!')
    print(cliente)
    print(emprestimo)
    print(f'{taxa}%')
    print(f'{pmt:.2f}')
    print(f'{total:.2f}')
    print(f'{juros:.2f}')
else:
    print('Empréstimo negado!')
