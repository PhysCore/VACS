# S.C.A.V
# Versão 2.3.0
# Programador por: João Victor Pereira Cavalcanti e Anderson Cortez Calderini

def tori(v0,acel,d_s):
    return ((v0**2)+acel*2*d_s)**0.5
    #v^2 = v0^2 + 2aΔS
    #retorno ta em m/s

def fgrav(m2,dist):
    g = 6.67408 * (10**-11)
    return g*(m2/(dist**2))

def nova_distancia(o_dist,ini_vel,tempo,acel):
    at2 = (acel*(tempo**2))/2
    return o_dist + (ini_vel*tempo) + at2
    #S = S0 + Vo*T + AT^2/2

def v0at(v0,acel,instante):
    return v0 + acel*instante

continuar = 1
while continuar:
    m2 = float(input("Massa do corpo parado em Kg: "))
    expm2 = int(input("Valor do expoente da massa do corpo parado em notação científica: "))
    m2 = m2*(10**expm2)
    print("")
    ini_dist = float(input("Insira a distancia inicial entre os dois corpos: "))
    expdist = int(input("Insira o valor do expoente da distancia entre os dois corpos: "))
    ini_dist = ini_dist*(10**expdist)
    print("")

    p1 = 0
    p2 = ini_dist
    _vel = 0
    _perc = 0

    pf = float(input("Insira o deslocamento final do movimento: "))
    exppf = int(input("Insira o valor do expotente do deslocamento final do movimento: "))
    pf = pf*(10**exppf)
    print("")
    TI = float(input("Insira a quantidade de instantes dentro de um segundo: "))
    TI = 1/TI
    dists = []
    print("")

    i = 0
    print(ini_dist)
    while p1 < pf:
        _dist = abs(p2 - p1)
        _acel = fgrav(m2,_dist)
        _perc = nova_distancia(_perc,_vel,TI,_acel)
        _vel = v0at(_vel,_acel,TI)
        i += 1
        p1 = _perc
        dists.append(p1)
        print(f"\nInstante {i}:\n\tPosicao de p1 = {p1}\n\tTempo = {round(TI*i,2)} seg\n\tDistancia entre p1 e p2 = {abs(p2 - p1)}\n\tAceleração = {_acel}\n\tVelocidade = {_vel}")
    print(dists)
    continuar = int(input("Digite 1 para continuar e 0 para sair: "))
