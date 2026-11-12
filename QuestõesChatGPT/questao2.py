'''
Crie uma variável produto (texto), preco (float, ex: 49.90) 
e quantidade (int, ex: 3). Calcule o valor total da compra em uma 
quarta variável e imprima o resumo:(Ex: 3x Camiseta = R$ 149.70)
'''

t = str(input("Digite o nome do produto: "))
p = float(input("Digite o preço do produto: "))
qtd = int(input("Digite a quantidade de itens: "))

valorT = p * qtd

print (f"{qtd}x {t} = R$ {valorT}")