# Camada de Coleta de Dados
class ColetaDados:
    def __init__(self, fonte_dados):
        self.fonte_dados = fonte_dados
        self.dados_brutos = None

    def coletar_dados(self):
        try:
            # Simulação de coleta de dados a partir de uma fonte externa (por exemplo, arquivo CSV)
            self.dados_brutos = pd.read_csv(self.fonte_dados)
        except Exception as e:
            raise Exception(f"Falha na coleta de dados: {str(e)}")