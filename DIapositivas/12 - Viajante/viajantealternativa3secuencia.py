from pulp import *
import time
# ALTERNATIVA 3: DEFINIR SECUENCIA
print("ALTERNATIVA 3: DEFINIR SECUENCIA")
# INICIALIZAR MATRIZ
print("inicializando matriz...")
t1=time.time()
N=0
D=[]
nombres=[]
ordenes=[]
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
    ordenes.append(N)
arch.close()


#CREAR MODELO
print("creando modelo...")
prob = LpProblem("Viajante",LpMinimize)

#DEF VARIABLES
Y = LpVariable.dicts("Y", (nombres,nombres,ordenes), 0, cat = "Binary")


#FUNCIONAL
prob += (lpSum([Y[i][j][t]*D[nombres.index(i)][nombres.index(j)] for i in nombres for j in nombres for t in ordenes]),"Z",)

#RESTRICCIONES

for i in nombres:
    prob += lpSum(Y[i][i][t] for t in ordenes) == 0

for i in nombres:
    prob += lpSum([Y[i][j][t] for j in nombres for t in ordenes])==1

for j in nombres:
    for t in range(1,N) :
        prob += (lpSum(Y[k][j][t] for k in nombres )== lpSum(Y[j][i][t+1] for i in nombres))

for j in nombres:
    prob += (lpSum(Y[k][j][N] for k in nombres )== lpSum(Y[j][i][1] for i in nombres))



prob.writeLP("Viajantealternativo3.lp")

#RESOLVER
print("resolviendo...")
status= prob.solve()

#MOSTRAR RESULTADO
if LpStatus[status] =="Optimal":
    for i in nombres:
        for j in nombres:
            for t in ordenes:
                if Y[i][j][t].value()==1:
                    print(Y[i][j][t], D[nombres.index(i)][nombres.index(j)])
    
    print("Z =", value(prob.objective))
t2=time.time()
print("Tiempo:", t2-t1)

