# ==  Conhecendo o While Loop ==

# Criar uma programação para um  produto no valor de R$1.00

#  Tipo de uma Promoção que automaticamente ela muda durante os dias do mes. 

#Introdução do código!
print('='*40)
print('Cadastro de Promoção de Mercadoria')
print('='*40)
#nome do produto!
produto = input('Produto deseja coloca a progromoção: ')
print('='*40)
# Valor da Mercaria que vai entrar em promoção.
valor = float(input('Digite o Valor: '))
print('='*40)
# Valor do desconto Diario que o produto vai receber.
valor_desconto = float(input('Valor do desconto: '))
# Intervalos de dia corrido que o produto permanece em promoção!
print('='*40)
intervalor_dia = int(input('Qual intervalor de dias da promoção; '))
print('='*40)
# Valor Minimo do produto!
valor_minimo = float(input('Qual valor minimo: '))
print('='*40)
# Formula do código!
dia = intervalor_dia
while valor > valor_minimo:
  dia += 1
  print(f' Promoção Valida para Hoje {dia} A Proveite {produto} Só R${valor}')
  valor -= valor_desconto
  #  Explicação:

#Aqui estou fazendo um loop dizendo ao código para ele permanecer até atingir o valor mínimo do produto, então ele vai continuar, ate chegar nesse valor. Em dia += 1 estou dizendo a ele um final. E os dias que quero que ele faça a soma da promoção, se eu colocar 2 ele vai pular dois dias para cada lançamento.
  
  


