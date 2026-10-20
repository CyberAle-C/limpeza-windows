from limpeza import executar_limpeza

while True:
    print("\n[1] Limpeza do Windows")
    print("[2] Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        executar_limpeza()
    elif opcao == "2":
        break
    else:
        print("Opção inválida.")
