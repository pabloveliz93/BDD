30)
select sum(monto)
from (
	select rut,count(*)
	from clientes as c,ventas as v
	where c.rut=v.rut_cliente
	group by rut
	)
	as first,ventas
where count= (
			select max(count)
			from (
				select rut,count(*)
				from clientes as c,ventas as v
				where c.rut=v.rut_cliente
				group by rut
				)
				as first
			)
and ventas.rut_cliente = first.rut;
31)
select numdep,sum(sueldo)
from empleados
group by numdep;
32)
select count(*) 
from empleados e,grados g 
where e.sueldo>sueldo_inf
and e.sueldo<sueldo_sup
and grado=2;
33)
select comuna,sum(monto)
from clientes c,ventas v 
where c.rut=v.rut_cliente
group by comuna;
34)
select nombre, sum(precio * cantidad) 
from ventas_detalle vd,productos p
where vd.cod_producto=p.codigo
group by nombre;
35)
select count(*)
from(
	select rut,count(rut)
	from ventas v,ventas_detalle vd,productos p,clientes c 
	where v.num_venta=vd.num_venta
	and vd.cod_producto=p.codigo
	and p.nombre= 'mesa'
	and c.rut=v.rut_cliente
	group by rut
	) as t1
;
36)
select t1.nombre
from (
	select d.nombre,count(*)
	from deptos d,empleados e
	where e.numdep=d.numdep
	group by d.nombre
	) as t1
where t1.count=(
	select max(count)
	from(
		select count(*)
		from deptos d, empleados e
		where e.numdep=d.numdep
		group by d.nombre
		) as t2
	);
