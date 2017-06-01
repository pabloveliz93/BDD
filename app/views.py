from app import app
from flask import render_template,request
from configuraciones import *

import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()


@app.route('/')
@app.route('/index')
def index():

	return render_template("index.html")


@app.route('/post/<post_id>', methods=['GET', 'POST'])
def post(post_id):
	if request.method == 'POST':
		comentario =  request.form['comentarios']
		print comentario
		sql = """ insert into comentarios  
		(post_id,usuario_id,creado,comentario) 
		values (%s,1,now(),'%s' ) """%(post_id,comentario)
		cur.execute(sql)


	sql ="""
	select id,titulo,texto from posts where id = %s
	"""%post_id
	print sql
	cur.execute(sql)
	post  = cur.fetchone()

	sql ="""
	select id,nombre from categorias,categorias_posts 
	where categorias_posts.categoria_id = categorias.id 
	and post_id = %s 
	"""%(post_id)
	print sql
	cur.execute(sql)
	categorias  = cur.fetchall()

	sql ="""
	select comentarios.id,nombre,apellido,comentario
	
	from usuarios,comentarios 
	where comentarios.usuario_id = usuarios.id 
	and post_id = %s order by id desc
	"""%(post_id)
	print sql
	cur.execute(sql)
	comentarios  = cur.fetchall()


	return render_template("post.html",post= post,categorias=categorias,comentarios= comentarios) 






