print('* Seja Bem-Vindo a loja do José Renildo dos Santos Junior! *')
valor = float(input('Informe o valor do produto em R$:'))
qtd = int(input('Agora informe a quantidade:'))
# Condições de acordo com as quantidades

# Abaixo de 200 unidades
if qtd <200:
    total = qtd * valor
    print(f'Sua compra totalizou em R$ {total:.2f}')
    print(f'Abaixo de 200 quantidades NÃO HÁ desconto.')
# Igual ou maior que 200 unidades e menor do que 1000
elif qtd >= 200 and qtd <1000:
    total = valor * qtd
    desconto = (total * 5) / 100
    com_desconto = total - desconto
    print(f'O valor da sua compra SEM desconto fica R$ {total:.2f}')
    print(f'O valor da sua compra COM desconto fica R$ {com_desconto:.2f}')
# Igual ou maior do que 1000 unidades e menor que 2000
elif qtd >= 1000 and qtd <2000:
    total = valor * qtd
    desconto = (total * 10) / 100
    com_desconto = total - desconto
    print(f'O valor da sua compra SEM desconto fica R$ {total:.2f}')
    print(f'O valor da sua compra COM desconto fica R$ {com_desconto:.2f}')
# Igual ou maior que 2000 unidades
else:
    total = valor * qtd
    desconto = (total * 15) / 100
    com_desconto = total - desconto
    print(f'O valor da sua compra SEM desconto fica R$ {total:.2f}')
    print(f'O valor da sua compra COM desconto fica R$ {com_desconto:.2f}')