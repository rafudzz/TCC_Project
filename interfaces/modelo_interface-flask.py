# Interface Externa (Flask)
app = Flask(__name__)

@app.route('/')
def interface_externa():
    try:
        # Simulação de interação com a interface externa
        coleta = ColetaDados('dados_externos.csv')
        coleta.coletar_dados()

        validacao = ValidacaoDados()
        validacao.validar_dados(coleta.dados_brutos)

        gerenciamento = GerenciamentoDados()
        gerenciamento.gerenciar_dados(validacao.dados_validos, validacao.dados_invalidos)

        armazenamento = ArmazenamentoDados()
        armazenamento.conectar_banco_dados()
        armazenamento.armazenar_dados(gerenciamento.dados_corrigidos)

        return 'Dados coletados, validados, gerenciados e armazenados com sucesso!'
    except Exception as e:
        return f'Erro: {str(e)}'