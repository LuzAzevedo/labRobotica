for index, nome in enumerate(CasoEstudo.hidr.nome['valor']):
  if nome.strip() == 'JIRAU':
    print(f"Volume Máximo {CasoEstudo.hidr.vol_max['valor'][index]:6.2f} hm3")
    print(f"Volume Mínimo {CasoEstudo.hidr.vol_min['valor'][index]:6.2f} hm3")
    print("Máquina Por Conjunto: ", CasoEstudo.hidr.maq_por_conj['valor'][index])
    print("Potencia Efetiva Cada Máquina (MW)", CasoEstudo.hidr.pef_por_conj['valor'][index])