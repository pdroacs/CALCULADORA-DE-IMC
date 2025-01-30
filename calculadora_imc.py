nome = 'Pedro'
altura = 1.86
peso = 94
imc = peso / altura ** 2

# f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura, pesa'
linha_2 = f'{peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)
