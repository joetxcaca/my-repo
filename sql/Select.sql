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
