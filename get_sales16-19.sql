show databases;
use liquorsales;
show tables;

select * from finance_liquor_sales
order by date;

select *
from finance_liquor_sales
where date >= '2016-01-01 00:00:00' and date < '2020-01-01 00:00:00'
order by date
