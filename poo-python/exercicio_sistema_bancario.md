# 💼 Exercício Prático: Sistema Bancário em Python

## 🎯 Objetivo
Desenvolver um sistema simples de banco utilizando conceitos de orientação a objetos em Python, praticando:
- Criação de classes e objetos
- Uso de atributos de instância e de classe
- Métodos de instância
- Composição (um banco possui várias contas)
- Manipulação de listas de objetos

---

## 📋 Enunciado

Implemente um sistema bancário com as seguintes características:

### 1. **Classe ContaBancaria**
Cada conta bancária deve possuir:
- **Atributos:**
  - `titular`: nome do cliente (string)
  - `numero`: número da conta (inteiro, gerado automaticamente e único para cada conta)
  - `saldo`: valor atual da conta (float, inicia em 0)
- **Métodos:**
  - `depositar(valor)`: adiciona o valor ao saldo, apenas se o valor for positivo.
  - `sacar(valor)`: subtrai o valor do saldo, apenas se houver saldo suficiente e o valor for positivo.
  - `exibir_saldo()`: imprime o saldo atual da conta.

> **Dica:** Use um atributo de classe para gerar automaticamente o número da conta, incrementando a cada nova conta criada.

---

### 2. **Classe Banco**
O banco deve possuir:
- **Atributos:**
  - `nome`: nome do banco (string)
  - `lista_contas`: lista de objetos do tipo `ContaBancaria`
- **Métodos:**
  - `criar_conta(titular)`: cria uma nova conta para o titular informado, adiciona à lista de contas e retorna o objeto da conta criada.
  - `exibir_contas()`: imprime todas as contas do banco, mostrando número, titular e saldo.
  - `total_contas()`: retorna o número total de contas criadas no banco.
  - `total_valor_em_contas()`: retorna a soma de todos os saldos das contas do banco.

---

### 3. **Simulação**
Implemente, ao final do arquivo, um bloco de simulação (dentro de `if __name__ == "__main__":`) que:
- Crie um banco
- Crie pelo menos três contas com titulares diferentes
- Realize depósitos e saques em cada conta (inclua pelo menos um saque com saldo insuficiente)
- Exiba o saldo de cada conta
- Liste todas as contas do banco
- Mostre o total de contas e o valor total em todas as contas

---

## 📝 Regras e Dicas
- Use nomes de variáveis e métodos claros e descritivos.
- Implemente mensagens informativas para operações inválidas (ex: saque sem saldo).
- Não utilize bibliotecas externas, apenas recursos básicos do Python.
- O código deve estar todo em um único arquivo `.py`.

---

## 🚀 Desafio Extra (opcional)
- Implemente um método para transferir dinheiro entre duas contas do mesmo banco.