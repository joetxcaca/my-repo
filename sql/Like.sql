-- --------
-- Like.sql
-- --------

-- https://www.w3schools.com/sql/sql_between.asp
-- https://www.w3schools.com/sql/sql_count_avg_sum.asp
-- https://www.w3schools.com/sql/sql_in.asp
-- https://www.w3schools.com/sql/sql_like.asp
-- https://www.w3schools.com/sql/sql_min_max.asp

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
-- students whose names end in "y"
select "*** query #1 ***" as "";
select *
    from Student
    where sName like "%y";

/*
+------------------+
| *** query #1 *** |
+------------------+
+-----+-------+------+--------+
| sID | sName | GPA  | sizeHS |
+-----+-------+------+--------+
| 123 | Amy   |  3.9 |   1000 |
| 321 | Mary  |  2.5 |   1200 |
| 654 | Amy   |  3.9 |   1000 |
| 678 | Fay   |  3.8 |    200 |
| 765 | Jay   |  2.9 |   1500 |
| 789 | Gary  |  3.4 |    800 |
+-----+-------+------+--------+
*/

-- -----------------------------------------------------------------------
-- students whose names have three letters and end in "y"
select "*** query #2 ***" as "";
select *
    from Student
    where sName like "__y";

/*
+------------------+
| *** query #2 *** |
+------------------+
+-----+-------+------+--------+
| sID | sName | GPA  | sizeHS |
+-----+-------+------+--------+
| 123 | Amy   |  3.9 |   1000 |
| 654 | Amy   |  3.9 |   1000 |
| 678 | Fay   |  3.8 |    200 |
| 765 | Jay   |  2.9 |   1500 |
+-----+-------+------+--------+
*/

-- -----------------------------------------------------------------------
-- students whose names are "Amy" or "Jay" or "Mary"
select "*** query #3 ***" as "";
select *
    from Student
    where sName = "Amy" or sName = "Jay" or sName = "Mary";

/*
+------------------+
| *** query #3 *** |
+------------------+
+-----+-------+------+--------+
| sID | sName | GPA  | sizeHS |
+-----+-------+------+--------+
| 123 | Amy   |  3.9 |   1000 |
| 321 | Mary  |  2.5 |   1200 |
| 654 | Amy   |  3.9 |   1000 |
| 765 | Jay   |  2.9 |   1500 |
+-----+-------+------+--------+
*/

-- -----------------------------------------------------------------------
-- students whose names are "Amy" or "Jay" or "Mary"
select "*** query #4 ***" as "";
select *
    from Student
    where sName in ("Amy", "Jay", "Mary");

/*
+------------------+
| *** query #4 *** |
+------------------+
+-----+-------+------+--------+
| sID | sName | GPA  | sizeHS |
+-----+-------+------+--------+
| 123 | Amy   |  3.9 |   1000 |
| 321 | Mary  |  2.5 |   1200 |
| 654 | Amy   |  3.9 |   1000 |
| 765 | Jay   |  2.9 |   1500 |
+-----+-------+------+--------+
*/

-- -----------------------------------------------------------------------
-- colleges whose enrollment is between 20,000 and 30,000
select "*** query #5 ***" as "";
select *
    from College
    where enrollment > 20000 and enrollment < 30000;

/*
+------------------+
| *** query #5 *** |
+------------------+
+---------+-------+------------+
| cName   | state | enrollment |
+---------+-------+------------+
| A&M     | TX    |      25000 |
| Cornell | NY    |      21000 |
+---------+-------+------------+
*/

-- -----------------------------------------------------------------------
-- colleges whose enrollment is between 20,000 and 30,000
select "*** query #6 ***" as "";
select *
    from College
    where enrollment between 20000 and 30000;

/*
+------------------+
| *** query #6 *** |
+------------------+
+---------+-------+------------+
| cName   | state | enrollment |
+---------+-------+------------+
| A&M     | TX    |      25000 |
| Cornell | NY    |      21000 |
+---------+-------+------------+
*/

-- -----------------------------------------------------------------------
-- number of colleges
select "*** query #7 ***" as "";
select count(*)
    from College;

/*
+------------------+
| *** query #7 *** |
+------------------+
+----------+
| count(*) |
+----------+
|        6 |
+----------+
*/

-- -----------------------------------------------------------------------
-- smallest, largest, average, and total enrollment of colleges
select "*** query #8 ***" as "";
select min(enrollment), max(enrollment), avg(enrollment), sum(enrollment)
    from College;

/*
+------------------+
| *** query #8 *** |
+------------------+
+-----------------+-----------------+-----------------+-----------------+
| min(enrollment) | max(enrollment) | avg(enrollment) | sum(enrollment) |
+-----------------+-----------------+-----------------+-----------------+
|           10000 |           36000 |      23833.3333 |          143000 |
+-----------------+-----------------+-----------------+-----------------+
*/

-- -----------------------------------------------------------------------
-- smallest, largest, average, and total enrollment of colleges by state
select "*** query #9 ***" as "";
select state, count(*), min(enrollment), max(enrollment), avg(enrollment), sum(enrollment)
    from College
    group by state;

/*
+------------------+
| *** query #9 *** |
+------------------+
+-------+----------+-----------------+-----------------+-----------------+-----------------+
| state | count(*) | min(enrollment) | max(enrollment) | avg(enrollment) | sum(enrollment) |
+-------+----------+-----------------+-----------------+-----------------+-----------------+
| TX    |        1 |           25000 |           25000 |      25000.0000 |           25000 |
| CA    |        2 |           15000 |           36000 |      25500.0000 |           51000 |
| NY    |        1 |           21000 |           21000 |      21000.0000 |           21000 |
| MA    |        1 |           10000 |           10000 |      10000.0000 |           10000 |
| FL    |        1 |           36000 |           36000 |      36000.0000 |           36000 |
+-------+----------+-----------------+-----------------+-----------------+-----------------+
*/

-- -----------------------------------------------------------------------
-- smallest, largest, average, and total enrollment of colleges by state, if state has 2 or more colleges
select "*** query #10 ***" as "";
select state, count(*), min(enrollment), max(enrollment), avg(enrollment), sum(enrollment)
    from College
    group by state
    having count(*) >= 2;

/*
+-------------------+
| *** query #10 *** |
+-------------------+
+-------+----------+-----------------+-----------------+-----------------+-----------------+
| state | count(*) | min(enrollment) | max(enrollment) | avg(enrollment) | sum(enrollment) |
+-------+----------+-----------------+-----------------+-----------------+-----------------+
| CA    |        2 |           15000 |           36000 |      25500.0000 |           51000 |
+-------+----------+-----------------+-----------------+-----------------+-----------------+
*/

exit
