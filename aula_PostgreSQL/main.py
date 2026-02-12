import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(
    host='localhost',
    port=5432, # Porta padrão PostgreSQL
    dbname='postgres',
    user='postgres',
    password='sctec'
)

conn.autocommit = True # O comando CREATE DATABASE não pode ser executado dentro de uma transação pendente. Ele exige que o banco salve a alteração imediatamente. Por isso, ativamos o autocommit

# Definir um novo banco de dados
db_name = 'db_mundotech'

# Criar uma string SQL para ser executada
# create_db_query = sql.SQL('CREATE DATABASE {}').format(sql.Identifier(db_name)) # Previne SQL injection. Se fizesse f"CREATE DATABASE {db_name}", código ficaria vulnerável a ataques. Identifier coloca as aspas duplas de segurança ao redor do nome do banco (ex: "db_mundotech"), garantindo que o Postgres entenda que aquilo é um nome de objeto e não um comando malicioso.

# Executar o comando
cur = conn.cursor()

# cur.execute(create_db_query)

# Fechar as conexoes do banco
# cur.close()
# conn.close()

# print(f"Banco de dados {db_name} contruído com sucesso.")

# create_table_query = '''
#     CREATE TABLE nome_tabela (
#         coluna1 VARCHAR(255),
#         coluna2 VARCHAR(255)
#         )
# '''

# cur.execute(create_table_query)
# conn.commit()

# cur.close()
# conn.close()

# print("Tabela construída com sucesso")

# INSERT
# valor1 = 'texto1'
# valor2 = 'texto2'
# cur.execute('INSERT INTO nome_tabela (coluna1, coluna2) VALUES (%s, %s)', (valor1, valor2))
# conn.commit

# cur.close()
# conn.close()

# SELECT
cur.execute('SELECT * FROM nome_tabela')
rows = cur.fetchall()

for row in rows:
    print(row)

# cur.close()
# conn.close()

# UPDATE
# novo_valor = 'texto_atualizado'
valor_criterio = 'texto2' # Busca
# cur.execute('UPDATE nome_tabela SET coluna1 = %s WHERE coluna2 = %s', (novo_valor, valor_criterio))

# cur.execute('SELECT * FROM nome_tabela')
# rows = cur.fetchall()

# for row in rows:
#     print(row)

# cur.close()
# conn.close()

# DELETE
cur.execute('DELETE FROM nome_tabela WHERE coluna2 = %s', (valor_criterio,))
conn.commit()

cur.execute('SELECT * FROM nome_tabela')
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()