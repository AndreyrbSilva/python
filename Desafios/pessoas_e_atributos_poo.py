# Desafio 1: Criar a classe Pessoa com os atributos nome e idade
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Desafio 2: Adicionar o método apresentar na classe Pessoa
    def apresentar(self):
        return f"Seja bem-vindo ao SENAC, {self.nome}!"

# Desafio 1: Criar a classe PessoaFisica com os atributos nome, idade e CPF
class PessoaFisica(Pessoa):  # PessoaFisica herda da classe Pessoa
    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade)  # Reutiliza o construtor da classe base
        self.cpf = cpf

    # Desafio 2: Sobrescrever o método apresentar na classe PessoaFisica
    def apresentar(self):
        return f"Seja bem-vindo ao SENAC, {self.nome}! Seu CPF é {self.cpf}."

# Desafio 1: Criar a classe PessoaJuridica com os atributos nome, idade e CNPJ
class PessoaJuridica(Pessoa):  # PessoaJuridica herda da classe Pessoa
    def __init__(self, nome, idade, cnpj):
        super().__init__(nome, idade)  # Reutiliza o construtor da classe base
        self.cnpj = cnpj

    # Desafio 2: Sobrescrever o método apresentar na classe PessoaJuridica
    def apresentar(self):
        return f"Seja bem-vindo ao SENAC, {self.nome}! Seu CNPJ é {self.cnpj}."

# Testando as classes e métodos
pessoa = Pessoa("Carlos", 30)
print(pessoa.apresentar())  # Exibe a mensagem de boas-vindas para Pessoa

pessoa_fisica = PessoaFisica("Ana", 25, "123.456.789-00")
print(pessoa_fisica.apresentar())  # Exibe a mensagem de boas-vindas com CPF

pessoa_juridica = PessoaJuridica("Empresa X", 10, "12.345.678/0001-99")
print(pessoa_juridica.apresentar())  # Exibe a mensagem de boas-vindas com CNPJ
