credito = 800.0
saques_realizados = 0
total_depositado = 0
total_sacado = 0


while True:
    escolha = int(input(""" 
        ============================
        BEM VINDO AO BANCO DO BRASIL
        ============================
            
        Escolha uma das opções:
                
        1- Saque
        2- Depósito
        3- Extrato
        4- Sair
        """))
    
    if escolha == 1:
        valor_saque = float(input("""
        =================================
        VOCÊ ESCOLHEU A OPÇÃO DE SAQUE!!!
        =================================
                
        Informe o valor do saque:
        """))

        if valor_saque > 500:
            print("VOCÊ NÃO PODE SACAR UM VALOR SUPERIOR A R$500.00")

        elif saques_realizados >= 3:
            print("LIMITE DE SAQUES EXCEDIDO")

        elif valor_saque > credito:
            print("VOCÊ NÃO PODE SACAR UM VALOR SUPERIOR AOS SEUS CRÉDITOS BANCÁRIOS")
        else:
            credito -= valor_saque
            saques_realizados += 1
            total_sacado += valor_saque
            print(f"SAQUE REALIZADO COM SUCESSO, NO VALOR DE R${valor_saque:.2f}")

    elif escolha == 2:
        valor_deposito = float(input("""
        ====================================
        VOCÊ ESCOLHEU A OPÇÃO DE DEPÓSITO!!!
        ====================================
                    
        Informe o valor do depósito:
        """))

        if valor_deposito <= 0:
            print("NÃO FOI POSSÍVEL REALIZAR A OPERAÇÃO")

        else:
            credito += valor_deposito
            total_depositado += valor_deposito
            print(f"DEPÓSITO REALIZADO COM SUCESSO, NO VALOR DE R${valor_deposito:.2f}")

    elif escolha == 3:
        print("""
        =======================================================
        VOCÊ ESCOLHEU A OPÇÃO DE VISUALIZAR EXTRATO BANCÁRIO!!!
        =======================================================
        """)
        print(f"Você sacou um total de R${total_sacado:.2f} e depositou um total de R${total_depositado:.2f} na sua conta.")
        print(f"Saldo atual: R${credito:.2f}")

    elif escolha == 4:
        print("Obrigado por usar o Banco do Brasil! Até a próxima.")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")