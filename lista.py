def cadastrar():
    nome = input("Digite o nome do aluno a ser cadastrar: ")
    return nome

def mostrar(lista):
    print("nome dos alunos: ")
    numero = 1
    for aluno in lista:
        print(" - ",aluno)
        numero += 1
        
        
listaAlunos = ["Gustavo","Arthur","Daniel"]
opcao = 0
while opcao != 10:
    opcao = int(input("Digite 1 para mostrar os alunos cadastrados\nDigite 2 cadastrar\nDigite 3 para editar\nDigite 3 para editar\nDigite 4 para deletar"))
    if opcao == 1:
        mostrar(listaAlunos)
    elif opcao == 2:
        listaAlunos.append(cadastrar())
    elif opcao == 3:
        mostrar(listaAlunos)
        print("------------------------------")
        nome = input("Digite o nome de aluno para ser editado: ")
        posicao = listaAlunos.index(nome)
        novoNome = input("Digite o novo nome para salvar: ")
        listaAlunos[posicao] = novoNome
    elif opcao == 4:
        mostrar(listaAlunos)
        print("------------------------------")
        nome = input("Digite o nome de aluno que será deletado:")
        listaAlunos.remove(nome)
        print("Lista atualizada com sucesso!")