-- ----------------
-- CreateTables.sql
-- ----------------

-- https://www.w3schools.com/sql/sql_drop_table.asp
-- https://www.w3schools.com/sql/sql_create_table.asp
-- https://www.w3schools.com/sql/sql_primarykey.asp
-- https://www.w3schools.com/sql/sql_foreignkey.asp

use test;

-- -----------------------------------------------------------------------
select "*** drop table Apply ***" as "";
drop table if exists Apply;

/*
+--------------------------+
| *** drop table Apply *** |
+--------------------------+
*/

-- -----------------------------------------------------------------------
select "*** drop table College ***" as "";
drop table if exists College;

/*
+----------------------------+
| *** drop table College *** |
+----------------------------+
*/

-- -----------------------------------------------------------------------
select "*** drop table Student ***" as "";
drop table if exists Student;

/*
+----------------------------+
| *** drop table Student *** |
+----------------------------+
*/

-- -----------------------------------------------------------------------
select "*** create table Student ***" as "";
create table Student (
    sID         int not null,
    sName       text,
    GPA         float,
    sizeHS      int,
    primary key (sID))
    engine = innodb;

/*
+------------------------------+
| *** create table Student *** |
+------------------------------+
*/

-- -----------------------------------------------------------------------
select "*** create table College ***" as "";
create table College (
    cName       varchar(8) not null,
    state       char(2),
    enrollment  int,
    primary key (cName))
    engine = innodb;

/*
+------------------------------+
| *** create table College *** |
+------------------------------+
*/

-- -----------------------------------------------------------------------
select "*** create table Apply ***" as "";
create table Apply (
    sID         int,
    cName       varchar(8),
    major       text,
    decision    boolean,
    foreign key (sID)   references Student (sID),
    foreign key (cName) references College (cName))
    engine = innodb;

/*
+----------------------------+
| *** create table Apply *** |
+----------------------------+
*/

-- -----------------------------------------------------------------------
select "*** show tables ***" as "";
show tables;

/*
+---------------------+
| *** show tables *** |
+---------------------+
+----------------+
| Tables_in_test |
+----------------+
| Apply          |
| College        |
| Student        |
+----------------+
*/

-- -----------------------------------------------------------------------
select "*** describe Student ***" as "";
describe Student;

/*
+--------------------------+
| *** describe Student *** |
+--------------------------+
+--------+---------+------+-----+---------+-------+
| Field  | Type    | Null | Key | Default | Extra |
+--------+---------+------+-----+---------+-------+
| sID    | int(11) | NO   | PRI | NULL    |       |
| sName  | text    | YES  |     | NULL    |       |
| GPA    | float   | YES  |     | NULL    |       |
| sizeHS | int(11) | YES  |     | NULL    |       |
+--------+---------+------+-----+---------+-------+
*/

-- -----------------------------------------------------------------------
select "*** describe College ***" as "";
describe College;

/*
+--------------------------+
| *** describe College *** |
+--------------------------+
+------------+------------+------+-----+---------+-------+
| Field      | Type       | Null | Key | Default | Extra |
+------------+------------+------+-----+---------+-------+
| cName      | varchar(8) | NO   | PRI | NULL    |       |
| state      | char(2)    | YES  |     | NULL    |       |
| enrollment | int(11)    | YES  |     | NULL    |       |
+------------+------------+------+-----+---------+-------+
*/

-- -----------------------------------------------------------------------
select "*** describe Apply ***" as "";
describe Apply;

/*
+------------------------+
| *** describe Apply *** |
+------------------------+
+----------+------------+------+-----+---------+-------+
| Field    | Type       | Null | Key | Default | Extra |
+----------+------------+------+-----+---------+-------+
| sID      | int(11)    | YES  | MUL | NULL    |       |
| cName    | varchar(8) | YES  | MUL | NULL    |       |
| major    | text       | YES  |     | NULL    |       |
| decision | tinyint(1) | YES  |     | NULL    |       |
+----------+------------+------+-----+---------+-------+
*/

exit
