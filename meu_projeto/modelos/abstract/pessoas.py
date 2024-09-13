from abc import ABC, abstractmethod
from modelos.endereco import Enderecos

class Pessoas(ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Enderecos) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def __str__(self) -> str:
        f"\nNome: {self.nome} \nTelefone: {self.telefone} \nEmail: {self.email} \n\nEndereço: {self.endereco}"