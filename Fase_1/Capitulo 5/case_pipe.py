...
ano_nascimento = int(input("Ano de nascimento: "))
match ano_nascimento:
    case 2000 | 2001 | 2002:
        print("Entrar na fila 1")
    case 2003 | 2004 | 2005:
        print("Entrar na fila 2")
    case 2006 | 2007 | 2008:
        print("Entrar na fila 3")
    case _:
        print("Entrar na fila 4")
...
