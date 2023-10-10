-- Cuboide base 3D
create view view_3D_nys as
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
create view view_2D_110 as
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
create view view_2D_101 as
select 
	name as albatros_id,
	'ALL' as año,
	season as temporada,
	st_convexhull(st_collect(geom)),
	st_area(st_convexhull(st_collect(geom))::geography)/10000 as ConvexHullArea_ha2
from albatros_seasons as2 
group by albatros_id, temporada;


-- all ID, año, temporadas
create view view_2D_011 as
select 
	'ALL' as albatros_id,
	substring(date, 1,4) as año,
	season as temporada,
	st_convexhull(st_collect(geom)),
	st_area(st_convexhull(st_collect(geom))::geography)/10000 as ConvexHullArea_ha2
from albatros_seasons as2 
group by año, season;

-- Cuboide 1D
create view view_1D_001 as
select 
	'ALL' as id,
	'ALL' as año,
	season as temporada,
	st_convexhull(st_collect(geom)),
	st_area(st_convexhull(st_collect(geom))::geography)/10000 as ConvexHullArea_ha2
from albatros_seasons as2 
group by temporada;

create view view_1D_010 as
select 
	'ALL' as id,
	substring(date, 1, 4)  as año,
	'ALL' as temporada,
	st_convexhull(st_collect(geom)),
	st_area(st_convexhull(st_collect(geom))::geography)/10000 as ConvexHullArea_ha2
from albatros_seasons as2 
group by año;

create view view_1D_100 as
select 
	name as id,
	'ALL' as año,
	'ALL' as temporada,
	st_convexhull(st_collect(geom)),
	st_area(st_convexhull(st_collect(geom))::geography)/10000 as ConvexHullArea_ha2
from albatros_seasons as2 
group by name;
