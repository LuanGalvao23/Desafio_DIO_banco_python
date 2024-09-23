menu = """"

[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

=> """

Saldo = 5000
Limite = 1500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 5

while True:
    
    opção = input(menu)

    if opção == "D":
        valor = float(input("informe o valor do depósitos: "))
        
        if valor > 0:
            Saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            
        else:
            print("Operação falhou! O valor informado é invalido.")

    elif opção == "S":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > Saldo

        excedeu_limite = valor > Limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem o saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print ("Operação falhou! Número de saques excedido.")

        elif valor > 0:
            Saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é invalido.")
    
    elif opção == "E":
        print("\n==================== EXTRATO ====================")
        print("Não foi constatado nenhuma movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {Saldo:.2f}")
        print("=================================================")

    elif opção == "Q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
