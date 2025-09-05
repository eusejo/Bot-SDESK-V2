import logging
import os

class Logs:
    def criar_log(self, servico, equipamento):
        logs_dir = r'G:\Meu Drive\Bot-Sdesk V2\loggs'
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir, exist_ok=True)
        logs_path = os.path.join(logs_dir, 'HISTORICO.log')
        
        logging.basicConfig(
                filename=logs_path,
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s - %(message)s'
        )
        try:
            logging.info(f'Chamado criado com sucesso: Serviço={servico}, Equipamento={equipamento}')
        except Exception as e:
            logging.error(f'erro ao criar chamado {e}')