from modelos.endereco import Enderecos
from modelos.enums.sexo import Sexo
from modelos.abstract.fisica import Fisica

class Clientes(Fisica):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Enderecos, cpf: str, rg: str, dataNascimento: str, sexoNome: Sexo, sexoSigla: Sexo, protocoloAtendimento: int) -> None:
        super().__init__(nome, telefone, email, endereco, cpf, rg, dataNascimento, sexoNome, sexoSigla)

        self.protocoloAtendimento = protocoloAtendimento

    def __str__(self) -> str:
        f"\nCliente: \nNome: {self.nome} \nData de Nascimento: {self.dataNascimento} \nCPF: {self.cfp} \nRG: {self.rg} \nTelefone: {self.telefone} \nEmail: {self.email} \nSexo: {self.sexoNome} / {self.sexoSigla} \nProtocolo de Atendimento: {self.protocoloAtendimento} \n\nEndereço: \n{self.endereco}"
