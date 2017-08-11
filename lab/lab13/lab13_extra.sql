.read lab13.sql

CREATE TABLE sp17favnum AS
  select number, count(*) as cnt from sp17students
  group by number order by cnt DESC limit 1;


CREATE TABLE sp17favpets AS
  select pet, count(*) as cnt from sp17students
  group by pet order by count(*) DESC limit 10;


CREATE TABLE su17favpets AS
  select pet, count(*) as cnt from students
  group by pet order by cnt DESC limit 10;

CREATE TABLE su17dog AS
  select pet, count(*) from students
  group by pet having pet = "dog";


CREATE TABLE su17alldogs AS
  select "doggo", count(*) from students
  where pet like "%dog%";


CREATE TABLE obedienceimage AS
  select seven, image, count(*) from students
  where seven = "7" group by image;

CREATE TABLE smallest_int_count AS
  select smallest, count(*) as cnt from students group by smallest
  order by smallest;
