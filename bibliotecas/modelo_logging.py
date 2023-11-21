# Logging
class Logging:
    def __init__(self, log_file='log.txt'):
        self.log_file = log_file

    def registrar_evento(self, mensagem):
        try:
            # Simulação de registro em arquivo de log
            with open(self.log_file, 'a') as f:
                f.write(f'{mensagem}\n')
        except Exception as e:
            raise Exception(f"Falha no registro de eventos: {str(e)}")