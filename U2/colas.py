def crearCola(largo):
    cola={}
    cola["cant_elementos"]=0
    cola["final"]=-1
    cola["cola"]=[]
    cola["largo"]=largo
    return cola

def enqueue(cola,valor):
    if cola["cant_elementos"] <= cola["largo"]:
        cola["cola"].append()

def main():
    largo = input()
    cola=crearCola(largo)
    with open("02.csv", "r") as f:
        datos = f.read()
    comando=[]
    intruccion=[]
    for d in datos:
        if d=='\n':
            comando.append(intruccion)
        elif d!=',':
            intruccion.append(d)

    for intruccion in comando:
        intruccion = intruccion.split(",")
        if intruccion[0].lower == "enqueue":
            enqueue(intruccion[1])
        elif intruccion[0].lower == "dequeue":
            dequeue()

main()