--  ------------------
--  CreateDatabase.sql
--  ------------------

-- https://www.w3schools.com/sql/sql_create_db.asp

-- -----------------------------------------------------------------------
select "*** drop database test ***" as "";
drop database if exists test;

/*
+----------------------------+
| *** drop database test *** |
+----------------------------+
*/

-- -----------------------------------------------------------------------
select "*** create database test ***" as "";
create database test;

/*
+------------------------------+
| *** create database test *** |
+------------------------------+
*/

-- -----------------------------------------------------------------------
select "*** show databases ***" as "";
show databases;

/*
+------------------------+
| *** show databases *** |
+------------------------+
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| test               |
+--------------------+
*/

exit
