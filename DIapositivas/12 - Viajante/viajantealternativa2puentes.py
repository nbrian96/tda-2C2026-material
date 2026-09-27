from pulp import *
import time
# ALTERNATIVA 2: CONSTRUIR PUENTES
print("ALTERNATIVA 2: CONSTRUIR PUENTES")
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

#PUENTES PARA GRUPOS DE 2:
print("creando puentes para grupos de 2...")
for i in nombres:
    for j in nombres:
        if i!=j:
            sub1=[i,j]
            sub2=[]
            for k in nombres:
                if k not in sub1:
                    sub2.append(k)
            prob += lpSum(Y[i][j] for i in sub1 for j in sub2) >= 1

#PUENTES PARA GRUPOS DE 3:
print("creando puentes para grupos de 3...")
for i in nombres:
    for j in nombres:
        for k in nombres:
                if i!=j and i!=k and j!=k:
                    sub1=[i,j,k]
                    sub2=[]
                    for n in nombres:
                        if n not in sub1:
                            sub2.append(n)
                    prob += lpSum(Y[i][j] for i in sub1 for j in sub2) >= 1
                            
 
#PUENTES PARA GRUPOS DE 4:
print("creando puentes para grupos de 4...")
for i in nombres:
    for j in nombres:
        for k in nombres:
            for l in nombres:
                if i!=j and i!=k and j!=k and i!=l and j!=l and k!=l:
                    sub1=[i,j,k,l]
                    sub2=[]
                    for n in nombres:
                        if n not in sub1:
                            sub2.append(n)
                    prob += lpSum(Y[i][j] for i in sub1 for j in sub2) >= 1
                    
                   
#PUENTES PARA GRUPOS DE 5:
print("creando puentes para grupos de 5...")
for i in nombres:
    for j in nombres:
        for k in nombres:
            for l in nombres:
                for a in nombres:
                    if i!=j and i!=k and j!=k and i!=l and j!=l and k!=l and i!=a and j!=a and k!=a and l!=a:
                        sub1=[i,j,k,l,a]
                        sub2=[]
                        for n in nombres:
                            if n not in sub1:
                                sub2.append(n)
                        prob += lpSum(Y[i][j] for i in sub1 for j in sub2) >= 1
              
#PUENTES PARA GRUPOS DE 6:
print("creando puentes para grupos de 6...")
for i in nombres:
    for j in nombres:
        for k in nombres:
            for l in nombres:
                for a in nombres:
                    for b in nombres:
                        if i!=j and i!=k and j!=k and i!=l and j!=l and k!=l and i!=a and j!=a and k!=a and l!=a and i!=b and j!=b and k!=b and l!=b and a !=b:
                            sub1=[i,j,k,l,a,b]
                            sub2=[]
                            for n in nombres:
                                if n not in sub1:
                                    sub2.append(n)
                            prob += lpSum(Y[i][j] for i in sub1 for j in sub2) >= 1
                          
prob.writeLP("ViajanteAlt2.lp")

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
