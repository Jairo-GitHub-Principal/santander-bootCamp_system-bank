
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
    entrada = (input(menu)) # aceita qualquer valor que seja digitado

    try:     
        option = int(entrada) # se o vlor for difenrente de int ele vai dar erro, então ele captura o erro e executa o except e não quebra o programa isso por causa do try e except
       
        if option == 1:
            print("Deposito")
            deposito = float(input("Informe o valor do depósito: "))

            if deposito > 0:
                print("Operação falhou! O valor informado é inválido.")

                saldo += deposito
                extrato += f"Depósito: R$ {deposito:.2f}\n"
            else:
                print("Operação falhou! O valor informado é menor ou igual a zero.")
            
        elif option == 2:
            print ("Saque")
            saque = float(input("Informe o valor do saque: "))

            if numero_saques >= LIMITE_SAQUES:
                print("Operação falhou! Número máximo de saques excedido.") 

            elif saque > limite:
                print("Operação falhou! O valor do saque excede o limite.")    
            
            elif saque > saldo:
                print("Operação falhou! Vocês não tem saldo suficiente.")          

            elif saque > 0:
                saldo -= saque
                numero_saques += 1
                extrato += f"{numero_saques}°  Saque: R$ {saque:.2f} \n"
                
        elif option == 3:
            print("\n================ EXTRATO ================")
            if not extrato:
                print("Não foram realizadas movimentações.") 
                print(f"\n {extrato} \nSaldo: R$ {saldo:.2f}")
            else :     
                print(f"\n {extrato} \nSaldo: R$ {saldo:.2f}")
                

            
            print("==========================================")
        elif option == 0:
            break    
        else:
            print("Opção inválida")
        
    except ValueError:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
