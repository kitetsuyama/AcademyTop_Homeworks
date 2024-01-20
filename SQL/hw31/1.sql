select city, email, category from "2gis_businesses"
where city like "Москва"
and email not like "null"
and (category like "Кафе%" or category like "%магазин%")