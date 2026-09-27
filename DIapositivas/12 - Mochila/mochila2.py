from pulp import *

X=[]
C={}
P={}
arch=open("mochilagrande.txt","r")
# arch=open("mochila.txt","r")
capacidadstr=arch.readline()
capacidad = int(capacidadstr)
elem=arch.readline()
while elem!='':
    peso=int(arch.readline())
    benef=int(arch.readline())
    X.append(elem)
    C[elem]=peso
    P[elem]=benef
    elem=arch.readline()
arch.close()    

prob = LpProblem("Mochila",LpMaximize)
elementos = LpVariable.dicts("Elemento", X, 0, cat = "Binary")
prob += lpSum([P[i]*elementos[i] for i in X])
prob += lpSum([C[i]*elementos[i] for i in X]) <=capacidad
## prob.writeLP("Mochila.lp")
status= prob.solve()
if LpStatus[status] =="Optimal":
    for i in elementos:
        print(i, elementos[i].value())
    print("Z =", value(prob.objective))
    suma=0
    for i in elementos:
        if elementos[i].value()==1:
            suma+=C[i]
    print("Capacidad de la mochila:", capacidad)
    print("Capacidad utilizada:    ", suma)
    
    
    
    