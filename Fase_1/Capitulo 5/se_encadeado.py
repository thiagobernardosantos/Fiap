...
print(f"""
0 - SAIR
1 - Cadastrar cliente
2 - Consultar clientes
3 - Editar Cliente
4 - Inativar cliente
""")
opcao = int(input("Escolha: "))
if opcao == 0:
    print("Encerrando o sistema")
elif opcao == 1:
    print("...\n[rotina de cadastro de clientes]...\n")
elif opcao == 2:
    print("...\n[rotina de consulta de clientes]...\n")
elif opcao == 3:
    print("...\n[rotina de edição de clientes]...\n")
elif opcao == 3:
    print("...\n[rotina de Inativação de clientes]...\n")
else:
    print("Opção inválida!")
...
