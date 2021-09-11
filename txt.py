def leer():
    with open("nombres.txt", "r", encoding= "UTF-8") as f:
        nombre = [line[:-1]for line in f]
        print(nombre)

def escribir():
    #nombres = ["Juna", "Pablo", "Pedro"]
    nombre_2 = ["Fernanda", "Lola", "Esperaza"]
    with open("nombres.txt", "w", encoding="UTF-8") as f:
        for nombre in nombre_2:
            f.write(nombre)
            f.write("\n")

def run():
    escribir()
    leer()

if __name__ == "__main__":
    run()