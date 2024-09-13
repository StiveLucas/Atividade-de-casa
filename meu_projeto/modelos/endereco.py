from modelos.enums.unidade_federativa import UnidadeFederativa

class Enderecos():
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str, ufnome: UnidadeFederativa, ufsigla: UnidadeFederativa) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.ufnome = ufnome
        self.ufsigla = ufsigla

    def __str__(self) -> str:
        f"\nLogradouro: {self.logradouro} \nNúmero: {self.numero} \nComplemento: {self.complemento} \nCEP: {self.cep} \nUF: {self.ufnome} / {self.ufsigla}"
