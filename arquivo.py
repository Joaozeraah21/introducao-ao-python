with open("notas.txt","w", encoding="utf-8") as arquivo:
    arquivo.write("João: 9.5\n")
    arquivo.write("Carlos: 8.3\n")
    arquivo.write("Ana: 5.2\n")

with open("notas.txt","r", encoding = "utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())