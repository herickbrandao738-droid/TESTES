'''
Crie uma variável ano_nascimento como texto ("2005") e ano_atual como inteiro (2026).
Converta o ano de nascimento para inteiro, calcule a idade e crie uma variável 
booleana maior_de_idade que guarda True se a idade for maior ou igual a 18 
(ou False caso contrário). Imprima a idade e o resultado booleano.
'''

maior_de_idade = True
ano_atual = 2026
ano_nascimento = input("Digite o ano de nascimento: ")

ano_nascimento = int(ano_nascimento)

if ano_atual - ano_nascimento > 18:
    print ("Você tem " , ano_atual-ano_nascimento , " anos e o resultado é: " , maior_de_idade)
else:
    maior_de_idade = False
    print ("Você tem " , ano_atual-ano_nascimento , " anos e o resultado é: " , maior_de_idade)