lista_colaboradores = []
id_global = 1

print("Bem-vindo ao Controle de Colaboradores do Reijan Lopes de Jesus")

def menu():
    while True:
        print("*" * 70)
        print("-" * 27 + " MENU PRINCIPAL " + "-" * 27)
        print("1 - Cadastrar Colaborador")
        print("2 - Consultar Colaborador(es)")
        print("3 - Remover Colaborador")
        print("4 - Sair")
        select = input(">> ")
       
        if select == "4":
            break
        elif select in ["1", "2", "3"]:
            if select == "1":
                cadastrar_colaborador(id_global)
                break
            elif select == "2":
                consultar_colaborador()
                break
            else:
                remover_colaborador()
                break
        else:
            continue

def cadastrar_colaborador(id):
    global id_global
    id_global += 1
    print("*" * 70)
    print("-" * 21 + " MENU CADASTRAR COLABORADOR " + "-" * 21)
    print("id do colaborador {}".format(id))
    name = input("Por favor entre com o numero do colaborador: ")
    sector = input("Por favor entre com o setor: ")
    payment = float(input("Por favor entre com o pagamento(R$): "))
    collaborator = {
        "id": id,
        "name": name,
        "sector": sector,
        "payment": payment
    }

    lista_colaboradores.append(collaborator)
    menu()

def consultar_colaborador():
    print("*" * 70)
    print("-" * 21 + " MENU CONSULTAR COLABORADOR " + "-" * 21)
    print("1 - Consultar Todos os Colaboradores")
    print("2 - Consultar Colaborador por id")
    print("3 - Colsultar Coloborador(es) por setor")
    print("4 - Retonar")
    select = input(">> ")

    if select == "4":
        menu()
    elif select in ["1", "2", "3"]:
        if select == "1":
            print("-" * 15)
            for collaborator in lista_colaboradores:
                print("id: {}".format(collaborator["id"]))
                print("nome: {}".format(collaborator["name"]))
                print("setor: {}".format(collaborator["sector"]))
                print("pagamento: {}".format(collaborator["payment"]))
            print("-" * 15)
            menu()       

        elif select == "2":
            contributorId = int(input("Digite o id do colaborador: "))
            print("-" * 15)
            for collaborator in lista_colaboradores:
                if collaborator["id"] == contributorId:
                    break
            print("-" * 15)
            menu()

        else:
           collaboratingSector = input("Digite o setor do colaborador: ")
           for collaborator in lista_colaboradores:
            if collaborator["sector"] == collaboratingSector:
               print("-" * 15)
               print("id: {}".format(collaborator["id"]))
               print("nome: {}".format(collaborator["name"]))
               print("setor: {}".format(collaborator["sector"]))
               print("pagamento: {}".format(collaborator["payment"]))
               print("-" * 15)
               menu()
               break
            
           

def remover_colaborador():
   print("*" * 70)
   print("-" * 22 + " MENU REMOVER COLABORADOR " + "-" * 22)
   contributorId = int(input("Digite o id do colaborador a ser removido: "))
   for i, collaborator in enumerate(lista_colaboradores):
        if collaborator["id"] == contributorId:
            lista_colaboradores.pop(i)
            break
   menu()

menu()