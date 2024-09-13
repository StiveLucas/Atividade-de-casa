from modelos.endereco import Enderecos
from modelos.enums.sexo import Sexo
from modelos.abstract.fisica import Fisica
from modelos.enums.setor import Setores

class Funcionarios(Fisica):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Enderecos, cpf: str, rg: str, dataNascimento: str, sexoNome: Sexo, sexoSigla: Sexo, matricula: str, setor: Setores, salario: float) -> None:
        super().__init__(nome, telefone, email, cpf, rg, dataNascimento, sexoNome, sexoSigla, endereco)

        self.matricula = matricula
        self.setor = setor
        self.salario = salario

    def __str__(self) -> str:
        f"Nome: {self.nome} Data de Nascimento: {self.dataNascimento} \nCPF: {self.cfp} \nRG: {self.rg} \nTelefone: {self.telefone} \nEmail: {self.email} \nSexo: {self.sexoNome.value} / {self.sexoSigla} \nSalário: R$ {self.salario}"