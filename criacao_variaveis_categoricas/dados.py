import csv

    #Teste no console pytho
    # from dados import carregar_acessos
    # x,y = carregar_acessos()
def carregar_acessos():
    #dados
    X = []
    #marcacoes
    Y = []
    
    arquivo = open('acesso.csv', 'rb')
    leitor = csv.reader(arquivo)
    
    #pula primeira linha
    #leitor.next()
    next(leitor)
    
    for home, como_funciona, contato, comprou in leitor:
        
        dado = [int(home),int(como_funciona),int(contato)]
        X.append(dado)
        Y.append(int(comprou))
        
    return X, Y
  
      #Teste no console pytho
    # from dados import carregar_buscas
    # x,y = carregar_buscas()  
def carregar_buscas():
    
    X = [];
    Y = [];
    
    arquivo = open('busca.csv', 'rb')
    leitor = csv.reader(arquivo)
    leitor.next()
    
    for home,busca,logado,comprou in leitor:
        
        dado = [int(home), busca, int(logado)]
        X.append(dado)
        Y.append(int(comprou))
        
    return X, Y
        
    #Teste no console pytho
    # from dados import carregar_acessos
    # x,y = carregar_acessos()