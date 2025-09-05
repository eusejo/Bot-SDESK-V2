import questionary
from main import Controller
from colorama import Fore, init
init(autoreset=True)

class Tester(Controller):
    def retornar_parser(self):
        return self.parser.print_help()

class Menu:
    def criar_menu(self):
        teste = Tester()
        
        choice = [
            '1 - Chamado para agora',
            '2 - Agendar chamado',
            '3 - Pedir ajuda',
            '4 - Fechar',
        ]
        
        s = questionary.select(
            'o que vc quer fazer? ',
            choices=choice
        ).ask()
        
        num = choice.index(s)
        
        if num == 0:
            print(Fore.GREEN+'[!] Use argumentos para criar um chamado')
        elif num == 1:
            pass
        elif num == 2:
            teste.retornar_parser()
        elif num == 3:
            print(Fore.RED+'[!] Fechando...')