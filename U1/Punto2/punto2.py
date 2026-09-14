import json

def es_reflexiva(estructura):
    count=0
    for x in estructura['P']:
        if x in estructura['E'][x] and x in estructura['E']:
            count+=1
    if count == len(estructura['P']):
        
        return True
    else:
        
        return False

def es_Simetrica(estructura):
    for x in estructura['P']:
        for y in estructura['E'][x]:
            if x not in estructura['E'][y] and y in estructura['E']:
                
                return False
    
    return True
            



def es_antisimetrica(estructura):
    es_antisimetrica = True

    for x in estructura['E']:
        for y in estructura['E'][x]:
            # Solo comprobamos para elementos distintos (x != y)
            if x != y:
                # Si 'y' se relaciona de vuelta con 'x', rompe la antisimetría
                if y in estructura['E'] and x in estructura['E'][y]:
                    es_antisimetrica = False
                    break
                    
        if not es_antisimetrica:
            break  # Cortamos el bucle exterior

    if es_antisimetrica:
        return True
    else:
        return False

def es_transitiva(estructura):
    es_transitiva = True

    for x in estructura['E']:
        for y in estructura['E'][x]:
            # Si 'y' tiene vecinos hacia otros nodos ('z')
            if y in estructura['E']:
                for z in estructura['E'][y]:
                    # Verificamos si la conexión directa 'x -> z' NO existe
                    if z not in estructura['E'][x]:
                        es_transitiva = False
                        break
                        
            if not es_transitiva:
                break
                
        if not es_transitiva:
            break  # Cortamos el bucle exterior


    if es_transitiva:
        return True
    else:
        return False

def es_Orden(estructura):
    if es_reflexiva(estructura) and es_antisimetrica(estructura) and es_transitiva(estructura):
        print("es un orden")
    else:
        print("no es un orden")

def es_Equivalencia(estructura):
    if es_reflexiva(estructura) and es_Simetrica(estructura) and es_transitiva(estructura):
        print("es una relacion de equivalencia")
    else:
        print("no es una relacion de equivalencia")

def main():
    f = open('02.json')
    estructura = json.load(f)

    print(" ")
    print(" ")
    if(es_reflexiva(estructura)== True):
        print("es reflexiva")
    else:
        print("no es reflexiva")
    print(" ")
    print(" ")
    if (es_Simetrica(estructura)== True):
        print("es simetrica")
    else:
        print("no es simetrica")

    print(" ")
    print(" ")
    if(es_antisimetrica(estructura)== True):
        print("es antisimetrica")
    else:
        print("no es antisimetrica")
    print(" ")
    print(" ")
    if(es_transitiva(estructura)== True):
        print("es transitiva")
    else:
        print("no es transitiva")
    print(" ")
    print(" ")
    es_Orden(estructura)
    print(" ")
    print(" ")
    es_Equivalencia(estructura)

    

    f.close()

main()