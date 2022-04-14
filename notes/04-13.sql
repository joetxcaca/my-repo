-- -----------
-- Wed, 13 Apr
-- -----------

/*
Paper #11: More getters and setters
remember to go to Perusall THROUGH Canvas
*/

/*
Takeaways:

 1. assertions are not good for testing
 2. assertions are not good for user errors
 3. frozenset, str, tuple are immutable in content and size
 4. set is immutable in content
 5. iter on an iterator returns itself
 6. iterators are exhaustible, containers are not
 7. generators are iterators
 8. generators and map and filter capture objects!!!
 9. lambdas capture names!!!
10. avoid mutable defaults
11. relational algebra is closed on all operations
12. Python, C, Java are procedural; SQL is declarative
*/

/*
SQL

declarative, as opposed to a procedural (C, Java, Python)
*/






--  -----------------
--  ShowDatabases.sql
--  -----------------

--  https://www.mysql.com

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
+--------------------+
*/

exit

/*
% which mysql
/usr/local/bin/mysql



% mysql --version
mysql  Ver 8.0.28 for macos12.2 on x86_64 (Homebrew)
%



% mysql.server status
 ERROR! MySQL is not running



% mysql.server start
Starting MySQL
. SUCCESS!



% mysql.server status
 SUCCESS! MySQL running (1378)



% mysql -u root
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 10
Server version: 8.0.28 Homebrew

Copyright (c) 2000, 2022, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> help

For information about MySQL products and services, visit:
   http://www.mysql.com/
For developer information, including the MySQL Reference Manual, visit:
   http://dev.mysql.com/
To buy MySQL Enterprise support, training, or other products, visit:
   https://shop.mysql.com/

List of all MySQL commands:
Note that all text commands must be first on line and end with ';'
?         (\?) Synonym for `help'.
clear     (\c) Clear the current input statement.
connect   (\r) Reconnect to the server. Optional arguments are db and host.
delimiter (\d) Set statement delimiter.
edit      (\e) Edit command with $EDITOR.
ego       (\G) Send command to mysql server, display result vertically.
exit      (\q) Exit mysql. Same as quit.
go        (\g) Send command to mysql server.
help      (\h) Display this help.
nopager   (\n) Disable pager, print to stdout.
notee     (\t) Don't write into outfile.
pager     (\P) Set PAGER [to_pager]. Print the query results via PAGER.
print     (\p) Print current command.
prompt    (\R) Change your mysql prompt.
quit      (\q) Quit mysql.
rehash    (\#) Rebuild completion hash.
source    (\.) Execute an SQL script file. Takes a file name as an argument.
status    (\s) Get status information from the server.
system    (\!) Execute a system shell command.
tee       (\T) Set outfile [to_outfile]. Append everything into given outfile.
use       (\u) Use another database. Takes database name as argument.
charset   (\C) Switch to another charset. Might be needed for processing binlog with multi-byte charsets.
warnings  (\W) Show warnings after every statement.
nowarning (\w) Don't show warnings after every statement.
resetconnection(\x) Clean session context.

For server side help, type 'help contents'

mysql> quit
Bye
%



% mysql -u root -t < ShowDatabases.sql > ShowDatabases.out



% mysql.server stop
Shutting down MySQL
. SUCCESS!



% mysql.server status
 ERROR! MySQL is not running
*/















--  ---------------
--  ShowEngines.sql
--  ---------------

select "*** show engines ***" as "";
show engines;

/*
+----------------------+
| *** show engines *** |
+----------------------+
+--------------------+---------+----------------------------------------------------------------+--------------+------+------------+
| Engine             | Support | Comment                                                        | Transactions | XA   | Savepoints |
+--------------------+---------+----------------------------------------------------------------+--------------+------+------------+
| ARCHIVE            | YES     | Archive storage engine                                         | NO           | NO   | NO         |
| BLACKHOLE          | YES     | /dev/null storage engine (anything you write to it disappears) | NO           | NO   | NO         |
| MRG_MYISAM         | YES     | Collection of identical MyISAM tables                          | NO           | NO   | NO         |
| FEDERATED          | NO      | Federated MySQL storage engine                                 | NULL         | NULL | NULL       |
| MyISAM             | YES     | MyISAM storage engine                                          | NO           | NO   | NO         |
| PERFORMANCE_SCHEMA | YES     | Performance Schema                                             | NO           | NO   | NO         |
| InnoDB             | DEFAULT | Supports transactions, row-level locking, and foreign keys     | YES          | YES  | YES        |
| MEMORY             | YES     | Hash based, stored in memory, useful for temporary tables      | NO           | NO   | NO         |
| CSV                | YES     | CSV storage engine                                             | NO           | NO   | NO         |
+--------------------+---------+----------------------------------------------------------------+--------------+------+------------+
*/

