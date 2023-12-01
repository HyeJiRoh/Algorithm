select f.FLAVOR from FIRST_HALF f
inner join ICECREAM_INFO i
on f.FLAVOR = i.FLAVOR
where f.TOTAL_ORDER >= 3000
and i.INGREDIENT_TYPE = 'fruit_based'
order by TOTAL_ORDER desc