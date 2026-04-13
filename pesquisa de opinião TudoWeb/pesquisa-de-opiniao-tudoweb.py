Excelente = 0
Ruim = 0
for i in range(1, 51):
    print("Para fazer a pesquisa de opinião, informe: ")
    nome = input("Qual o seu nome: ")
    idade = input("Qual a sua idade: ")
    opiniao = input("Qual seu nível de satisfação com o atendimento, entre as opções: Excelente, Bom e Ruim: ")
    if opiniao == "Excelente":
        Excelente += 1
    elif opiniao == "Ruim":
        Ruim += 1
print (f"O resultado das pesquisas mostra que {Excelente} cliente(s) acham o atendimento excelente e {Ruim} cliente(s) acham o atendimento ruim")