-- Cuboide base 4D
select
	name as albatros_id,
	substring(date, 1, 4)  as año,
	season as temporada,
	st_convexhull(st_collect(geom)),
	st_area(st_convexhull(st_collect(geom))::geography)/10000 as ConvexHullArea_ha2
from albatros_seasons as2
group by albatros_id, año, temporada

-- Cuboides 2D
-- ID, año, all temporadas
select 
	name as albatros_id,
	substring(date, 1, 4) as año,
	'ALL' as temporada,
	st_convexhull(st_collect(geom)),
	st_area(
	st_convexhull(st_collect(geom))::geography)/10000 as ConvexHullArea_ha2
from albatros_seasons as2 
group by albatros_id, año
order by ConvexHullArea_ha2 desc;

-- ID, all año,temporadas
select 
	name as albatros_id,
	'ALL' as año,
	season as temporada,
	st_convexhull(st_collect(geom)),
	st_area(st_convexhull(st_collect(geom))::geography)/10000 as ConvexHullArea_ha2
from albatros_seasons as2 
group by albatros_id, temporada;


-- all ID, año, all posición, temporadas
select 
	'ALL' as albatros_id,
	substring(date, 1,4) as año,
	'ALL' as posición,
	season as temporada,
	st_convexhull(st_collect(geom)),
	st_area(st_convexhull(st_collect(geom))::geography)/10000 as ConvexHullArea_ha2
from albatros_seasons as2 
group by año, season;

-- all ID, all año, posición, temporadas
select 
	'ALL' as albatros_id,
	'ALL' as año,
	season as temporada,
	st_convexhull(st_collect(geom)),
	st_area(st_convexhull(st_collect(geom))::geography)/10000 as ConvexHullArea_ha2
from albatros_seasons as2 
group by posición, temporada
order by temporada;

-- Cuboide 1D

select 
	'ALL' as id,
	'ALL' as año,
	season as temporada,
	st_convexhull(st_collect(geom)),
	st_area(st_convexhull(st_collect(geom))::geography)/10000 as ConvexHullArea_ha2
from albatros_seasons as2 
group by temporada;

select 
	'ALL' as id,
	substring(date, 1, 4)  as año,
	'ALL' as temporada,
	st_convexhull(st_collect(geom)),
	st_area(st_convexhull(st_collect(geom))::geography)/10000 as ConvexHullArea_ha2
from albatros_seasons as2 
group by año;

select 
	name as id,
	'ALL' as año,
	'ALL' as temporada,
	st_convexhull(st_collect(geom)),
	st_area(st_convexhull(st_collect(geom))::geography)/10000 as ConvexHullArea_ha2
from albatros_seasons as2 
group by name;