exit


/*
movie table

title       director         year genre
"star wars" "george lucas"   1977 "sci-fi"
"giant"     "george stevens" 1956 "western"
...
*/



/*
director table

director_id director_name     // primary keys
1           "george lucas"
2           "george stevens"
*/

/*
genre table

genre_id genre_name // primary keys
1        "sci-fi"
2        "western"
*/

/*
movie table

title       director_id year genre_id // foreign keys
"star wars" 1           1977 1
"giant"     2           1956 2
*/

/*
foreign key support
	1. dictates a creation order
	2. dictates a tear down order
	3. validates the foreign keys
*/






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








-- ----------
-- Insert.sql
-- ----------

-- https://www.w3schools.com/sql/sql_insert.asp

use test;

-- -----------------------------------------------------------------------
select "*** insert Student ***" as "";
insert into Student values (123, "Amy",    3.9,  1000);
insert into Student values (234, "Bob",    3.6,  1500);
insert into Student values (320, "Lori",   null, 2500);
insert into Student values (321, "Mary",   2.5,  1200);
insert into Student values (345, "Craig",  3.5,   500);
insert into Student values (432, "Kevin",  null, 1500);
insert into Student values (456, "Doris",  3.9,  1000);
insert into Student values (543, "Craig",  3.4,  2000);
insert into Student values (567, "Edward", 2.9,  2000);
insert into Student values (654, "Amy",    3.9,  1000);
insert into Student values (678, "Fay",    3.8,   200);
insert into Student values (765, "Jay",    2.9,  1500);
insert into Student values (789, "Gary",   3.4,   800);
insert into Student values (876, "Irene",  3.9,   400);
insert into Student values (987, "Helen",  3.7,   800);

/*
+------------------------+
| *** insert Student *** |
+------------------------+
*/

-- -----------------------------------------------------------------------
select "*** insert College ***" as "";
insert into College values ("A&M",      "TX", 25000);
insert into College values ("Berkeley", "CA", 36000);
insert into College values ("Cornell",  "NY", 21000);
insert into College values ("MIT",      "MA", 10000);
insert into College values ("Stanford", "CA", 15000);
insert into College values ("UCF",      "FL", 36000);

/*
+------------------------+
| *** insert College *** |
+------------------------+
*/

-- -----------------------------------------------------------------------
select "*** insert Apply ***" as "";
insert into Apply values (123, "Berkeley", "CS",             true);
insert into Apply values (123, "Cornell",  "EE",             true);
insert into Apply values (123, "Stanford", "CS",             true);
insert into Apply values (123, "Stanford", "EE",             false);
insert into Apply values (234, "Berkeley", "biology",        false);
insert into Apply values (321, "MIT",      "history",        false);
insert into Apply values (321, "MIT",      "psychology",     true);
insert into Apply values (345, "Cornell",  "bioengineering", false);
insert into Apply values (345, "Cornell",  "CS",             true);
insert into Apply values (345, "Cornell",  "EE",             false);
insert into Apply values (345, "MIT",      "bioengineering", true);
insert into Apply values (543, "MIT",      "CS",             false);
insert into Apply values (678, "Stanford", "history",        true);
insert into Apply values (765, "Cornell",  "history",        false);
insert into Apply values (765, "Cornell",  "psychology",     true);
insert into Apply values (765, "Stanford", "history",        true);
insert into Apply values (876, "MIT",      "biology",        true);
insert into Apply values (876, "MIT",      "marine biology", false);
insert into Apply values (876, "Stanford", "CS",             false);
insert into Apply values (987, "Berkeley", "CS",             true);
insert into Apply values (987, "Stanford", "CS",             true);

/*
+----------------------+
| *** insert Apply *** |
+----------------------+
*/

-- -----------------------------------------------------------------------
select "*** show Student ***" as "";
select * from Student;

/*
+----------------------+
| *** show Student *** |
+----------------------+
+-----+--------+------+--------+
| sID | sName  | GPA  | sizeHS |
+-----+--------+------+--------+
| 123 | Amy    |  3.9 |   1000 |
| 234 | Bob    |  3.6 |   1500 |
| 320 | Lori   | NULL |   2500 |
| 321 | Mary   |  2.5 |   1200 |
| 345 | Craig  |  3.5 |    500 |
| 432 | Kevin  | NULL |   1500 |
| 456 | Doris  |  3.9 |   1000 |
| 543 | Craig  |  3.4 |   2000 |
| 567 | Edward |  2.9 |   2000 |
| 654 | Amy    |  3.9 |   1000 |
| 678 | Fay    |  3.8 |    200 |
| 765 | Jay    |  2.9 |   1500 |
| 789 | Gary   |  3.4 |    800 |
| 876 | Irene  |  3.9 |    400 |
| 987 | Helen  |  3.7 |    800 |
+-----+--------+------+--------+
*/

