...
print(f"""
0 - SAIR
1 - Cadastrar cliente
2 - Consultar clientes
3 - Editar Cliente
4 - Inativar cliente
""")
opcao = int(input("Escolha: "))

match opcao:
    case 0:
        print("Encerrando o sistema")
    case 1:
        print("...\n[rotina de cadastro de clientes]...\n")
    case 2:
        print("...\n[rotina de consulta de clientes]...\n")
    case 3:
        print("...\n[rotina de edição de clientes]...\n")
    case 4:
        print("...\n[rotina de Inativação de clientes]...\n")
    case _:
        print("Opção inválida!")
...
