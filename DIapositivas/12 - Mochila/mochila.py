from pulp import *
## Definimos las variables del modelo
x1 = LpVariable("x1",cat="Binary")
x2 = LpVariable("x2",cat="Binary")
x3 = LpVariable("x3",cat="Binary")
x4 = LpVariable("x4",cat="Binary")
x5 = LpVariable("x5",cat="Binary")

## Creamos el modelo
prob = LpProblem("Mochila",LpMaximize)
## Definimos las restricciones del modelo
prob += 30*x1+20*x2+20*x3+20*x4+25*x5<=65
## Definimos la funcion objetivo
prob += 30*x1+15*x2+80*x3+100*x4+10*x5

## Creamos un archivo para la salida de la solucion
prob.writeLP("Mochila.lp")

## Ejecutamos el solver
status= prob.solve()
if LpStatus[status] =="Optimal":
    print("X1=", value(x1))
    print("X2=", value(x2))
    print("X3=", value(x3))
    print("X4=", value(x4))
    print("X5=", value(x5))
    print("Z =", value(prob.objective))