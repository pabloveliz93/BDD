from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()

sql="""
insert into tallas (talla) values ('XS'),('S'),('M'),('L'),('XL'),('ESP');
"""
cur.execute(sql)
sql = """
insert into colores (color) values ('rojo'),('azul'),('verde'),('amarillo'),('negro'),('blanco');
"""
cur.execute(sql)
#conn.commit()
#post_id=cur.fetchone()[0]

#print post_id

sql = """
insert into clasif (nombre) values ('polera'),('poleron'),('tinta inkjet'),('vinilo'),('papel'),('tinta sublimacion'), ('taza'), ('reloj');
"""
cur.execute(sql)

sql = """
insert into genero (nombre) values ('pokemon'),('steven universe'),('zelda'),('anime'),('videojuegos'),('manga'), ('geek'), ('informatica'), ('ingenieria');
"""
cur.execute(sql)

conn.commit()
cur.close()
conn.close()
