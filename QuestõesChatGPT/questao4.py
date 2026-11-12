'''
Peça para o usuário digitar um número inteiro usando input(). 
Calcule e imprima o dobro e a metade desse número.(Lembrete: o input() 
sempre devolve um texto, então você vai precisar converter com int() ou float()).
'''

numb = int(input("Digite um número inteiro: "))

print (f"O dobro de {numb} é " , numb *2 )
print (f"A metade de {numb} é " , numb/2)