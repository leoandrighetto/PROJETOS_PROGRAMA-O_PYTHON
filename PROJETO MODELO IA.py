#ARQUIVO  IPYNB ARQUIVO  IPYNB ARQUIVO  IPYNB ARQUIVO  IPYNB ARQUIVO  IPYNB ARQUIVO  IPYNB ARQUIVO  IPYNB ARQUIVO  IPYNB ARQUIVO  IPYNB ARQUIVO  IPYNB


#PASSO A PASSO
# PASSO 0 - ENTENDER A EMPRESA E O DESAFIO DA EMPRESA
# PASSO 1 - IMPORTAR A BASE DE DADOS
# PASSO 2 - PREPARA A BASE DE DADOS PARA A IA
# PASSO 2.1 - DIVIDIR A BASE DE DADOS EM DUAS PARTES
# PASSO 3 - TREINAR A INTELIGENCIA ARTIFICIAL -> CRIAR O MODELO: NOTA DE CRÉDITO: BOA, OK, RUIM
# PASSO 4 - ESCOLHER QUAL MELHOR MODELO
# PASSO 5 - USAR O MELHOR MODELO PARA FAZER AS PREVISÕES DE NOVOS CLIENTES






# divisao_celula divisao_celula divisao_celula divisao_celula divisao_celula






# PASSO 1 - IMPORTAR A BASE DE DADOS
import pandas as pd

tabela = pd.read_csv("clientes.csv")

display(tabela)





# divisao_celula divisao_celula divisao_celula divisao_celula divisao_celula()






# PASSO 2 - PREPARAR A BASE DE DADOS PARA A IA 

# tipos de dados:
# int (inteiros)
# float (decimais)
# object (texto)

# !!IAs NÃO CONSEGUEM APRENDER SOBRE A BASE DE DADOS COM COLUNAS DE TEXTO (object)!!!
# VAMOS INICIAR O PROCESSO DE LABELENCODER (DOCIFICAR OS RÓTULOS): TRANSFORMAR
# AS INFORMAÇÕES DAS COLUNAS DE TEXTO EM NÚMEROS:

# profissao
# mix_credito
# comportamento_pagamento

# LINHA DE CÓDIGO RETIRADA DA BIBLIOTECA SCIKIT-LEARN:

from sklearn.preprocessing import LabelEncoder

# EXECUTANDO O PROCESSO DE LABELENCODER:

cod_profissao = LabelEncoder()
tabela['profissao'] = cod_profissao.fit_transform(tabela['profissao'])
#novovalortabela    = antigovalor    transformado no  codificador

cod_credito = LabelEncoder()
tabela['mix_credito'] = cod_credito.fit_transform(tabela['mix_credito'])

cod_comportamento = LabelEncoder()
tabela['comportamento_pagamento'] = cod_comportamento.fit_transform(tabela['comportamento_pagamento'])

display(tabela.info())







# divisao_celula divisao_celula divisao_celula divisao_celula divisao_celula()





   
#PASSO 2.1

# A COLUNA (y) SERÁ A COLUNA QUE QUEREMOS PREVER:
y = tabela['score_credito']



x = tabela.drop(columns = ['score_credito', 'id_cliente']) # id do cliente também não serve para nada.
# A COLUNA (x) SERÁ AS COLUNAS DE TREINAMENTO  
# TODAS AS COLUNAS MENOS A QUE QUEREMOS PREVER




# SEPARAMOS A BASE ENTRE ESTAS DUAS VARIÁVEIS PARA TREINAR NOSSA IA USANDO UMA FUNÇÃO DA BIBLIOTECA SCIKIT-LEARN:

from sklearn.model_selection import train_test_split
                                   #treino, teste, separação
# SEPARA DA BASE OS DADOS DE TREINO E DE TESTE


# A FUNÇÃO DA BIBLIOTECA É USADA SEMPRE NA MESMA ORDEM, PARA FACILITAR A NOSSA VIDA:
# X TREINO, X TESTE, Y TREINO, Y TESTE:

