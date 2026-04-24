codigo_do_estado = int(input("Digite o código do estado de origem da carga: "))
peso_da_carga = int(input("Digite o peso da carga em toneladas: "))
codigo_da_carga = int(input("Digite o codigo da carga: "))
conversao = peso_da_carga * 1000


if codigo_da_carga >= 10 and codigo_da_carga <= 20:
   preco_da_carga = 100 * conversao
elif codigo_da_carga >= 21 and codigo_da_carga <= 30:
   preco_da_carga = 250 * conversao
else:
   preco_da_carga = 340 * conversao

if codigo_do_estado == 1:
   valor_imposto = 0.35 * preco_da_carga
elif codigo_do_estado == 2:
   valor_imposto = 0.25 * preco_da_carga
elif codigo_do_estado == 3:
   valor_imposto = 0.15 * preco_da_carga
elif codigo_do_estado == 4:
   valor_imposto = 0.05 * preco_da_carga
else:
   valor_imposto = 0 * preco_da_carga

valor_total = preco_da_carga + valor_imposto



print(f"Valor total transportado pelo caminhão é: {valor_total:.1f}")