-- -----------------------------------------------------------------------
select "*** show College ***" as "";
select * from College;

/*
+----------------------+
| *** show College *** |
+----------------------+
+----------+-------+------------+
| cName    | state | enrollment |
+----------+-------+------------+
| A&M      | TX    |      25000 |
| Berkeley | CA    |      36000 |
| Cornell  | NY    |      21000 |
| MIT      | MA    |      10000 |
| Stanford | CA    |      15000 |
| UCF      | FL    |      36000 |
+----------+-------+------------+
*/

-- -----------------------------------------------------------------------
select "*** show Apply ***" as "";
select * from Apply;

/*
+--------------------+
| *** show Apply *** |
+--------------------+
+------+----------+----------------+----------+
| sID  | cName    | major          | decision |
+------+----------+----------------+----------+
|  123 | Berkeley | CS             |        1 |
|  123 | Cornell  | EE             |        1 |
|  123 | Stanford | CS             |        1 |
|  123 | Stanford | EE             |        0 |
|  234 | Berkeley | biology        |        0 |
|  321 | MIT      | history        |        0 |
|  321 | MIT      | psychology     |        1 |
|  345 | Cornell  | bioengineering |        0 |
|  345 | Cornell  | CS             |        1 |
|  345 | Cornell  | EE             |        0 |
|  345 | MIT      | bioengineering |        1 |
|  543 | MIT      | CS             |        0 |
|  678 | Stanford | history        |        1 |
|  765 | Cornell  | history        |        0 |
|  765 | Cornell  | psychology     |        1 |
|  765 | Stanford | history        |        1 |
|  876 | MIT      | biology        |        1 |
|  876 | MIT      | marine biology |        0 |
|  876 | Stanford | CS             |        0 |
|  987 | Berkeley | CS             |        1 |
|  987 | Stanford | CS             |        1 |
+------+----------+----------------+----------+
*/

exit









-- ----------
-- Select.sql
-- ----------

-- https://www.w3schools.com/sql/sql_select.asp
-- https://www.w3schools.com/sql/sql_distinct.asp
-- https://www.w3schools.com/sql/sql_orderby.asp

use test;

-- -----------------------------------------------------------------------
select "*** show Student ***" as "";
select * from Student;

/*
+----------------------+
| *** show Student *** |
+----------------------+
+-----+--------+------+--------+
| sID | sName  | GPA  | sizeHS |
+-----+--------+------+--------+
| 123 | Amy    |  3.9 |   1000 |
| 234 | Bob    |  3.6 |   1500 |
| 320 | Lori   | NULL |   2500 |
| 321 | Mary   |  2.5 |   1200 |
| 345 | Craig  |  3.5 |    500 |
| 432 | Kevin  | NULL |   1500 |
| 456 | Doris  |  3.9 |   1000 |
| 543 | Craig  |  3.4 |   2000 |
| 567 | Edward |  2.9 |   2000 |
| 654 | Amy    |  3.9 |   1000 |
| 678 | Fay    |  3.8 |    200 |
| 765 | Jay    |  2.9 |   1500 |
| 789 | Gary   |  3.4 |    800 |
| 876 | Irene  |  3.9 |    400 |
| 987 | Helen  |  3.7 |    800 |
+-----+--------+------+--------+
*/

-- -----------------------------------------------------------------------
select "*** show College ***" as "";
select * from College;

/*
+----------------------+
| *** show College *** |
+----------------------+
+----------+-------+------------+
| cName    | state | enrollment |
+----------+-------+------------+
| A&M      | TX    |      25000 |
| Berkeley | CA    |      36000 |
| Cornell  | NY    |      21000 |
| MIT      | MA    |      10000 |
| Stanford | CA    |      15000 |
| UCF      | FL    |      36000 |
+----------+-------+------------+
*/

-- -----------------------------------------------------------------------
select "*** show Apply ***" as "";
select * from Apply;

/*
+--------------------+
| *** show Apply *** |
+--------------------+
+------+----------+----------------+----------+
| sID  | cName    | major          | decision |
+------+----------+----------------+----------+
|  123 | Berkeley | CS             |        1 |
|  123 | Cornell  | EE             |        1 |
|  123 | Stanford | CS             |        1 |
|  123 | Stanford | EE             |        0 |
|  234 | Berkeley | biology        |        0 |
|  321 | MIT      | history        |        0 |
|  321 | MIT      | psychology     |        1 |
|  345 | Cornell  | bioengineering |        0 |
|  345 | Cornell  | CS             |        1 |
|  345 | Cornell  | EE             |        0 |
|  345 | MIT      | bioengineering |        1 |
|  543 | MIT      | CS             |        0 |
|  678 | Stanford | history        |        1 |
|  765 | Cornell  | history        |        0 |
|  765 | Cornell  | psychology     |        1 |
|  765 | Stanford | history        |        1 |
|  876 | MIT      | biology        |        1 |
|  876 | MIT      | marine biology |        0 |
|  876 | Stanford | CS             |        0 |
|  987 | Berkeley | CS             |        1 |
|  987 | Stanford | CS             |        1 |
+------+----------+----------------+----------+
*/

