import psycopg2,array


conn = psycopg2.connect("user=memoria password=memoriaaeterna host=127.0.0.1 dbname=dbmemoria")
curs = conn.cursor()
curs.execute("""Drop TABLE operations""")
curs.execute("""CREATE TABLE operations (id SERIAL PRIMARY KEY,Nomclient varchar(200),IdClient  varchar(200),NomOperation varchar(200),Date varchar(100))""")
#curs.execute("""Drop TABLE adresses""")
curs.execute("""CREATE TABLE adresses (id SERIAL PRIMARY KEY, idoperation varchar(200),colonne1 varchar(200),colonne2 varchar(200),colonne3 varchar(200),colonne4 varchar(200),colonne5 varchar(200),colonne6 varchar(200),colonne7 varchar(200),colonne8 varchar(200),colonne9 varchar(200),colonne10 varchar(200),colonne11 varchar(200),colonne12 varchar(200),colonne13 varchar(200),colonne14 varchar(200),colonne15 varchar(200),colonne16 varchar(200),colonne17 varchar(200),colonne18 varchar(200),colonne19 varchar(200),colonne20 varchar(200))""")
conn.commit()
conn.close()
print "FINIT"