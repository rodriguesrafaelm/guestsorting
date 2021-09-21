temp = []
lista = []
with open("Lista de convidados.txt", "a") as file:
    file.close
with open("Lista de convidados.txt", "r+") as file:
    while temp := file.readline().rstrip():
        lista.append(temp)
    file.truncate(0)
    file.close()
while True:
    nome = str(input("Digite \"0\" para abrir o menu.\nDigite um nome para adicionar um convidado: ").capitalize())
    if nome == "0":
        print("O que deseja fazer?")
        continuar = int(input("1 - Parar a lista\n2 - Listar ou remover nomes\n3 - Continuar listando\n->"))
        if continuar == 1:
            break
        elif continuar == 2:
            lista.sort()
            for c in range(0, len(lista)):
                print(f'{c+1}   {lista[c]}')
            remover = int(input("Deseja remover alguem? \nDigite o numero correspondente para remover\nDigite 0 para voltar a adicionar convidados."))
        else:
            print("Continuando...")
    else:
        if nome in lista:
            print('Nome já adicionado.')
        else:
            lista.append(nome)
lista.sort()
with open('Lista de convidados.txt', 'a') as f:
    f.write('\n'.join(lista))
    f.close()