-- -----------------------------------------------------------------------
-- relational algebra select
select "*** query #1 ***" as "";
select *
    from Student
    where (GPA > 3.7);

/*
+------------------+
| *** query #1 *** |
+------------------+
+-----+-------+------+--------+
| sID | sName | GPA  | sizeHS |
+-----+-------+------+--------+
| 123 | Amy   |  3.9 |   1000 |
| 456 | Doris |  3.9 |   1000 |
| 654 | Amy   |  3.9 |   1000 |
| 678 | Fay   |  3.8 |    200 |
| 876 | Irene |  3.9 |    400 |
| 987 | Helen |  3.7 |    800 |
+-----+-------+------+--------+
*/

-- -----------------------------------------------------------------------
-- relational algebra select
select "*** query #2 ***" as "";
select *
    from Student
    where (GPA > 3.7) and (sizeHS < 1000);

/*
+------------------+
| *** query #2 *** |
+------------------+
+-----+-------+------+--------+
| sID | sName | GPA  | sizeHS |
+-----+-------+------+--------+
| 678 | Fay   |  3.8 |    200 |
| 876 | Irene |  3.9 |    400 |
| 987 | Helen |  3.7 |    800 |
+-----+-------+------+--------+
*/

-- -----------------------------------------------------------------------
-- relational algebra select
select "*** query #3 ***" as "";
select *
    from Apply
    where (cName = "Stanford") and (major = "CS");

/*
+------------------+
| *** query #3 *** |
+------------------+
+------+----------+-------+----------+
| sID  | cName    | major | decision |
+------+----------+-------+----------+
|  123 | Stanford | CS    |        1 |
|  876 | Stanford | CS    |        0 |
|  987 | Stanford | CS    |        1 |
+------+----------+-------+----------+
*/

-- -----------------------------------------------------------------------
-- relational algebra project
select "*** query #4 ***" as "";
select sID, decision
    from Apply;

/*
+------------------+
| *** query #4 *** |
+------------------+
+------+----------+
| sID  | decision |
+------+----------+
|  123 |        1 |
|  123 |        1 |
|  123 |        1 |
|  123 |        0 |
|  234 |        0 |
|  321 |        0 |
|  321 |        1 |
|  345 |        0 |
|  345 |        1 |
|  345 |        0 |
|  345 |        1 |
|  543 |        0 |
|  678 |        1 |
|  765 |        0 |
|  765 |        1 |
|  765 |        1 |
|  876 |        1 |
|  876 |        0 |
|  876 |        0 |
|  987 |        1 |
|  987 |        1 |
+------+----------+
*/

-- -----------------------------------------------------------------------
-- relational algebra select and project
select "*** query #5 ***" as "";
select sID, sName
    from Student
    where (GPA > 3.7);

/*
+------------------+
| *** query #5 *** |
+------------------+
+-----+-------+
| sID | sName |
+-----+-------+
| 123 | Amy   |
| 456 | Doris |
| 654 | Amy   |
| 678 | Fay   |
| 876 | Irene |
| 987 | Helen |
+-----+-------+
*/

-- -----------------------------------------------------------------------
-- relational algebra project, sort ascending, and limit
select "*** query #6 ***" as "";
select major, decision
    from Apply
    order by major
    limit 6;

/*
+------------------+
| *** query #6 *** |
+------------------+
+----------------+----------+
| major          | decision |
+----------------+----------+
| bioengineering |        0 |
| bioengineering |        1 |
| biology        |        0 |
| biology        |        1 |
| CS             |        1 |
| CS             |        1 |
+----------------+----------+
*/

-- -----------------------------------------------------------------------
-- relational algebra project, uniquely, and sort descending
select "*** query #7 ***" as "";
select distinct major, decision
    from Apply
    order by major desc;

/*
+------------------+
| *** query #7 *** |
+------------------+
+----------------+----------+
| major          | decision |
+----------------+----------+
| psychology     |        1 |
| marine biology |        0 |
| history        |        0 |
| history        |        1 |
| EE             |        0 |
| EE             |        1 |
| CS             |        0 |
| CS             |        1 |
| biology        |        0 |
| biology        |        1 |
| bioengineering |        0 |
| bioengineering |        1 |
+----------------+----------+
*/

exit
