from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from time import sleep

class Bot:
    def __init__(self, servico, equipa):
        self.options = Options()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])        
        self.chrome = webdriver.Chrome(options=self.options)
        self.descricao = 'Por favor, realizar a inspeção dos seguintes equipamentos especificados acima e identificar o estado do próprio.'
        self.servico = servico
        self.equipa = equipa
        self.equipamentos = {
            'D' : '/html/body/div[2]/div/div/main/div[1]/form/ol/li[2]/div[2]/div[1]/div/div/div/div[1]/span/input',
            'M' : '/html/body/div[2]/div/div/main/div[1]/form/ol/li[2]/div[2]/div[1]/div/div/div/div[2]/span/input',
            'N' : '/html/body/div[2]/div/div/main/div[1]/form/ol/li[2]/div[2]/div[1]/div/div/div/div[3]/span/input',
            'No' : '/html/body/div[2]/div/div/main/div[1]/form/ol/li[2]/div[2]/div[1]/div/div/div/div[4]/span/input'
        }
        
    def patri(self):
        with open(r'G:\Meu Drive\Bot-Sdesk V2\patrimonios\patri.txt', 'r') as arq:
            return [line.strip() for line in arq]
    
    def login(self, user, password):
        self.chrome.get('https://sdeskcloud.com.br/index.php?noAUTO=1')
        self.chrome.maximize_window()
        login = self.chrome.find_element(By.ID, "login_name")
        user_password = self.chrome.find_element(By.ID, "login_password")
        botao = self.chrome.find_element(By.NAME, 'submit')
        
        login.send_keys(user)
        user_password.send_keys(password)
        botao.click()
        sleep(1)
        
    def criar_chamado(self):
        self.chrome.get('https://sdeskcloud.com.br/marketplace/formcreator/front/formdisplay.php?id=5')
        sleep(1)
        selecionar = self.chrome.find_element(By.XPATH, r'/html/body/div[2]/div/div/main/div[1]/form/ol/li[1]/div[2]/div/div/div/select')
        opcoes = Select(selecionar)
        opcoes.select_by_index(self.servico)
        sleep(0.5)
        if self.servico in [1,3,4]:
            self.inspecoes()
        
    def inspecoes(self):
        equipamento = self.chrome.find_element(By.XPATH, rf'{self.equipamentos.get(self.equipa)}')
        equipamento.click()
        
        patris = self.patri()
        lista_formatada = [item.strip("'\"") for item in patris]
        patrimonios = ', '.join(lista_formatada)
        
        patrimonio = self.chrome.find_element(By.XPATH, r'/html/body/div[2]/div/div/main/div[1]/form/ol/li[2]/div[2]/div[3]/div/div/input')
        patrimonio.send_keys(patrimonios)
        
        descri = self.chrome.find_element(By.XPATH, r'/html/body/div[2]/div/div/main/div[1]/form/ol/li[2]/div[2]/div[5]/div/div/input').send_keys(self.descricao)
        self.chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(0.5)
        enviar = self.chrome.find_element(By.NAME, 'add')
        enviar.click()
        sleep(1)