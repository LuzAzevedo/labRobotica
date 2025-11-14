tabela = CasoEstudo.dadger.bloco_ut['df']

print(tabela.columns)

for index, row in tabela.iterrows():
  if float(row['gmin']) > 0.:
    print(f"Usina: {row['nome']}, Submercado: {row['ss']}, Inflexibilidade: {float(row['gmin']):10.2f} MW")