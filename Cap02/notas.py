def media(vetor, horas):
    
    media = 0

    for num in vetor:
        media += num

    media /= len(vetor)
    return media * horas


total_periodos = [10, 7.5, 9.1, 9.7, 10, 8.8, 9.10, ]

########## 1 Período ##########
horas1 = [90, 60, 60, 60, 15, 60]

alg1 = media([], horas1[0])
gestao = media([], horas1[1])
logica = media([], horas1[2])
metodologia = media([], horas1[3])
introducao = media([], horas1[4])
si1 = media([], horas1[5])

periodo1 = alg1 + gestao + logica + metodologia + introducao + si1

total_periodos.append(periodo1)

########## 2 Período ##########
horas2 = [90, 60, 60, 60, 60, 30, 60]

alg2 = media([], horas2[0])
calculo = media([], horas2[1])
circuitos = media([], horas2[2])
empreendedorismo = media([], horas2[3])
discreta = media([], horas2[4])
prolog = media([], horas2[5])
si2 = media([], horas2[6])

periodo2 = alg2 + calculo + circuitos + empreendedorismo + discreta + prolog + si2

total_periodos.append(periodo2)

########## 3 Período ##########
horas3 = [60, 60, 60, 60, 60, 60, 60]
# horas3 = [0, 60, 0, 60, 0, 60, 60]

arquitetura = media([], horas3[0])
bd1 = media([], horas3[1])
engenharia1 = media([], horas3[2])
estatistica = media([], horas3[3])
ed1 = media([], horas3[4])
poo1 = media([], horas3[5])
so = media([], horas3[6])

periodo3 = arquitetura + bd1 + engenharia1 + estatistica + ed1 + poo1 + so
# periodo3 = bd1 + estatistica + poo1 + so

total_periodos.append(periodo3)

########## Cálculo ##########
IRA = sum(total_periodos)
IRA /= sum(horas1) + sum(horas2) + sum(horas3)

print(f"IRA isolado do 1º período: {periodo1 / sum(horas1)}")
print(f"IRA isolado do 2º período: {periodo2 / sum(horas2)}")
print(f"IRA isolado do 3º período: {periodo3 / sum(horas3)}")
print(f"IRA final: {IRA}")