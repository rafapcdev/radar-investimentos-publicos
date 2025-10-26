import pandas as pd
import requests
import sys

url = "https://apicadprev.trabalho.gov.br/DAIR_CARTEIRA"
parametros = {
    'nr_cnpj_entidade': "29131075000193",
    'sg_uf': "RJ",
    'dt_ano': 2025
}

arquivo_csv = "investimentos_marica_2025.csv"

response = requests.get(url, timeout=60, params=parametros)

if response.ok:
    data = response.json()["data"]

    mapa_meses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'} # Mapeamento dos números dos meses para nomes

    df = pd.DataFrame(data)
    
    df['vl_atual_ativo'] = df['vl_atual_ativo'].astype(float) # Converte para float
    
    vl_total_por_mes = df.groupby('dt_mes_bimestre')['vl_atual_ativo'].sum() # Agrupa por mês/bimestre e soma os valores

    vl_total_por_mes = vl_total_por_mes.rename(mapa_meses) # Renomeia os índices para nomes dos meses

    vl_total_por_mes = vl_total_por_mes.round(2) # Arredonda para 2 casas decimais

    vl_total_por_mes.to_csv("investimentos_marica_2025.csv") # Salva o resumo em CSV

    print(f"Arquivo '{arquivo_csv}' salvo com sucesso!")
    print("\nResumo dos totais por mês:")
    print(vl_total_por_mes)

    # df.to_excel("rafael.xlsx")
    # df.head()
    # df.info()

else:
    print("houve um problema na conexão da API")
    print(f"Status Code: {response.status_code}")
    print(f"Resposta: {response.text}")
    

