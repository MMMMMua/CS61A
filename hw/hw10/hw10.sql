-------------------------------------------------------------
                                                   -- DOGS --
-------------------------------------------------------------

create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
    -- PLEASE DO NOT CHANGE ANY DOG TABLES ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
  select sizes.size, dogs.name from sizes, dogs where sizes.min < dogs.height and dogs.height <= sizes.max;

-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
  select par.child from parents as par, dogs as dgs where par.parent = dgs.name order by dgs.height DESC;

-- Sentences about siblings that are the same size
create table sentences as
  select parents1.child || " and " || parents2.child || " are " || size1.size || " siblings"
  from parents as parents1, parents as parents2, size_of_dogs as size1, size_of_dogs as size2
  where parents1.parent = parents2.parent and size1.size = size2.size and parents1.child = size1.name
  and parents2.child = size2.name and parents1.child < parents2.child;

-- Heights and names of dogs that are above average in height among
-- dogs whose height has the same first digit.
create table above_average as
  with AVG as (
    select avg(height) as std, height-height%10 as tenth from dogs group by tenth
  )
  select dogs.height, dogs.name from dogs, AVG where dogs.height > AVG.std and dogs.height-dogs.height%10 = AVG.tenth;

-------------------------------------------------------------
                                     -- EUCLID CAFE TYCOON --
-------------------------------------------------------------

-- Locations of each cafe
create table cafes as
  select "nefeli" as name, 2 as location union
  select "brewed"        , 8             union
  select "hummingbird"   , 6;

-- Menu items at each cafe
create table menus as
  select "nefeli" as cafe, "espresso" as item union
  select "nefeli"        , "bagels"           union
  select "brewed"        , "coffee"           union
  select "brewed"        , "bagels"           union
  select "brewed"        , "muffins"          union
  select "hummingbird"   , "muffins"          union
  select "hummingbird"   , "eggs";

-- All locations on the block
create table locations as
  select 1 as n union
  select 2      union
  select 3      union
  select 4      union
  select 5      union
  select 6      union
  select 7      union
  select 8      union
  select 9      union
  select 10;

-------------------------------------------------------------
   -- PLEASE DO NOT CHANGE ANY CAFE TABLES ABOVE THIS LINE --
-------------------------------------------------------------

-- Locations without a cafe
create table open_locations as
    select n as n from cafes, locations where location != n
    group by n having count(*) = 3;

-- Items that could be placed on a menu at an open location
create table allowed as
  with item_locations(item, location) as (
    select item, location from cafes, menus where name = cafe
  )
  select n as n, item from locations as place, item_locations as food
  group by n, item having min(abs(n - location)) > 2;
