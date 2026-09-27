import time

# INICIALIZAR MATRIZ
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

t1=time.time()
costomin = 99999 
for i in nombres:
    for j in nombres:
        if i!=j:
            for k in nombres:
                if k!=i and k!=j:
                    for l in nombres:
                        if l!=i and l!=j and l!=k:
                            for m in nombres:
                                if m!=l and m!=k and m!=j and m!=i:
                                    for n in nombres:
                                        if n!=m and n!=l and n!=k and n!=j and n!=i:
                                            for p in nombres:
                                                if p!=n and p!=m and p!=l and p!=k and p!=j and p!=i:
                                                    for q in nombres:
                                                        if q!=p and q!=n and q!=m and q!=l and q!=k and q!=j and q!=i:
                                                            for r in nombres:
                                                                if r!=q and r!=p and r!=n and r!=m and r!=l and r!=k and r!=j and r!=i:
                                                                    for s in nombres:
                                                                        if s!=r and s!=q and s!=p and s!=n and s!=m and s!=l and s!=k and s!=j and s!=i:
                                                                            for t in nombres:
                                                                                if t!=s and t!=r and t!=q and t!=p and t!=n and t!=m and t!=l and t!=k and t!=j and t!=i:
                                                                                    for u in nombres:
                                                                                        if u!=t and u!=s and u!=r and u!=q and u!=p and u!=n and u!=m and u!=l and u!=k and u!=j and u!=i:
                                                                                            costo = D[nombres.index(i)][nombres.index(j)] + D[nombres.index(j)][nombres.index(k)] + D[nombres.index(k)][nombres.index(l)] +D[nombres.index(l)][nombres.index(m)]+D[nombres.index(m)][nombres.index(n)]+D[nombres.index(n)][nombres.index(p)]+D[nombres.index(p)][nombres.index(q)]+D[nombres.index(q)][nombres.index(r)]+D[nombres.index(r)][nombres.index(s)]+D[nombres.index(s)][nombres.index(t)]+D[nombres.index(t)][nombres.index(u)]+D[nombres.index(u)][nombres.index(i)]
                                                                                            if costo < costomin:
                                                                                                costomin = costo
                                                                                                viajemin = [i,j,k,l,m,n,p,q,r,s,t,u]
t2=time.time()
print("Tiempo total: ",t2-t1)
print("El costo mínimo es ", costomin, " y recorre las ciudades ")
for i in viajemin:
    print (i)

                                
                            

