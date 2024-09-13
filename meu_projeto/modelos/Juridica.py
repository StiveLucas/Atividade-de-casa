from modelos.endereco import Enderecos
from modelos.abstract.pessoas import Pessoas

class Juridiricas(Pessoas):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Enderecos, cnpj: str, inscricaoEstadual: str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj
        self.inscricaoEstadual = inscricaoEstadual