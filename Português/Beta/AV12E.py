# V.A.C.S
# Versão Beta
# Programado por: João Victor Pereira Cavalcanti e Anderson Cortez Calderini

import matplotlib.pyplot as plot

def tori(v0,acel,d_s):
    return ((v0**2)+acel*2*d_s)**0.5
    #v^2 = v0^2 + 2aΔS
    #retorno ta em m/s

def coulomb(q1,q2,dist):
    k = 9 * (10**9)
    return k*((q1*q2)/(dist**2))

def nova_distancia(o_dist,ini_vel,tempo,acel):
    at2 = (acel*(tempo**2))/2
    return o_dist + (ini_vel*tempo) + at2
    #S = S0 + Vo*T + AT^2/2

def v0at(v0,acel,instante):
    return v0 + acel*instante

continuar = 1
while continuar:
    q1 = float(input("Insira a Carga do corpo 1 em Coulomb: "))
    q2 = float(input("Insira a Carga do corpo 2 em Coulomb: "))
    q1exp = int(input("Insira o valor do expoente da carga 1 em notação científica: "))
    q2exp = int(input("Insira o valor do expoente da carga 2 em notação científica: "))
    q1 = q1*(10**q1exp)
    q2 = q2*(10**q2exp)
    print("")
    ini_dist = float(input("Insira a distância inicial em metros: "))
    distexp = int(input("Insira o valor do expoente da distância em notação científica: "))
    ini_dist = ini_dist*(10**distexp)
    print("")
    massa = float(input("Insira o valor da massa do objeto que se move em Kg: "))
    massaexp = int(input("Insira o valor do expoente da massa em notação científica: "))
    massa = massa*(10**massaexp)
    print("")

    p1 = 0
    p2 = ini_dist
    _perc = 0

    _vel = float(input("Insira a velocidade inicial do corpo em movimento em m/s: "))
    print("")
    pf = float(input("Insira o deslocamento final do movimento: "))
    exppf = int(input("Insira o valor do expotente do deslocamento final do movimento: "))
    pf = pf*(10**exppf)
    print("")
    TI = float(input("Insira a quantidade de instantes dentro de um segundo: "))
    TI = 1/TI
    dists = []
    vels = []
    acels = []
    print("")

    i = 0
    while p1 < pf:
        _dist = abs(p2 - p1)
        _f = coulomb(q1,q2,_dist)
        _acel = _f/massa
        _perc = nova_distancia(_perc,_vel,TI,_acel)
        _vel = v0at(_vel,_acel,TI)
        i += 1
        p1 = _perc
        dists.append(p1)
        vels.append(_vel)
        acels.append(_acel)
        print(f"\nInstante {i}:\n\tPosicao de p1 = {p1}\n\tTempo = {round(TI*i,5)} seg\n\tDistancia entre p1 e p2 = {abs(p2 - p1)}\n\tAceleração: {_acel}\n\tVelocidade: {_vel}")
    printvals = int(input("Digite 1 para baixar os valores de espaço: "))
    if(printvals == 1):
        arquivo = str(input("Defina o nome do documento para salvar os valores de espaço: "))
        arquivo = arquivo + ".txt"
        str1 = ', '.join(str(e) for e in dists)
        with open(arquivo, "w") as opfile:
            opfile.write("".join(str1))
    printgraph = int(input("Digite 1 para exibir o gráfico de espaço: "))
    if(printgraph == 1):
        xpoints = []
        i = 0
        while i < len(dists):
            xpoints.append(i)
            i = i + 1
        plot.plot(xpoints, dists)
        plot.show()
    printvals = int(input("Digite 1 para baixar os valores de velocidade: "))
    if(printvals == 1):
        arquivo = str(input("Defina o nome do documento para salvar os valores de velocidade: "))
        arquivo = arquivo + ".txt"
        str1 = ', '.join(str(e) for e in vels)
        with open(arquivo, "w") as opfile:
            opfile.write("".join(str1))
    printgraph = int(input("Digite 1 para exibir o gráfico de velocidade: "))
    if(printgraph == 1):
        xpoints = []
        i = 0
        while i < len(vels):
            xpoints.append(i)
            i = i + 1
        plot.plot(xpoints, vels)
        plot.show()
    printvals = int(input("Digite 1 para baixar os valores de aceleração: "))
    if(printvals == 1):
        arquivo = str(input("Defina o nome do documento para salvar os valores de aceleração: "))
        arquivo = arquivo + ".txt"
        str1 = ', '.join(str(e) for e in acels)
        with open(arquivo, "w") as opfile:
            opfile.write("".join(str1))
    printgraph = int(input("Digite 1 para exibir o gráfico de aceleração: "))
    if(printgraph == 1):
        xpoints = []
        i = 0
        while i < len(acels):
            xpoints.append(i)
            i = i + 1
        plot.plot(xpoints, acels)
        plot.show()
    continuar = int(input("digite 1 para continuar e 0 para sair: "))
