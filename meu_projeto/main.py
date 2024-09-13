from modelos.abstract.funcionarios import Funcionarios
from modelos.endereco import Enderecos
from modelos.enums.sexo import Sexo
from modelos.enums.setor import Setores

class Motoboys(Funcionarios):
    
    def __init__(self, nome: str, telefone: str, email: str, endereco: Enderecos, cpf: str, rg: str, dataNascimento: str, sexoNome: Sexo, sexoSigla: Sexo, matricula: str, setor: Setores, salario: float) -> None:
        super().__init__(nome, telefone, email, endereco, cpf, rg, dataNascimento, sexoNome, sexoSigla, matricula, setor, salario)

    def __str__(self) -> str:
        f"\nMotoboy: \nNome: {self.nome} \nCPF: {self.cfp} \nRG: {self.rg} \nTelefone: {self.telefone} \nEmail: {self.email} \nMatrícula: {self.matricula} \nData de Nascimento: {self.dataNascimento} \nSexo: {self.sexoNome} / {self.sexoSigla} \nSetor: {self.setor} \nSalário: R$ {self.salario} \n\nEndereço: \n{self.endereco}" 

#Instanciando
motoboy = Motoboys("Stive", "99866-99", "stive22@hotmail.com", Enderecos, "775.866-88", "56.7457755-88", "02/04/2006", Sexo.MASCULINO.nome, Sexo.MASCULINO.sigla, "566563-567", Setores.SAUDE.name, 3500.90)

print(motoboy)

#Não conseguir terminar.