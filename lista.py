def cadastrar():
    nome = input("Digite o nome do aluno a ser cadastrar: ")
    return nome

listaAlunos = ["Gustavo","Arthur","Daniel"]
listaAlunos.append(cadastrar())
print("Nome dos alunos da sala: ")
print(listaAlunos[0])
print(listaAlunos[1])
print(listaAlunos[2])
print(listaAlunos[3])