import lerJson as ler
import menu
import datetime as dt

dados = ler.ler_arquivo()
raca = menu.menu()

if raca:
  peso = dados.get(raca)
  preco = peso * 2.5

  print(f'Raça: {raca}')
  print(f'Peso: {peso}')
  print(f'Preço: R${preco}')


