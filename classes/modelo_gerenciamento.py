# Camada de Gerenciamento de Dados
class GerenciamentoDados:
    def __init__(self):
        self.dados_corrigidos = None

    def gerenciar_dados(self, dados_validos, dados_invalidos):
        try:
            # Simulação de decisões de gerenciamento
            # Neste exemplo, apenas duplicando a receita dos dados válidos
            self.dados_corrigidos = dados_validos.copy()
            self.dados_corrigidos['Receita'] = self.dados_corrigidos['Receita'] * 2
        except Exception as e:
            raise Exception(f"Falha no gerenciamento de dados: {str(e)}")