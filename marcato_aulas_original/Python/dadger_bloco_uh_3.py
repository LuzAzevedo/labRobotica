tabela = CasoEstudo.dadger.bloco_uh['df']

for index, row in tabela.iterrows():
  if int(row['ss']) == 6:
    print(f"Usina: {row['nome']}, Ree: {row['ss']}, Volume Inicial: {float(row['vinic']):6.2f} %")
