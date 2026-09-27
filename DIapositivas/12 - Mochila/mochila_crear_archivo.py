def carga_archivo():
    arch=open("mochila.txt","w")
    cap=int(input("Ingrese capacidad de la mochila:"))
    arch.write(str(cap)+"\n")
    mas=True
    while(mas):
        elem=input("Ingrese el nombre:(o BASTA para terminar)")
        if elem!="BASTA":
            peso=int(input("Ingrese su peso:"))
            beneficio=int(input("Ingrese su beneficio:"))
            arch.write(elem+"\n")
            arch.write(str(peso)+"\n")
            arch.write(str(beneficio)+"\n")
        else:
            mas=False
    arch.close()
carga_archivo()
            