from abc import ABC, abstractmethod
from modelos.endereco import Enderecos
from modelos.enums.sexo import Sexo
from modelos.abstract.pessoas import Pessoas

class Fisica(Pessoas, ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Enderecos, cpf: str, rg: str, dataNascimento: str, sexoNome: Sexo, sexoSigla: Sexo) -> None:
        super().__init__(nome, telefone, email, cpf, rg, dataNascimento, sexoNome, sexoSigla, endereco)
        self.cfp = cpf
        self.rg = rg
        self.dataNascimento = dataNascimento
        self.sexoNome = sexoNome
        self.sexoSigla = sexoSigla

    def __str__(self) -> str:
        f"{super} \nCPF {self.cpf} \nRG: {self.rg} \nData de Nascimento: {self.dataNacimento} \nSexo {self.sexoNome} / {self.sexoSigla}"