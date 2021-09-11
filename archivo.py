archivo, f = "datos.txt", ""
docentes = [{"nombre":"Daniel", "edad":50, "fac":"Ing"},
    {"nombre":"Juan", "edad":30, "fac":"Salud"},
    {"nombre":"Dario", "edad":25, "fac":"Adminis"}]
 
 with open(archivo, "w") as writer:
     for i in range(len(docentes)):
         linea = ""
         for cñave, valor in docentes[i].items():
            if clave == "fac":
                 linea = linea + (str(valor) if type(valor)== int else valor) 
            else:
                linea = linea + (str(valor) if type(valor) == int else valor)
            writer.writelines(linea) 

try:
    f = open("algo.txt", "r")
    for linea in f:
        print(linea[:-1])
        f.close()
    except Exception as e:
        print("Error de archivo: " + str(e))
    finally:
        pass