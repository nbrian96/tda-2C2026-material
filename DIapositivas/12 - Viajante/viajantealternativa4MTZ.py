from pulp import *
import time
# ALTERNATIVA 4: DEFINIR UN ORDEN: MTZ
print("ALTERNATIVA 3: DEFINIR UN ORDEN: MTZ")
# INICIALIZAR MATRIZ
print("inicializando matriz...")
t1=time.time()
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

nombres2=[]   #nombres2 es la lista de nombres sin el origen
for n in nombres:
    nombres2.append(n)
nombres2.pop(0)

#CREAR MODELO
print("creando modelo...")
prob = LpProblem("Viajante",LpMinimize)

#DEF VARIABLES
Y = LpVariable.dicts("Y", (nombres,nombres), 0, cat = "Binary")
U = LpVariable.dicts("U", (nombres2), 1, cat = "Integer")

#FUNCIONAL
prob += (lpSum([Y[i][j]*D[nombres.index(i)][nombres.index(j)] for i in nombres for j in nombres]),"Z",)

#RESTRICCIONES
for j in nombres:
    prob += lpSum([Y[i][j] for i in nombres])==1
for i in nombres:
    prob += lpSum([Y[i][j] for j in nombres])==1
for i in nombres:
    prob += Y[i][i]==0
for i in nombres2:
    for j in nombres2:
        if i!=j:
            prob += U[i] - U[j] + (N-1)*Y[i][j] <= N-2

prob.writeLP("ViajanteAlternativa4MTZ.lp")

#RESOLVER
print("resolviendo...")
status= prob.solve()

#MOSTRAR RESULTADO
if LpStatus[status] =="Optimal":
    for i in nombres:
        for j in nombres:
            if Y[i][j].value()==1:
                print(Y[i][j], D[nombres.index(i)][nombres.index(j)])
    for i in nombres2:
        print(U[i], U[i].value())
    print("Z =", value(prob.objective))

t2=time.time()
print("Tiempo: ",t2-t1)