#---                                                          #tamanho do teste: 70 / 30
x_treino, x_teste, y_treino, y_teste = train_test_split (x, y, test_size = 0.3)
#---






# divisao_celula divisao_celula divisao_celula divisao_celula divisao_celula()





# PASSO 3 - TREINAR A INTELIGENCIA ARTIFICIAL -> CRIAR O MODELO: NOTA DE CRÉDITO: BOA, OK, RUIM

# PASSOS PARA CRIAR A IA:

# Passo 1 - IMPORTAR A IA
# Passo 2 - CRIAR A IA
# Passo 3 - TREINAR A IA



# VAMOS IMPORTAR DOIS MODELOS DIFERENTES QUE APRENDEM DE MANEIRAS DIFERENTES E TESTAR CADA UMA DELAS.


# 1º MODELO: ÁRVORE DE DECISÃO (RANDOMFOREST)
# 2º MODELO: VIZINHOS PRÓXIMOS (NEIREST NEIGHBORS)


# PASSO 1 - IMPORTAR A IA USANDO SUAS RESPECTIVAS BIBLIOTECAS EM ESPECÍFICO

# OU PODERIA TER IMPORTADO APENAS A BIBLIOTECA INTEIRA ONDE SE ENCONTRA O MODELO EM ESPECIAL

from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

# import sklearn.neighbors
# import sklearn.ensemble



# Passo 2 - CRAIR A IA ATRIBUINDO OS MODELOS À VARIÁVEIS
modelo_arvoredecisao = RandomForestClassifier()
modelo_knn = KNeighborsClassifier()



# Passo 3 - TREINAR A IA ATRIBUINDO ÀS VARIÁVEIS MODELOS O X_TREINO, Y_TREINO
modelo_arvoredecisao.fit(x_treino, y_treino)
modelo_knn.fit(x_treino, y_treino)

# divisao_celula divisao_celula divisao_celula divisao_celula divisao_celula()

# PASSO 4 - TESTAR OS MODELOS E ESCOLHER QUAL É O MELHOR MODELO
# UTILIZANDO A FUNÇÃO DE ACURÁCIA.
#ATRIBUÍNDO OS MODELOS À UMA VARIÁVEL COM O COMANDO "PREDICT"?

previsao_arvore_decisao = modelo_arvoredecisao.predict(x_teste)
previsao_knn = modelo_knn.predict(x_teste)

# para saber como comparar os modelos, calculamos a acurácia( precisão ) de ambos.

from sklearn.metrics import accuracy_score

display(accuracy_score(y_teste, previsao_arvore_decisao))
display(accuracy_score(y_teste, previsao_knn))

# PASSO 5 - USAR O MELHOR MODELO PARA FAZER AS PREVISÕES DE NOVOS CLIENTES

# UTILIZANDO A NOVA TABELA NO FORMATO CSV 

# 1.0 PRECISAMOS CODIFICAR NOVAMENTE AS COLUNAS EM TEXTO PARA A INTERPRETAÇÃO A IA DAR CERTO:

tabela_novos_clientes = pd.read_csv('novos_clientes.csv')


from sklearn.preprocessing import LabelEncoder

# EXECUTANDO O PROCESSO DE LABELENCODER:

cod_profissao = LabelEncoder()
tabela_novos_clientes['profissao'] = cod_profissao.fit_transform(tabela_novos_clientes['profissao'])
#novovalortabela    = antigovalor    transformado no  codificador

cod_credito = LabelEncoder()
tabela_novos_clientes['mix_credito'] = cod_credito.fit_transform(tabela_novos_clientes['mix_credito'])

cod_comportamento = LabelEncoder()
tabela_novos_clientes['comportamento_pagamento'] = cod_comportamento.fit_transform(tabela_novos_clientes['comportamento_pagamento'])

# display(tabela.info())

nova_previsao = modelo_knn.predict(tabela_novos_clientes)

display(nova_previsao)
