def cadastrar():
    nome = input("Digite o nome do aluno a ser cadastrar: ")
    return nome

def mostrar(lista):
    print("nome dos alunos: ")

listaAlunos = ["Gustavo","Arthur","Daniel"]
opcao = 0
while opcao != 10:
    opcao = int(input("Digite 1 para mostrar os alunos cadastrados\nDigite 2 cadastrar\nDigite 3 para editar\nDigite 3 para editar\nDigite 4 para deletar"))
    if opcao == 1:
        mostrar(lidtaAlumos)
    elif opcao == 2:
        listaAlunos.append(cadastrar())