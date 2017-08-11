create table ns as
  with t(n) as (select 0 union select n+1 from t where n < 99)
  select * from t;

create table ps as select n from ns where n > 0;

create table gg as select c1.n * 100 + c2.n from ns as c1, ns as c2 where c1.n >= 20;
