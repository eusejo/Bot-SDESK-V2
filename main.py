from core import chamados, Menu, CriarLogs
from dotenv import load_dotenv
from colorama import Fore, init
import argparse
import socket
import os

init(autoreset=True)
load_dotenv()

class Controller:
    def __init__(self):
        self.user = os.getenv('LOGIN_SDESK_USER')
        self.password = os.getenv('LOGIN_SDESK_PASSWORD')
        self.parser = argparse.ArgumentParser(
        description='Bot para abrir chamados usando Selenium e Sdesk',
        usage='python main.py --entrada <valor>')
        self.parser.add_argument('-t', '--tipo', type=int, help='Especifique o tipo de serviço')
        self.parser.add_argument('-e', '--equipa', type=str, help='Especifique o tipo de equipamento')
        self.args = self.parser.parse_args()
        self.menu = Menu.Menu()
        self.logg = CriarLogs.Logs()
        
    def verificar_conexao(self, host='8.8.8.8', port=53, timeout=3):
        try:
            socket.setdefaulttimeout(timeout)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host,port))
            return True
        except socket.error as error:
            return False
    
    def banner(self):
        banner = '''
    ███████╗██████╗ ███████╗███████╗██╗  ██╗██████╗  ██████╗ ████████╗
    ██╔════╝██╔══██╗██╔════╝██╔════╝██║ ██╔╝██╔══██╗██╔═══██╗╚══██╔══╝
    ███████╗██║  ██║█████╗  ███████╗█████╔╝ ██████╔╝██║   ██║   ██║   
    ╚════██║██║  ██║██╔══╝  ╚════██║██╔═██╗ ██╔══██╗██║   ██║   ██║   
    ███████║██████╔╝███████╗███████║██║  ██╗██████╔╝╚██████╔╝   ██║   
    ╚══════╝╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝    ╚═╝
                Minha ferramenta para automação de chamados
                           Python é foda.'''
        print(Fore.CYAN+banner)
    
    def main(self):
        os.system('cls')
        self.banner()
        
        if not self.verificar_conexao():
            print(Fore.RED + '[!] Sem conexão com internet')
            return
        
        if not self.args.tipo and not self.args.equipa:
            self.menu.criar_menu()
        else:
            try:
                print(Fore.RED+'[!] Aguarde, estou inicando')
                bot = chamados.Bot(self.args.tipo, self.args.equipa)
                bot.login(self.user, self.password)
                bot.criar_chamado()
                print(Fore.GREEN    +'[!] Chamado aberto e pronto para ser resolvido')
                self.logg.criar_log(self.args.tipo, self.args.equipa)
            except Exception:
                print(Fore.RED+'[!] Algum erro impediu o funcinamento da automação')

if __name__ == '__main__':
    control = Controller()
    control.main()