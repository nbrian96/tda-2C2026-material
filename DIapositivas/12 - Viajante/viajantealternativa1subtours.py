from pulp import *
import time
# ALTERNATIVA 1: ROMPER SUBTOURS
print("ALTERNATIVA 1: ROMPER SUBTOURS")
t1=time.time()
# INICIALIZAR MATRIZ
print("inicializando matriz...")
N=0
D=[]
nombres=[]
arch=open("distancias12.csv","r")
linea=arch.readline()
while linea!='':
    lista=linea.split(";")
    nombres.append(lista.pop(0))
    D.append([])
    for i in lista:
        D[N].append(int(i))
    linea=arch.readline()
    N+=1     # N es la cantidad de ciudades incluyendo el origen
arch.close()


#CREAR MODELO
print("creando modelo...")
prob = LpProblem("Viajante",LpMinimize)

#DEF VARIABLES
Y = LpVariable.dicts("Y", (nombres,nombres), 0, cat = "Binary")

#FUNCIONAL
prob += (lpSum([Y[i][j]*D[nombres.index(i)][nombres.index(j)] for i in nombres for j in nombres]),"Z",)

#RESTRICCIONES
for j in nombres:
    prob += lpSum([Y[i][j] for i in nombres])==1
for i in nombres:
    prob += lpSum([Y[i][j] for j in nombres])==1
for i in nombres:
    prob += Y[i][i]==0

#ELIMINA SUBTOURS DE 2:
print("eliminando subtours de 2...")
for i in nombres:
    for j in nombres:
        if i!=j:
            prob += Y[i][j]+Y[j][i] <= 1

#ELIMINA SUBTOURS DE 3:
print("eliminando subtours de 3...")
for i in nombres:
    for j in nombres:
        for k in nombres:
                if i!=j and i!=k and j!=k:
                    prob += Y[i][j]+Y[j][i]+Y[i][k]+Y[k][i]+Y[j][k]+Y[k][j] <= 2

#ELIMINA SUBTOURS DE 4:
print("eliminando subtours de 4...")
for i in nombres:
    for j in nombres:
        for k in nombres:
            for l in nombres:
                if i!=j and i!=k and j!=k and i!=l and j!=l and k!=l:
                    prob += Y[i][j]+Y[j][i]+Y[i][k]+Y[k][i]+Y[j][k]+Y[k][j]+Y[i][l]+Y[l][i]+Y[j][l]+Y[l][j]+Y[k][l]+Y[l][k] <= 3

#ELIMINA SUBTOURS DE 5:
print("eliminando subtours de 5...")
for i in nombres:
    for j in nombres:
        for k in nombres:
            for l in nombres:
                for a in nombres:
                    if i!=j and i!=k and j!=k and i!=l and j!=l and k!=l and i!=a and j!=a and k!=a and l!=a:
                        prob += Y[i][j]+Y[j][i]+Y[i][k]+Y[k][i]+Y[j][k]+Y[k][j]+Y[i][l]+Y[l][i]+Y[j][l]+Y[l][j]+Y[k][l]+Y[l][k]+Y[i][a]+Y[j][a]+Y[k][a]+Y[l][a]+Y[a][i]+Y[a][j]+Y[a][k]+Y[a][l] <= 4

#ELIMINA SUBTOURS DE 6:
print("eliminando subtours de 6...")
for i in nombres:
    for j in nombres:
        for k in nombres:
            for l in nombres:
                for a in nombres:
                    for b in nombres:
                        if i!=j and i!=k and j!=k and i!=l and j!=l and k!=l and i!=a and j!=a and k!=a and l!=a and i!=b and j!=b and k!=b and l!=b and a !=b:
                            sub1=[i,j,k,l,a,b]
                            prob += lpSum(Y[i][j] for i in sub1 for j in sub1) <= 5
#                             prob += Y[i][j]+Y[j][i]+Y[i][k]+Y[k][i]+Y[j][k]+Y[k][j]+Y[i][l]+Y[l][i]+Y[j][l]+Y[l][j]+Y[k][l]+Y[l][k]+Y[i][a]+Y[j][a]+Y[k][a]+Y[l][a]+Y[a][i]+Y[a][j]+Y[a][k]+Y[a][l]+Y[i][b]+Y[b][i]+Y[j][b]+Y[b][j]+Y[k][b]+Y[b][k]+Y[l][b]+Y[b][l]+Y[a][b]+Y[b][a] <= 5

prob.writeLP("ViajanteAlt1.lp")

#RESOLVER
print("resolviendo...")
status= prob.solve()

#MOSTRAR RESULTADO
if LpStatus[status] =="Optimal":
    for i in nombres:
        for j in nombres:
            if Y[i][j].value()==1:
                print(Y[i][j], D[nombres.index(i)][nombres.index(j)])
    print("Z =", value(prob.objective))
t2=time.time()
print("Tiempo:", t2-t1)
