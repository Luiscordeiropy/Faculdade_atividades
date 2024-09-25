class MeuErroPersonalizado(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem

try:
    raise MeuErroPersonalizado("ocorreu um erro personalizado.")
except MeuErroPersonalizado as e:
    print("Erro personalizado: ", e.mensagem)