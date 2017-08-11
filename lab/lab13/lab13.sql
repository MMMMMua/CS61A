.read sp17data.sql
.read su17data.sql

CREATE TABLE obedience AS
	select seven, image from students;

CREATE TABLE smallest_int AS
  select time, smallest from students
	where smallest > 5 order by smallest limit 20;

CREATE TABLE greatstudents AS
  select sp17.date, sp17.color, sp17.pet, su17.number, sp17.number
	from sp17students as sp17, students as su17 where
	sp17.date = su17.date and sp17.color = su17.color and sp17.pet = su17.pet;

CREATE TABLE sevens AS
  select stu.seven from students as stu, checkboxes as chk where
	stu.number = 7 and chk.'7' = "True" and stu.time = chk.time;

CREATE TABLE matchmaker AS
  select stu1.pet, stu1.beets, stu1.color, stu2.color from
	students as stu1, students as stu2 where stu1.time < stu2.time and
	stu1.pet = stu2.pet and stu1.beets = stu2.beets;
