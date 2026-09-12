variáveis
    idade: inteiro
    rm: alfanumérico
    autorizado: caractere
início
    Escreva “Por favor, digite seu nome”
    Leia rm
    Escreva “Por favor, digite sua idade”
    Leia idade
    Se idade >=18 então
        Escreva “Sua participação foi autorizada, aluno de RM”, rm
        Escreva “Mais instruções serão enviadas ao seu e-mail cadastrado na FIAP!”
    Senão
        Escreva “Você possui autorização dos responsáveis para participar? S – SIM ou N – NÃO”
        Leia autorizado
        Se autorizado = “S” então
            Escreva “Sua participação foi autorizada, aluno de RM”, rm
            Escreva “Mais instruções serão enviadas ao e-mail dos seus responsáveis”
        Senão
            Escreva “Sua participação não foi autorizada por causa da sua idade”
        Fim_se
    Fim_se
Fim
