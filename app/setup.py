from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))

cur= conn.cursor()
sql="""
CREATE TABLE productos (id serial,precio integer,diseno_id integer,insumo_id integer);
CREATE TABLE clientes (rut varchar(10),nombre varchar(30),comuna varchar(10));
CREATE TABLE pedidos (id serial,cliente_rut varchar(10), fecha date,entrega date,boletas_id integer);
CREATE TABLE pedido_detalle (producto_id integer,pedido_id integer);
CREATE TABLE insumos (id serial, nombre varchar(30),detalle_id integer,clasif_id integer);
CREATE TABLE clasif (id serial, nombre varchar(30));
CREATE TABLE proveedores (id serial,nombre varchar(30),rut varchar(10));
CREATE TABLE proveedores_insumos (proveedores_id integer,insumos_id integer,costo integer,detalle_insumo_id integer);
CREATE TABLE disenos (id serial,nombre varchar(30));
CREATE TABLE diseno_genero (genero_id integer,insumo_id integer);
CREATE TABLE genero(id serial,nombre varchar(30));
CREATE TABLE facturas (id serial,proveedor_id integer);
CREATE TABLE detalle_insumo (id serial, otros varchar(30),stock integer);
CREATE TABLE color_insumo (color_id integer,detalle_id integer);
CREATE TABLE colores (id serial,color varchar(10));
CREATE TABLE talla_insumo (talla_id integer, detalle_id integer);
CREATE TABLE tallas(id serial, talla varchar(5));


			"""

cur.execute(sql)
conn.commit()
cur.close()
conn.close()
