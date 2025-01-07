import os
def show_program_name():
  print(""""
  ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗███████╗░██████╗░██████╗
  ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝
  ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░█████╗░░╚█████╗░╚█████╗░
  ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░██╔══╝░░░╚═══██╗░╚═══██╗
  ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗███████╗██████╔╝██████╔╝
  ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚══════╝╚═════╝░╚═════╝░
  """)
def show_options():
  print('1. Cadastrar restaurante')
  print('2. Listar restaurantes')
  print('3. Ativar restaurante')
  print('4. Sair\n')
def encerrando_aplicação():
  os.system('clear') 
  print('Encerrando aplicação')
def choose_option():
  opcao_escolhida = int(input('Escolha uma opção: '))
  print(f'Opção escolhida {opcao_escolhida}!')
  # if opcao_escolhida == 1:
  #   print('Cadastrando restaurante')
  # elif opcao_escolhida == 2:
  #   print('Listando restarantes')
  # elif opcao_escolhida == 3:
  #   print('Ativando restaurante')
  # else :
  #   encerrando_aplicação()
  match opcao_escolhida:
    case 1:
      print('Cadastrando restaurante')
    case 2:
      print('Listando restarantes')
    case 3:
      print('Ativando restaurante')
    case _:
      encerrando_aplicação()
def main():
  show_program_name();
  show_options();
  choose_option();
if __name__ == '__main__':
  main()