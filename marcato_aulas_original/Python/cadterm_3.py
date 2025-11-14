tabela = CasoEstudo.cadterm.cadusit_df

for index, row in CasoEstudo.cadterm.cadunidt_df.iterrows():
  flag = int(row['flag_equiv']) if row['flag_equiv'].strip() else 0
  if flag == 0:  # Só ciclo simples
    codigo_usina = row['num_usi']
    linha = tabela.loc[tabela['num_usi'] == codigo_usina, 'nome'].values[0]
    print(linha)