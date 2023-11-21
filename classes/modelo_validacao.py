# Camada de Validação de Dados
class ValidacaoDados:
    def __init__(self):
        self.dados_validos = None
        self.dados_invalidos = None

    def validar_dados(self, dados):
        try:
            # Simulação de validação de dados
            dados['Receita'] = pd.to_numeric(dados['Receita'], errors='coerce')
            self.dados_validos = dados.dropna(subset=['Receita'])
            self.dados_invalidos = dados[~dados.index.isin(self.dados_validos.index)]
        except Exception as e:
            raise Exception(f"Falha na validação de dados: {str(e)}")