import pandas as pd


tabela = pd.read_csv("cancelamentos.csv")
tabela = tabela.drop("CustomerID", axis=1)

print(tabela.info())
tabela = tabela.dropna()
print(tabela.info())

print(tabela["cancelou"].value_counts())
print(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

print(tabela["duracao_contrato"].value_counts(normalize=True).map("{:.1%}".format))
print(tabela["duracao_contrato"].value_counts())

print(tabela.groupby("duracao_contrato").mean(numeric_only=True))