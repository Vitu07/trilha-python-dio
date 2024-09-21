menu = """
   
   [1] Depositar
   [2] Sacar
   [3] Extrato
   [0] Sair

=> """

saldo = 0
limite = 500 
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Valor de deposito inválido, informe valor válido")


    elif opcao == "2":
        valor = float(input("Digite o valor que deseja sacar: "))

        excedeu_limite = valor > 500
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Saldo insuficiente.")

        elif excedeu_limite:
            print("O valor por operação de saque é até : R$ 500, 00.")
        
        elif excedeu_saques:
            print("Número de saques diários excedidos.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Valor de saque inválido, informe valor valído.")

        
    elif opcao == "3":
        print(" EXTRATO ".center(71, "="))
        print("Nenhuma transação realizada" if not extrato else extrato)
        print(f"\nSaldo dispinível: R$ {saldo:.2f}")
        print("=======================================================================")



    elif opcao == "0":
        print("Obrigado pela preferencia, volte sempre!!!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        

     
