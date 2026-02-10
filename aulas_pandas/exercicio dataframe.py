import pandas as pd

data = {
    'Nome': ['João', 'Aline', 'Maria', 'José'],
    'Endereco': ['Curitiba', 'São Paulo', 'Florianópolis', 'Criciúma'],
    'Nascimento': ['22/10/1980', '02/04/1991', '30/11/1994', '11/3/1983'],
    'Admissao': ['05/06/2020', '22/03/2024', '03/11/2025', '15/08/2000'],
    'Salário': [2000, 2500, 1800, 5000],
    'Cargo': ['Técnico', 'Recepcionista', 'Analista', 'Garçom']
}

df = pd.DataFrame(data)

print(df['Admissao'])