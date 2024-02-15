
import psycopg2

# conectando o banco de dados
conn = psycopg2.connect(
    host = "127.0.0.1",
    database = "bdestudo",
    user = "postgres",
    password = "senha",
    port = "5432"
)
cursor = conn.cursor()


# criando a tabela
comando = '''CREATE TABLE public."AGENDA"
(
   id integer NOT NULL,
   nome text COLLATE pg_catalog."default" NOT NULL,
   telefone char(12) COLLATE pg_catalog."default" NOT NULL
);'''

# inserindo dados na tabela
comando2 = '''INSERT INTO public."AGENDA"( id, nome, telefone)
                VALUES (1, 'teste 1', '02199999999');'''

comando3 = ("""INSERT INTO "Agenda" ("id", "nome" , "telefone" ) 
            VALUES (2, 'Pessoa 1' , '02199999999' );""")


# consulta da tabela
cursor.execute("""select * from public."Agenda" where "id"=1""")
registro=cursor.fetchone()
print(registro)
print("Seleção realizada com sucesso!")


# atualização de um dado na tabela

cursor.execute("""Update public."Agenda" set "telefone"='02188888888' where "id"=1""")
print("Alteração realizada com sucesso!")

#verificando a tabela novamente para checarmos a alteração
cursor.execute("""select * from public."Agenda" where "id"=1""")
registro=cursor.fetchone()
print("Visualização apos a Atualização!")
print(registro)


# realizando a contagem de linhas dentro da tabela que foi alterada
cont = cursor.rowcount
print(cont, "Contagem realizada com sucesso!")
print("Programa Funcionando Perfeitamente")
#------------------------------------------

conn.commit()
cursor.close()
conn.close()
