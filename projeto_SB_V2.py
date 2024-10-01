def depositar(conta, valor):
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"] += f"Deposito: R$ {valor:.2f}\n"
    else:
        print("Valor de deposito inválido, informe valor válido")
    return conta

def sacar(conta, valor, LIMITE_SAQUES, limite):
    excedeu_limite = valor > limite
    excedeu_saques = conta["numero_saques"] >= LIMITE_SAQUES
    excedeu_saldo = valor > conta["saldo"]

    if excedeu_saldo:
        print("Saldo insuficiente.")
    elif excedeu_limite:
        print("O valor por operação de saque é até : R$ 500, 00.")
    elif excedeu_saques:
        print("Número de saques diários excedidos.")
    elif valor > 0:
        conta["saldo"] -= valor
        conta["extrato"] += f"Saque: R$ {valor:.2f}\n"
        conta["numero_saques"] += 1
    else:
        print("Valor de saque inválido, informe valor valído.")
    return conta

def imprimir_extrato(conta):
    print(" EXTRATO ".center(71, "="))
    print("Nenhuma transação realizada" if not conta["extrato"] else conta["extrato"])
    print(f"\nSaldo dispinível: R$ {conta['saldo']:.2f}")
    print("=======================================================================")

def criar_usuario(usuarios):
    cpf = input("Digite o CPF(somente o número) ")
    usuario = filtro_usuario(cpf, usuarios)

    if usuario:
        print("\n ## Usuario já cadastrado! ##")
        return

    nome = input("Informe seu nome: ")
    data_nasc = input("Digite sua data de nascimento(dd/mm/aaaa): ")

    logradouro = input("Digite o logradouro: ")
    nro = input("Informe o numero: ")
    bairro = input("Informe o bairro: ")
    cidade = input("Informe a cidade(pela sigla): ")
    endereco = f"{logradouro} - {nro} - {bairro} - {cidade}"

    usuarios.append({"cpf": cpf, "nome": nome, "data": data_nasc, "endereco": endereco})

    print("+++++ Usuário criado com sucesso!!! +++++")

def filtro_usuario(cpf, usuarios):
    for usuario in usuarios:
      if usuario["cpf"] == cpf:
        return usuario
    return None

def criar_conta(usuarios, contas):
    cpf = input("Digite o CPF do usuario (somente número): ")
    usuario = filtro_usuario(cpf, usuarios)

    if not usuario:
        print("Usuário não encontrado. Por favor, crie um usuário antes")
        return

    numero_conta = len(contas) + 1
    saldo = 0
    extrato = ""
    numero_saques = 0

    conta = {
        "agencia": "0001",
        "numero_conta": numero_conta,
        "cpf": cpf,
        "saldo": saldo,
        "extrato": extrato,
        "numero_saques": numero_saques
    }

    contas.append(conta)

    print("+++++ Conta criada com sucesso!!! +++++")

menu = """
   
   [1] Depositar
   [2] Sacar
   [3] Extrato
   [4] Criar conta
   [5] Criar usuario
   [0] Sair

=> """

def main():
    usuarios = []
    contas = []

    while True:
        opcao = input(menu)

        if opcao == "1":
            cpf = input("Digite o CPF do usuario (somente número): ")
            usuario = filtro_usuario(cpf, usuarios)
            if usuario:
                for conta in contas:
                    if conta["cpf"] == cpf:
                        conta = depositar(conta, float(input("Digite o valor que deseja depositar: ")))
                        break
            else:
                print("Usuário não encontrado. Por favor, crie um usuário antes")

        elif opcao == "2":
            cpf = input("Digite o CPF do usuario (somente número): ")
            usuario = filtro_usuario(cpf, usuarios)
            if usuario:
                for conta in contas:
                    if conta["cpf"] == cpf:
                        conta = sacar(conta, float(input("Digite o valor que deseja sacar: ")), 3, 500)
                        break
            else:
                print("Usuário não encontrado. Por favor, crie um usuário antes")

        elif opcao == "3":
            cpf = input("Digite o CPF do usuario (somente número): ")
            usuario = filtro_usuario(cpf, usuarios)
            if usuario:
                for conta in contas:
                    if conta["cpf"] == cpf:
                        imprimir_extrato(conta)
                        break
            else:
                print("Usuário não encontrado. Por favor, crie um usuário antes")

        elif opcao == "4":
            criar_conta(usuarios, contas)

        elif opcao == "5":
            criar_usuario(usuarios)

        elif opcao == "0":
            print("Obrigado pela preferencia, volte sempre!!!!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
