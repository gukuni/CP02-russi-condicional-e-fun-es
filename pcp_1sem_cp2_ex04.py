
def calcular_horas_extras(salario_base, horas):
    return (salario_base * 0.015) * horas

def calcular_descontos_faltas(salario_base, faltas):
    return (salario_base * 0.02) * faltas

def calcular_bonus(cargo, recebeu_bonus):
    if recebeu_bonus == "s":
        if cargo == 1:
            return 1000
        elif cargo == 2:
            return 500
        elif cargo == 3:
            return 300
        elif cargo == 4:
            return 100
    return 0

nome = input("Nome do funcionário: ")
cargo = int(input("Cargo (1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário): "))
salario_base = float(input("Salário base: R$ "))
horas_extras = int(input("Total de horas extras: "))
faltas = int(input("Total de faltas no mês: "))
bonus_input = input("Recebeu bônus por desempenho? (s/n): ").lower()

valor_hora_extra = calcular_horas_extras(salario_base, horas_extras)
valor_faltas = calcular_descontos_faltas(salario_base, faltas)
valor_bonus = calcular_bonus(cargo, bonus_input)

total_acrescimos = valor_hora_extra + valor_bonus
total_descontos = valor_faltas
salario_bruto = salario_base + total_acrescimos
salario_final = salario_bruto - total_descontos

print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Total de acréscimos: R$ {total_acrescimos:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Salário Final: R$ {salario_final:.2f}")