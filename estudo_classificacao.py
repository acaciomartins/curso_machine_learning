# he gordinho? tem perninha curta? se faz au au
porco1 =    [1, 1, 0]
porco2 =    [1, 1, 0] 
porco3 =    [1, 1, 0]
cachorro1 = [1, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [0, 1, 1]

dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

marcacoes = [1, 1, 1, -1, -1, -1]

from sklearn.naive_bayes import MultinomialNB
# treino inicio
modelo = MultinomialNB()
modelo.fit(dados, marcacoes)
#treino fim

# massa teste inicio
misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]
# massa teste fim

# Teste
teste = [misterioso1, misterioso2]

# Resultado
print(modelo.predict(teste))