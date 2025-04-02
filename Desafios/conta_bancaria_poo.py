## Criando a classe

class ContaBancaria:
  def __init__(self, numero_conta, titular, saldo = 0):
    ## Atributos privadod
    self.__numero_conta = numero_conta
    self.__titular = titular
    self.__saldo = saldo

## Função para consultar o saldo
  def consultar_saldo(self):
    return f"Seu saldo atual é de: R${self.__saldo}"

## Função para depositar
  def depositar(self, valor):
    ## Permitir que apenas valores acima de 0 seja possível depositar
    if valor > 0:
      self.__saldo += valor
      return f"Valor de R${valor} foi depositado com sucesso.\n{self.consultar_saldo()}"
    ## Caso digite 0 ou valor negativos
    else:
      return "Não foi possível depositar, valor informado inválido!"

## Função para sacar
  def sacar(self, valor):
    ## Verificar se o número é maior que 0
    if valor > 0:
      ## Verifica se o valor digitado é menor ou igual o saldo, se sim decrementa
      if valor <= self.__saldo:
        self.__saldo -= valor
        return f"Valor de R${valor} foi sacado com sucesso.\n{self.consultar_saldo()}"
      ## Se não, ocorre erro
      else:
        return "Saldo insuficiente para o saque!"
    ## Erro caso o valor digitado seja negativo ou 0
    else:
      return "Valor negativo ou 0 digitado, digite um valor válido!"

###### TESTES ######

pessoa1 = ContaBancaria(numero_conta = 124248, titular = "Andrey", saldo = 0)

## Consulta o saldo inicial | 0
print(pessoa1.consultar_saldo())
print("")
## Deposita R$8 na conta
print(pessoa1.depositar(8))
print("")
## Saca R$3 da conta
print(pessoa1.sacar(3))
print("")

## TESTE DE ERRO ##
## Tenta sacar mais do que tem na conta
print(pessoa1.sacar(10))
print("")
## Tenta depositar e sacar valores negativos
print(pessoa1.depositar(-10))
print("")
print(pessoa1.sacar(-10))

## Pilar

## O código usa o Encapsulamento para proteger os dados da
## classe ContaBancaria, como o saldo, que é privado e só pode ser acessado 
## ou modificado pelos métodos da própria classe. 
## Isso garante que só ações válidas, como depósitos ou saques 
## dentro das regras, possam alterar o saldo. Assim, tudo fica
## mais organizado, seguro e fácil de usar, sem permitir
## alterações diretas que poderiam causar problemas. 

## VEÍCULO ##

from abc import ABC, abstractmethod

# Parte 1: Abstração
# --------------------
# Classe abstrata Veiculo
# Representa um veículo genérico com atributos e métodos abstratos
class Veiculo(ABC):
    def __init__(self, marca, modelo, velocidade=0):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade

    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frear(self):
        pass

    @abstractmethod
    def mostrar_velocidade(self):
        pass

# Parte 2: Herança
# --------------------
# Classe Carro que herda de Veiculo
# Adiciona o atributo tipo_combustivel e implementa os métodos abstratos
class Carro(Veiculo):
    def __init__(self, marca, modelo, velocidade=0, tipo_combustivel="Diesel"):
        super().__init__(marca, modelo, velocidade)
        self.tipo_combustivel = tipo_combustivel

    def acelerar(self):
        self.velocidade += 10
        return "O carro está acelerando..."

    def frear(self):
        self.velocidade = max(0, self.velocidade - 10)
        return "O carro freou."

    def mostrar_velocidade(self):
        return f"Velocidade atual do carro: {self.velocidade} km/h"

# Classe Moto que herda de Veiculo
# Adiciona o atributo tipo_combustivel e implementa os métodos abstratos
class Moto(Veiculo):
    def __init__(self, marca, modelo, velocidade=0, tipo_combustivel="Gasolina"):
        super().__init__(marca, modelo, velocidade)
        self.tipo_combustivel = tipo_combustivel

    def acelerar(self):
        self.velocidade += 15
        return "A moto está acelerando..."

    def frear(self):
        self.velocidade = max(0, self.velocidade - 15)
        return "A moto freou."

    def mostrar_velocidade(self):
        return f"Velocidade atual da moto: {self.velocidade} km/h"

# Parte 3: Polimorfismo
# --------------------
# Função que testa qualquer objeto que herde de Veiculo
# Mostra o comportamento dos métodos acelerar, frear e mostrar_velocidade
def teste_veiculo(veiculo):
    print(veiculo.acelerar())
    print(veiculo.acelerar())
    print(veiculo.mostrar_velocidade())
    print(veiculo.frear())
    print(veiculo.mostrar_velocidade())

# Teste do polimorfismo com Carro e Moto
print("Testando um carro:\n")
carro1 = Carro("Toyota", "Corolla")
teste_veiculo(carro1)

print("\nTestando uma moto:\n")
moto1 = Moto("Honda", "Titan 160")
teste_veiculo(moto1)

# Parte 4: Composição
# --------------------
# Classe Motor
# Representa um motor com o atributo potencia
class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

# Modificação na classe Carro para incluir um motor
# Adiciona o atributo motor como uma instância da classe Motor
class Carro(Veiculo):
    def __init__(self, marca, modelo, velocidade=0, tipo_combustivel="Gasolina", potencia_motor=100):
        super().__init__(marca, modelo, velocidade)
        self.tipo_combustivel = tipo_combustivel
        self.motor = Motor(potencia_motor)  # Composição: Carro tem um Motor

    def acelerar(self):
        self.velocidade += 10
        return "O carro está acelerando..."

    def frear(self):
        self.velocidade = max(0, self.velocidade - 10)
        return "O carro freou."

    def mostrar_velocidade(self):
        return f"Velocidade atual do carro: {self.velocidade} km/h"

    def mostrar_potencia_motor(self):
        return f"Potência do motor: {self.motor.potencia} CV"

# Teste da composição
print("\nTestando composição no carro:\n")
carro2 = Carro("Ford", "Focus", potencia_motor=140)
print(carro2.acelerar())
print(carro2.mostrar_velocidade())
print(carro2.mostrar_potencia_motor())

## Pilares

## 1. Abstração:
## A classe Veiculo representa o conceito geral de um veículo, com atributos 
## e métodos que todo veículo deve ter, mas sem entrar nos detalhes de como
## cada um funciona. Os métodos abstratos (acelerar, frear, mostrar_velocidade)
## obrigam as subclasses a definir seus próprios comportamentos.

## 2. Herança:
## As classes Carro e Moto são especializações de Veiculo, ou seja, elas herdam
## tudo o que é genérico e ainda adicionam suas próprias características, como o 
## tipo de combustível. Isso evita repetir código e organiza bem o que é comum e o 
## que é específico.

## 3. Polimorfismo:
## O polimorfismo aparece na função teste_veiculo, que funciona tanto para Carro 
## quanto para Moto. Mesmo sendo tipos diferentes, ambos têm os métodos acelerar, frear e 
## mostrar_velocidade, e o comportamento muda dependendo de qual veículo está sendo testado.

## 4. Composição:
## A composição é usada na relação entre Carro e Motor. Aqui, o Carro tem um atributo
## chamado motor, que é uma instância da classe Motor. Isso significa que o carro não
## herda as características do motor, mas usa ele como parte do seu funcionamento, como no caso
## de mostrar a potência.
