import lerBanco as ler
import menu

op = menu.menu()
dados = ler.ler_arquivo()
def listar():
  for sigla in dados.keys():
    print(sigla)

def buscar():
  busca = input("Digite a sigla do time que deseja buscar: ").upper()
  print(f"Buscando {busca} no banco de dados...")
  if busca in dados:
    busca = dados[busca]
    print(busca)

def listarTodo():
  for sigla in dados.values():
    print(sigla)


match(op):
  case '1':
    listar()
  case '2':
    buscar()
  case '3':
    listarTodo()

