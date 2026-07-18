gastos = []

try:
    arquivo = open("gastos.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()

    for linha in linhas:
        lina = linha.strip()
        partes = linha.split(",")
        descricao = partes[0]
        categoria = partes[1]
        valor = float(partes[2])
        gasto = {"descricao": descricao, "categoria": categoria, "valor": valor}
        gastos.append(gasto)

    
except:
    pass


while True:
    print("\n1 - Adicionar gastos")
    print("2 - Ver gastos")
    print("3 - Ver total de gastos")
    print("4 - Sair")
    
    opcao = input("Selecione: ")
    
    if opcao == "4":
        break
    
    elif opcao == "1":
        descricao = input("Descrição do gasto: ")
        categoria = input("Categoria (ex: alimentação, transporte): ")
        valor = input("Valor: ")
        valor = float(valor)
        
        gasto = {"descricao": descricao, "categoria": categoria, "valor": valor}
        gastos.append(gasto)

        arquivo=open("gastos.txt", "a")

        arquivo.write(f"{descricao},{categoria}.{valor}\n")
        arquivo.close()



        print("Gasto adicionado!")
    
    elif opcao == "2":
        for gasto in gastos:
            print(f"{gasto['descricao']} - {gasto['categoria']} - R${gasto['valor']}")
             
    elif opcao=="3":
        soma=0
        for gasto in gastos:
            soma=soma + gasto["valor"]

        
        print(f"total gasto: R${soma}")