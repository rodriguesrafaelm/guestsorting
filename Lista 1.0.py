def salvar(a):
    a.sort()
    with open('Lista de convidados.txt', 'w') as f:
        f.write('\n'.join(a))
        f.close()
    print('Alterações salvas.')


temp = []
lista = []
with open("Lista de convidados.txt", "a+") as file:
    file.seek(0)
    while temp := file.readline().rstrip():
        lista.append(temp)
    file.close()
while True:
    nome = str(input("Digite \"0\" para abrir o menu.\nDigite um nome para adicionar um convidado: ").title())
    if nome == "0":
        print("O que deseja fazer?")
        continuar = int(input("1 - Salvar a lista e fechar o programa.\n2 - Listar ou remover convidados.\n3 - Voltar.\n-> "))
        if continuar == 1:
            break
        elif continuar == 2:
            lista.sort()
            for c in range(0, len(lista)):
                print(f'{c+1:<2}   {lista[c]}')
            remover = int(input("Deseja remover alguem?\nDigite o numero correspondente para remover ou digite 0 para voltar a adicionar convidados.\n-> "))
            if len(lista) >= remover > 0:
                print(f"Você removeu {lista[remover-1]} da lista com sucesso.")
                lista.pop(remover-1)
                salvar(lista)
            else:
                print('Continuando...')            
        else:
            print("Continuando...")
    else:
        if nome in lista:
            print('ERRO! - Esse nome já foi adicionado em outro momento.')
        else:
            lista.append(nome)
            salvar(lista)
            print(f"{nome} foi adicionado com sucesso.")
salvar(lista)
print("Programa finalizado.")
