nome = input("Escreva aqui o nome do aparelho: ")
potencia = float(input("Escreva aqui o número da potência em watts do aparelho: "))
tempo = float(input("Escreva aqui o número do tempo médio de uso diário em horas: "))
consumo_mensal = (potencia * tempo * 30) / 1000
print (f"\n Aparelho: {nome} ")
print (f"\n Consumo estimado: {consumo_mensal} kWh/mês ")