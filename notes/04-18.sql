-- -----------
-- Mon, 18 Apr
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
*/

-- --------
-- Join.sql
-- --------

-- https://www.w3schools.com/sql/sql_join_inner.asp
-- https://www.w3schools.com/sql/sql_join.asp

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
-- relational algebra cross join
select "*** query #1 ***" as "";
select *
    from Student
    cross join Apply
    order by Student.sID;

/*
+------------------+
| *** query #1 *** |
+------------------+
+-----+--------+------+--------+------+----------+----------------+----------+
| sID | sName  | GPA  | sizeHS | sID  | cName    | major          | decision |
+-----+--------+------+--------+------+----------+----------------+----------+
| 123 | Amy    |  3.9 |   1000 |  321 | MIT      | history        |        0 |
| 123 | Amy    |  3.9 |   1000 |  765 | Cornell  | history        |        0 |
| 123 | Amy    |  3.9 |   1000 |  234 | Berkeley | biology        |        0 |
| 123 | Amy    |  3.9 |   1000 |  678 | Stanford | history        |        1 |
| 123 | Amy    |  3.9 |   1000 |  987 | Stanford | CS             |        1 |
| 123 | Amy    |  3.9 |   1000 |  123 | Stanford | EE             |        0 |
| 123 | Amy    |  3.9 |   1000 |  543 | MIT      | CS             |        0 |
| 123 | Amy    |  3.9 |   1000 |  987 | Berkeley | CS             |        1 |
| 123 | Amy    |  3.9 |   1000 |  123 | Stanford | CS             |        1 |
| 123 | Amy    |  3.9 |   1000 |  345 | MIT      | bioengineering |        1 |
| 123 | Amy    |  3.9 |   1000 |  876 | Stanford | CS             |        0 |
| 123 | Amy    |  3.9 |   1000 |  123 | Cornell  | EE             |        1 |
| 123 | Amy    |  3.9 |   1000 |  345 | Cornell  | EE             |        0 |
| 123 | Amy    |  3.9 |   1000 |  876 | MIT      | marine biology |        0 |
| 123 | Amy    |  3.9 |   1000 |  123 | Berkeley | CS             |        1 |
| 123 | Amy    |  3.9 |   1000 |  345 | Cornell  | CS             |        1 |
| 123 | Amy    |  3.9 |   1000 |  876 | MIT      | biology        |        1 |
| 123 | Amy    |  3.9 |   1000 |  345 | Cornell  | bioengineering |        0 |
| 123 | Amy    |  3.9 |   1000 |  765 | Stanford | history        |        1 |
| 123 | Amy    |  3.9 |   1000 |  321 | MIT      | psychology     |        1 |
| 123 | Amy    |  3.9 |   1000 |  765 | Cornell  | psychology     |        1 |
| 234 | Bob    |  3.6 |   1500 |  321 | MIT      | psychology     |        1 |
| 234 | Bob    |  3.6 |   1500 |  765 | Cornell  | psychology     |        1 |
| 234 | Bob    |  3.6 |   1500 |  321 | MIT      | history        |        0 |
| 234 | Bob    |  3.6 |   1500 |  765 | Cornell  | history        |        0 |
| 234 | Bob    |  3.6 |   1500 |  234 | Berkeley | biology        |        0 |
| 234 | Bob    |  3.6 |   1500 |  678 | Stanford | history        |        1 |
| 234 | Bob    |  3.6 |   1500 |  987 | Stanford | CS             |        1 |
| 234 | Bob    |  3.6 |   1500 |  123 | Stanford | EE             |        0 |
| 234 | Bob    |  3.6 |   1500 |  543 | MIT      | CS             |        0 |
| 234 | Bob    |  3.6 |   1500 |  987 | Berkeley | CS             |        1 |
| 234 | Bob    |  3.6 |   1500 |  123 | Stanford | CS             |        1 |
| 234 | Bob    |  3.6 |   1500 |  345 | MIT      | bioengineering |        1 |
| 234 | Bob    |  3.6 |   1500 |  876 | Stanford | CS             |        0 |
| 234 | Bob    |  3.6 |   1500 |  123 | Cornell  | EE             |        1 |
| 234 | Bob    |  3.6 |   1500 |  345 | Cornell  | EE             |        0 |
| 234 | Bob    |  3.6 |   1500 |  876 | MIT      | marine biology |        0 |
| 234 | Bob    |  3.6 |   1500 |  123 | Berkeley | CS             |        1 |
| 234 | Bob    |  3.6 |   1500 |  345 | Cornell  | CS             |        1 |
| 234 | Bob    |  3.6 |   1500 |  876 | MIT      | biology        |        1 |
| 234 | Bob    |  3.6 |   1500 |  345 | Cornell  | bioengineering |        0 |
| 234 | Bob    |  3.6 |   1500 |  765 | Stanford | history        |        1 |
| 320 | Lori   | NULL |   2500 |  345 | Cornell  | bioengineering |        0 |
| 320 | Lori   | NULL |   2500 |  765 | Stanford | history        |        1 |
| 320 | Lori   | NULL |   2500 |  321 | MIT      | psychology     |        1 |
| 320 | Lori   | NULL |   2500 |  765 | Cornell  | psychology     |        1 |
| 320 | Lori   | NULL |   2500 |  321 | MIT      | history        |        0 |
| 320 | Lori   | NULL |   2500 |  765 | Cornell  | history        |        0 |
| 320 | Lori   | NULL |   2500 |  234 | Berkeley | biology        |        0 |
| 320 | Lori   | NULL |   2500 |  678 | Stanford | history        |        1 |
| 320 | Lori   | NULL |   2500 |  987 | Stanford | CS             |        1 |
| 320 | Lori   | NULL |   2500 |  123 | Stanford | EE             |        0 |
| 320 | Lori   | NULL |   2500 |  543 | MIT      | CS             |        0 |
| 320 | Lori   | NULL |   2500 |  987 | Berkeley | CS             |        1 |
| 320 | Lori   | NULL |   2500 |  123 | Stanford | CS             |        1 |
| 320 | Lori   | NULL |   2500 |  345 | MIT      | bioengineering |        1 |
| 320 | Lori   | NULL |   2500 |  876 | Stanford | CS             |        0 |
| 320 | Lori   | NULL |   2500 |  123 | Cornell  | EE             |        1 |
| 320 | Lori   | NULL |   2500 |  345 | Cornell  | EE             |        0 |
| 320 | Lori   | NULL |   2500 |  876 | MIT      | marine biology |        0 |
| 320 | Lori   | NULL |   2500 |  123 | Berkeley | CS             |        1 |
| 320 | Lori   | NULL |   2500 |  345 | Cornell  | CS             |        1 |
| 320 | Lori   | NULL |   2500 |  876 | MIT      | biology        |        1 |
| 321 | Mary   |  2.5 |   1200 |  123 | Berkeley | CS             |        1 |
| 321 | Mary   |  2.5 |   1200 |  345 | Cornell  | CS             |        1 |
| 321 | Mary   |  2.5 |   1200 |  876 | MIT      | biology        |        1 |
| 321 | Mary   |  2.5 |   1200 |  345 | Cornell  | bioengineering |        0 |
| 321 | Mary   |  2.5 |   1200 |  765 | Stanford | history        |        1 |
| 321 | Mary   |  2.5 |   1200 |  321 | MIT      | psychology     |        1 |
| 321 | Mary   |  2.5 |   1200 |  765 | Cornell  | psychology     |        1 |
| 321 | Mary   |  2.5 |   1200 |  321 | MIT      | history        |        0 |
| 321 | Mary   |  2.5 |   1200 |  765 | Cornell  | history        |        0 |
| 321 | Mary   |  2.5 |   1200 |  234 | Berkeley | biology        |        0 |
| 321 | Mary   |  2.5 |   1200 |  678 | Stanford | history        |        1 |
| 321 | Mary   |  2.5 |   1200 |  987 | Stanford | CS             |        1 |
| 321 | Mary   |  2.5 |   1200 |  123 | Stanford | EE             |        0 |
| 321 | Mary   |  2.5 |   1200 |  543 | MIT      | CS             |        0 |
| 321 | Mary   |  2.5 |   1200 |  987 | Berkeley | CS             |        1 |
| 321 | Mary   |  2.5 |   1200 |  123 | Stanford | CS             |        1 |
| 321 | Mary   |  2.5 |   1200 |  345 | MIT      | bioengineering |        1 |
| 321 | Mary   |  2.5 |   1200 |  876 | Stanford | CS             |        0 |
| 321 | Mary   |  2.5 |   1200 |  123 | Cornell  | EE             |        1 |
| 321 | Mary   |  2.5 |   1200 |  345 | Cornell  | EE             |        0 |
| 321 | Mary   |  2.5 |   1200 |  876 | MIT      | marine biology |        0 |
| 345 | Craig  |  3.5 |    500 |  123 | Cornell  | EE             |        1 |
| 345 | Craig  |  3.5 |    500 |  345 | Cornell  | EE             |        0 |
| 345 | Craig  |  3.5 |    500 |  876 | MIT      | marine biology |        0 |
| 345 | Craig  |  3.5 |    500 |  123 | Berkeley | CS             |        1 |
| 345 | Craig  |  3.5 |    500 |  345 | Cornell  | CS             |        1 |
| 345 | Craig  |  3.5 |    500 |  876 | MIT      | biology        |        1 |
| 345 | Craig  |  3.5 |    500 |  345 | Cornell  | bioengineering |        0 |
| 345 | Craig  |  3.5 |    500 |  765 | Stanford | history        |        1 |
| 345 | Craig  |  3.5 |    500 |  321 | MIT      | psychology     |        1 |
| 345 | Craig  |  3.5 |    500 |  765 | Cornell  | psychology     |        1 |
| 345 | Craig  |  3.5 |    500 |  321 | MIT      | history        |        0 |
| 345 | Craig  |  3.5 |    500 |  765 | Cornell  | history        |        0 |
| 345 | Craig  |  3.5 |    500 |  234 | Berkeley | biology        |        0 |
| 345 | Craig  |  3.5 |    500 |  678 | Stanford | history        |        1 |
| 345 | Craig  |  3.5 |    500 |  987 | Stanford | CS             |        1 |
| 345 | Craig  |  3.5 |    500 |  123 | Stanford | EE             |        0 |
| 345 | Craig  |  3.5 |    500 |  543 | MIT      | CS             |        0 |
| 345 | Craig  |  3.5 |    500 |  987 | Berkeley | CS             |        1 |
| 345 | Craig  |  3.5 |    500 |  123 | Stanford | CS             |        1 |
| 345 | Craig  |  3.5 |    500 |  345 | MIT      | bioengineering |        1 |
| 345 | Craig  |  3.5 |    500 |  876 | Stanford | CS             |        0 |
| 432 | Kevin  | NULL |   1500 |  123 | Stanford | CS             |        1 |
| 432 | Kevin  | NULL |   1500 |  345 | MIT      | bioengineering |        1 |
| 432 | Kevin  | NULL |   1500 |  876 | Stanford | CS             |        0 |
| 432 | Kevin  | NULL |   1500 |  123 | Cornell  | EE             |        1 |
| 432 | Kevin  | NULL |   1500 |  345 | Cornell  | EE             |        0 |
| 432 | Kevin  | NULL |   1500 |  876 | MIT      | marine biology |        0 |
| 432 | Kevin  | NULL |   1500 |  123 | Berkeley | CS             |        1 |
| 432 | Kevin  | NULL |   1500 |  345 | Cornell  | CS             |        1 |
| 432 | Kevin  | NULL |   1500 |  876 | MIT      | biology        |        1 |
| 432 | Kevin  | NULL |   1500 |  345 | Cornell  | bioengineering |        0 |
| 432 | Kevin  | NULL |   1500 |  765 | Stanford | history        |        1 |
| 432 | Kevin  | NULL |   1500 |  321 | MIT      | psychology     |        1 |
| 432 | Kevin  | NULL |   1500 |  765 | Cornell  | psychology     |        1 |
| 432 | Kevin  | NULL |   1500 |  321 | MIT      | history        |        0 |
| 432 | Kevin  | NULL |   1500 |  765 | Cornell  | history        |        0 |
| 432 | Kevin  | NULL |   1500 |  234 | Berkeley | biology        |        0 |
| 432 | Kevin  | NULL |   1500 |  678 | Stanford | history        |        1 |
| 432 | Kevin  | NULL |   1500 |  987 | Stanford | CS             |        1 |
| 432 | Kevin  | NULL |   1500 |  123 | Stanford | EE             |        0 |
| 432 | Kevin  | NULL |   1500 |  543 | MIT      | CS             |        0 |
| 432 | Kevin  | NULL |   1500 |  987 | Berkeley | CS             |        1 |
| 456 | Doris  |  3.9 |   1000 |  123 | Stanford | EE             |        0 |
| 456 | Doris  |  3.9 |   1000 |  543 | MIT      | CS             |        0 |
| 456 | Doris  |  3.9 |   1000 |  987 | Berkeley | CS             |        1 |
| 456 | Doris  |  3.9 |   1000 |  123 | Stanford | CS             |        1 |
| 456 | Doris  |  3.9 |   1000 |  345 | MIT      | bioengineering |        1 |
| 456 | Doris  |  3.9 |   1000 |  876 | Stanford | CS             |        0 |
| 456 | Doris  |  3.9 |   1000 |  123 | Cornell  | EE             |        1 |
| 456 | Doris  |  3.9 |   1000 |  345 | Cornell  | EE             |        0 |
| 456 | Doris  |  3.9 |   1000 |  876 | MIT      | marine biology |        0 |
| 456 | Doris  |  3.9 |   1000 |  123 | Berkeley | CS             |        1 |
| 456 | Doris  |  3.9 |   1000 |  345 | Cornell  | CS             |        1 |
| 456 | Doris  |  3.9 |   1000 |  876 | MIT      | biology        |        1 |
| 456 | Doris  |  3.9 |   1000 |  345 | Cornell  | bioengineering |        0 |
| 456 | Doris  |  3.9 |   1000 |  765 | Stanford | history        |        1 |
| 456 | Doris  |  3.9 |   1000 |  321 | MIT      | psychology     |        1 |
| 456 | Doris  |  3.9 |   1000 |  765 | Cornell  | psychology     |        1 |
| 456 | Doris  |  3.9 |   1000 |  321 | MIT      | history        |        0 |
| 456 | Doris  |  3.9 |   1000 |  765 | Cornell  | history        |        0 |
| 456 | Doris  |  3.9 |   1000 |  234 | Berkeley | biology        |        0 |
| 456 | Doris  |  3.9 |   1000 |  678 | Stanford | history        |        1 |
| 456 | Doris  |  3.9 |   1000 |  987 | Stanford | CS             |        1 |
| 543 | Craig  |  3.4 |   2000 |  234 | Berkeley | biology        |        0 |
| 543 | Craig  |  3.4 |   2000 |  678 | Stanford | history        |        1 |
| 543 | Craig  |  3.4 |   2000 |  987 | Stanford | CS             |        1 |
| 543 | Craig  |  3.4 |   2000 |  123 | Stanford | EE             |        0 |
| 543 | Craig  |  3.4 |   2000 |  543 | MIT      | CS             |        0 |
| 543 | Craig  |  3.4 |   2000 |  987 | Berkeley | CS             |        1 |
| 543 | Craig  |  3.4 |   2000 |  123 | Stanford | CS             |        1 |
| 543 | Craig  |  3.4 |   2000 |  345 | MIT      | bioengineering |        1 |
| 543 | Craig  |  3.4 |   2000 |  876 | Stanford | CS             |        0 |
| 543 | Craig  |  3.4 |   2000 |  123 | Cornell  | EE             |        1 |
| 543 | Craig  |  3.4 |   2000 |  345 | Cornell  | EE             |        0 |
| 543 | Craig  |  3.4 |   2000 |  876 | MIT      | marine biology |        0 |
| 543 | Craig  |  3.4 |   2000 |  123 | Berkeley | CS             |        1 |
| 543 | Craig  |  3.4 |   2000 |  345 | Cornell  | CS             |        1 |
| 543 | Craig  |  3.4 |   2000 |  876 | MIT      | biology        |        1 |
| 543 | Craig  |  3.4 |   2000 |  345 | Cornell  | bioengineering |        0 |
| 543 | Craig  |  3.4 |   2000 |  765 | Stanford | history        |        1 |
| 543 | Craig  |  3.4 |   2000 |  321 | MIT      | psychology     |        1 |
| 543 | Craig  |  3.4 |   2000 |  765 | Cornell  | psychology     |        1 |
| 543 | Craig  |  3.4 |   2000 |  321 | MIT      | history        |        0 |
| 543 | Craig  |  3.4 |   2000 |  765 | Cornell  | history        |        0 |
| 567 | Edward |  2.9 |   2000 |  321 | MIT      | history        |        0 |
| 567 | Edward |  2.9 |   2000 |  765 | Cornell  | history        |        0 |
| 567 | Edward |  2.9 |   2000 |  234 | Berkeley | biology        |        0 |
| 567 | Edward |  2.9 |   2000 |  678 | Stanford | history        |        1 |
| 567 | Edward |  2.9 |   2000 |  987 | Stanford | CS             |        1 |
| 567 | Edward |  2.9 |   2000 |  123 | Stanford | EE             |        0 |
| 567 | Edward |  2.9 |   2000 |  543 | MIT      | CS             |        0 |
| 567 | Edward |  2.9 |   2000 |  987 | Berkeley | CS             |        1 |
| 567 | Edward |  2.9 |   2000 |  123 | Stanford | CS             |        1 |
| 567 | Edward |  2.9 |   2000 |  345 | MIT      | bioengineering |        1 |
| 567 | Edward |  2.9 |   2000 |  876 | Stanford | CS             |        0 |
| 567 | Edward |  2.9 |   2000 |  123 | Cornell  | EE             |        1 |
| 567 | Edward |  2.9 |   2000 |  345 | Cornell  | EE             |        0 |
| 567 | Edward |  2.9 |   2000 |  876 | MIT      | marine biology |        0 |
| 567 | Edward |  2.9 |   2000 |  123 | Berkeley | CS             |        1 |
| 567 | Edward |  2.9 |   2000 |  345 | Cornell  | CS             |        1 |
| 567 | Edward |  2.9 |   2000 |  876 | MIT      | biology        |        1 |
| 567 | Edward |  2.9 |   2000 |  345 | Cornell  | bioengineering |        0 |
| 567 | Edward |  2.9 |   2000 |  765 | Stanford | history        |        1 |
| 567 | Edward |  2.9 |   2000 |  321 | MIT      | psychology     |        1 |
| 567 | Edward |  2.9 |   2000 |  765 | Cornell  | psychology     |        1 |
| 654 | Amy    |  3.9 |   1000 |  321 | MIT      | psychology     |        1 |
| 654 | Amy    |  3.9 |   1000 |  765 | Cornell  | psychology     |        1 |
| 654 | Amy    |  3.9 |   1000 |  321 | MIT      | history        |        0 |
| 654 | Amy    |  3.9 |   1000 |  765 | Cornell  | history        |        0 |
| 654 | Amy    |  3.9 |   1000 |  234 | Berkeley | biology        |        0 |
| 654 | Amy    |  3.9 |   1000 |  678 | Stanford | history        |        1 |
| 654 | Amy    |  3.9 |   1000 |  987 | Stanford | CS             |        1 |
| 654 | Amy    |  3.9 |   1000 |  123 | Stanford | EE             |        0 |
| 654 | Amy    |  3.9 |   1000 |  543 | MIT      | CS             |        0 |
| 654 | Amy    |  3.9 |   1000 |  987 | Berkeley | CS             |        1 |
| 654 | Amy    |  3.9 |   1000 |  123 | Stanford | CS             |        1 |
| 654 | Amy    |  3.9 |   1000 |  345 | MIT      | bioengineering |        1 |
| 654 | Amy    |  3.9 |   1000 |  876 | Stanford | CS             |        0 |
| 654 | Amy    |  3.9 |   1000 |  123 | Cornell  | EE             |        1 |
| 654 | Amy    |  3.9 |   1000 |  345 | Cornell  | EE             |        0 |
| 654 | Amy    |  3.9 |   1000 |  876 | MIT      | marine biology |        0 |
| 654 | Amy    |  3.9 |   1000 |  123 | Berkeley | CS             |        1 |
| 654 | Amy    |  3.9 |   1000 |  345 | Cornell  | CS             |        1 |
| 654 | Amy    |  3.9 |   1000 |  876 | MIT      | biology        |        1 |
| 654 | Amy    |  3.9 |   1000 |  345 | Cornell  | bioengineering |        0 |
| 654 | Amy    |  3.9 |   1000 |  765 | Stanford | history        |        1 |
| 678 | Fay    |  3.8 |    200 |  345 | Cornell  | bioengineering |        0 |
| 678 | Fay    |  3.8 |    200 |  765 | Stanford | history        |        1 |
| 678 | Fay    |  3.8 |    200 |  321 | MIT      | psychology     |        1 |
| 678 | Fay    |  3.8 |    200 |  765 | Cornell  | psychology     |        1 |
| 678 | Fay    |  3.8 |    200 |  321 | MIT      | history        |        0 |
| 678 | Fay    |  3.8 |    200 |  765 | Cornell  | history        |        0 |
| 678 | Fay    |  3.8 |    200 |  234 | Berkeley | biology        |        0 |
| 678 | Fay    |  3.8 |    200 |  678 | Stanford | history        |        1 |
| 678 | Fay    |  3.8 |    200 |  987 | Stanford | CS             |        1 |
| 678 | Fay    |  3.8 |    200 |  123 | Stanford | EE             |        0 |
| 678 | Fay    |  3.8 |    200 |  543 | MIT      | CS             |        0 |
| 678 | Fay    |  3.8 |    200 |  987 | Berkeley | CS             |        1 |
| 678 | Fay    |  3.8 |    200 |  123 | Stanford | CS             |        1 |
| 678 | Fay    |  3.8 |    200 |  345 | MIT      | bioengineering |        1 |
| 678 | Fay    |  3.8 |    200 |  876 | Stanford | CS             |        0 |
| 678 | Fay    |  3.8 |    200 |  123 | Cornell  | EE             |        1 |
| 678 | Fay    |  3.8 |    200 |  345 | Cornell  | EE             |        0 |
| 678 | Fay    |  3.8 |    200 |  876 | MIT      | marine biology |        0 |
| 678 | Fay    |  3.8 |    200 |  123 | Berkeley | CS             |        1 |
| 678 | Fay    |  3.8 |    200 |  345 | Cornell  | CS             |        1 |
| 678 | Fay    |  3.8 |    200 |  876 | MIT      | biology        |        1 |
| 765 | Jay    |  2.9 |   1500 |  123 | Berkeley | CS             |        1 |
| 765 | Jay    |  2.9 |   1500 |  345 | Cornell  | CS             |        1 |
| 765 | Jay    |  2.9 |   1500 |  876 | MIT      | biology        |        1 |
| 765 | Jay    |  2.9 |   1500 |  345 | Cornell  | bioengineering |        0 |
| 765 | Jay    |  2.9 |   1500 |  765 | Stanford | history        |        1 |
| 765 | Jay    |  2.9 |   1500 |  321 | MIT      | psychology     |        1 |
| 765 | Jay    |  2.9 |   1500 |  765 | Cornell  | psychology     |        1 |
| 765 | Jay    |  2.9 |   1500 |  321 | MIT      | history        |        0 |
| 765 | Jay    |  2.9 |   1500 |  765 | Cornell  | history        |        0 |
| 765 | Jay    |  2.9 |   1500 |  234 | Berkeley | biology        |        0 |
| 765 | Jay    |  2.9 |   1500 |  678 | Stanford | history        |        1 |
| 765 | Jay    |  2.9 |   1500 |  987 | Stanford | CS             |        1 |
| 765 | Jay    |  2.9 |   1500 |  123 | Stanford | EE             |        0 |
| 765 | Jay    |  2.9 |   1500 |  543 | MIT      | CS             |        0 |
| 765 | Jay    |  2.9 |   1500 |  987 | Berkeley | CS             |        1 |
| 765 | Jay    |  2.9 |   1500 |  123 | Stanford | CS             |        1 |
| 765 | Jay    |  2.9 |   1500 |  345 | MIT      | bioengineering |        1 |
| 765 | Jay    |  2.9 |   1500 |  876 | Stanford | CS             |        0 |
| 765 | Jay    |  2.9 |   1500 |  123 | Cornell  | EE             |        1 |
| 765 | Jay    |  2.9 |   1500 |  345 | Cornell  | EE             |        0 |
| 765 | Jay    |  2.9 |   1500 |  876 | MIT      | marine biology |        0 |
| 789 | Gary   |  3.4 |    800 |  123 | Cornell  | EE             |        1 |
| 789 | Gary   |  3.4 |    800 |  345 | Cornell  | EE             |        0 |
| 789 | Gary   |  3.4 |    800 |  876 | MIT      | marine biology |        0 |
| 789 | Gary   |  3.4 |    800 |  123 | Berkeley | CS             |        1 |
| 789 | Gary   |  3.4 |    800 |  345 | Cornell  | CS             |        1 |
| 789 | Gary   |  3.4 |    800 |  876 | MIT      | biology        |        1 |
| 789 | Gary   |  3.4 |    800 |  345 | Cornell  | bioengineering |        0 |
| 789 | Gary   |  3.4 |    800 |  765 | Stanford | history        |        1 |
| 789 | Gary   |  3.4 |    800 |  321 | MIT      | psychology     |        1 |
| 789 | Gary   |  3.4 |    800 |  765 | Cornell  | psychology     |        1 |
| 789 | Gary   |  3.4 |    800 |  321 | MIT      | history        |        0 |
| 789 | Gary   |  3.4 |    800 |  765 | Cornell  | history        |        0 |
| 789 | Gary   |  3.4 |    800 |  234 | Berkeley | biology        |        0 |
| 789 | Gary   |  3.4 |    800 |  678 | Stanford | history        |        1 |
| 789 | Gary   |  3.4 |    800 |  987 | Stanford | CS             |        1 |
| 789 | Gary   |  3.4 |    800 |  123 | Stanford | EE             |        0 |
| 789 | Gary   |  3.4 |    800 |  543 | MIT      | CS             |        0 |
| 789 | Gary   |  3.4 |    800 |  987 | Berkeley | CS             |        1 |
| 789 | Gary   |  3.4 |    800 |  123 | Stanford | CS             |        1 |
| 789 | Gary   |  3.4 |    800 |  345 | MIT      | bioengineering |        1 |
| 789 | Gary   |  3.4 |    800 |  876 | Stanford | CS             |        0 |
| 876 | Irene  |  3.9 |    400 |  123 | Stanford | CS             |        1 |
| 876 | Irene  |  3.9 |    400 |  345 | MIT      | bioengineering |        1 |
| 876 | Irene  |  3.9 |    400 |  876 | Stanford | CS             |        0 |
| 876 | Irene  |  3.9 |    400 |  123 | Cornell  | EE             |        1 |
| 876 | Irene  |  3.9 |    400 |  345 | Cornell  | EE             |        0 |
| 876 | Irene  |  3.9 |    400 |  876 | MIT      | marine biology |        0 |
| 876 | Irene  |  3.9 |    400 |  123 | Berkeley | CS             |        1 |
| 876 | Irene  |  3.9 |    400 |  345 | Cornell  | CS             |        1 |
| 876 | Irene  |  3.9 |    400 |  876 | MIT      | biology        |        1 |
| 876 | Irene  |  3.9 |    400 |  345 | Cornell  | bioengineering |        0 |
| 876 | Irene  |  3.9 |    400 |  765 | Stanford | history        |        1 |
| 876 | Irene  |  3.9 |    400 |  321 | MIT      | psychology     |        1 |
| 876 | Irene  |  3.9 |    400 |  765 | Cornell  | psychology     |        1 |
| 876 | Irene  |  3.9 |    400 |  321 | MIT      | history        |        0 |
| 876 | Irene  |  3.9 |    400 |  765 | Cornell  | history        |        0 |
| 876 | Irene  |  3.9 |    400 |  234 | Berkeley | biology        |        0 |
| 876 | Irene  |  3.9 |    400 |  678 | Stanford | history        |        1 |
| 876 | Irene  |  3.9 |    400 |  987 | Stanford | CS             |        1 |
| 876 | Irene  |  3.9 |    400 |  123 | Stanford | EE             |        0 |
| 876 | Irene  |  3.9 |    400 |  543 | MIT      | CS             |        0 |
| 876 | Irene  |  3.9 |    400 |  987 | Berkeley | CS             |        1 |
| 987 | Helen  |  3.7 |    800 |  123 | Stanford | EE             |        0 |
| 987 | Helen  |  3.7 |    800 |  543 | MIT      | CS             |        0 |
| 987 | Helen  |  3.7 |    800 |  987 | Berkeley | CS             |        1 |
| 987 | Helen  |  3.7 |    800 |  123 | Stanford | CS             |        1 |
| 987 | Helen  |  3.7 |    800 |  345 | MIT      | bioengineering |        1 |
| 987 | Helen  |  3.7 |    800 |  876 | Stanford | CS             |        0 |
| 987 | Helen  |  3.7 |    800 |  123 | Cornell  | EE             |        1 |
| 987 | Helen  |  3.7 |    800 |  345 | Cornell  | EE             |        0 |
| 987 | Helen  |  3.7 |    800 |  876 | MIT      | marine biology |        0 |
| 987 | Helen  |  3.7 |    800 |  123 | Berkeley | CS             |        1 |
| 987 | Helen  |  3.7 |    800 |  345 | Cornell  | CS             |        1 |
| 987 | Helen  |  3.7 |    800 |  876 | MIT      | biology        |        1 |
| 987 | Helen  |  3.7 |    800 |  345 | Cornell  | bioengineering |        0 |
| 987 | Helen  |  3.7 |    800 |  765 | Stanford | history        |        1 |
| 987 | Helen  |  3.7 |    800 |  321 | MIT      | psychology     |        1 |
| 987 | Helen  |  3.7 |    800 |  765 | Cornell  | psychology     |        1 |
| 987 | Helen  |  3.7 |    800 |  321 | MIT      | history        |        0 |
| 987 | Helen  |  3.7 |    800 |  765 | Cornell  | history        |        0 |
| 987 | Helen  |  3.7 |    800 |  234 | Berkeley | biology        |        0 |
| 987 | Helen  |  3.7 |    800 |  678 | Stanford | history        |        1 |
| 987 | Helen  |  3.7 |    800 |  987 | Stanford | CS             |        1 |
+-----+--------+------+--------+------+----------+----------------+----------+
*/

-- -----------------------------------------------------------------------
-- relational algebra theta join (with on)
-- notice duplicate sID attribute
select "*** query #2a ***" as "";
select *
    from Student
    inner join Apply
    on Student.sID = Apply.sID;

/*
+-------------------+
| *** query #2a *** |
+-------------------+
+-----+-------+------+--------+------+----------+----------------+----------+
| sID | sName | GPA  | sizeHS | sID  | cName    | major          | decision |
+-----+-------+------+--------+------+----------+----------------+----------+
| 123 | Amy   |  3.9 |   1000 |  123 | Berkeley | CS             |        1 |
| 123 | Amy   |  3.9 |   1000 |  123 | Cornell  | EE             |        1 |
| 123 | Amy   |  3.9 |   1000 |  123 | Stanford | CS             |        1 |
| 123 | Amy   |  3.9 |   1000 |  123 | Stanford | EE             |        0 |
| 234 | Bob   |  3.6 |   1500 |  234 | Berkeley | biology        |        0 |
| 321 | Mary  |  2.5 |   1200 |  321 | MIT      | history        |        0 |
| 321 | Mary  |  2.5 |   1200 |  321 | MIT      | psychology     |        1 |
| 345 | Craig |  3.5 |    500 |  345 | Cornell  | bioengineering |        0 |
| 345 | Craig |  3.5 |    500 |  345 | Cornell  | CS             |        1 |
| 345 | Craig |  3.5 |    500 |  345 | Cornell  | EE             |        0 |
| 345 | Craig |  3.5 |    500 |  345 | MIT      | bioengineering |        1 |
| 543 | Craig |  3.4 |   2000 |  543 | MIT      | CS             |        0 |
| 678 | Fay   |  3.8 |    200 |  678 | Stanford | history        |        1 |
| 765 | Jay   |  2.9 |   1500 |  765 | Cornell  | history        |        0 |
| 765 | Jay   |  2.9 |   1500 |  765 | Cornell  | psychology     |        1 |
| 765 | Jay   |  2.9 |   1500 |  765 | Stanford | history        |        1 |
| 876 | Irene |  3.9 |    400 |  876 | MIT      | biology        |        1 |
| 876 | Irene |  3.9 |    400 |  876 | MIT      | marine biology |        0 |
| 876 | Irene |  3.9 |    400 |  876 | Stanford | CS             |        0 |
| 987 | Helen |  3.7 |    800 |  987 | Berkeley | CS             |        1 |
| 987 | Helen |  3.7 |    800 |  987 | Stanford | CS             |        1 |
+-----+-------+------+--------+------+----------+----------------+----------+
*/

-- -----------------------------------------------------------------------
-- relational algebra theta join (with using)
-- notice NO duplicate sID attribute
select "*** query #2b ***" as "";
select *
    from Student
    inner join Apply using (sID);

/*
+-------------------+
| *** query #2b *** |
+-------------------+
+-----+-------+------+--------+----------+----------------+----------+
| sID | sName | GPA  | sizeHS | cName    | major          | decision |
+-----+-------+------+--------+----------+----------------+----------+
| 123 | Amy   |  3.9 |   1000 | Berkeley | CS             |        1 |
| 123 | Amy   |  3.9 |   1000 | Cornell  | EE             |        1 |
| 123 | Amy   |  3.9 |   1000 | Stanford | CS             |        1 |
| 123 | Amy   |  3.9 |   1000 | Stanford | EE             |        0 |
| 234 | Bob   |  3.6 |   1500 | Berkeley | biology        |        0 |
| 321 | Mary  |  2.5 |   1200 | MIT      | history        |        0 |
| 321 | Mary  |  2.5 |   1200 | MIT      | psychology     |        1 |
| 345 | Craig |  3.5 |    500 | Cornell  | bioengineering |        0 |
| 345 | Craig |  3.5 |    500 | Cornell  | CS             |        1 |
| 345 | Craig |  3.5 |    500 | Cornell  | EE             |        0 |
| 345 | Craig |  3.5 |    500 | MIT      | bioengineering |        1 |
| 543 | Craig |  3.4 |   2000 | MIT      | CS             |        0 |
| 678 | Fay   |  3.8 |    200 | Stanford | history        |        1 |
| 765 | Jay   |  2.9 |   1500 | Cornell  | history        |        0 |
| 765 | Jay   |  2.9 |   1500 | Cornell  | psychology     |        1 |
| 765 | Jay   |  2.9 |   1500 | Stanford | history        |        1 |
| 876 | Irene |  3.9 |    400 | MIT      | biology        |        1 |
| 876 | Irene |  3.9 |    400 | MIT      | marine biology |        0 |
| 876 | Irene |  3.9 |    400 | Stanford | CS             |        0 |
| 987 | Helen |  3.7 |    800 | Berkeley | CS             |        1 |
| 987 | Helen |  3.7 |    800 | Stanford | CS             |        1 |
+-----+-------+------+--------+----------+----------------+----------+
*/

-- -----------------------------------------------------------------------
-- relational algebra natural join
select "*** query #2c ***" as "";
select *
    from Student
    natural join Apply;

/*
+-------------------+
| *** query #2c *** |
+-------------------+
+-----+-------+------+--------+----------+----------------+----------+
| sID | sName | GPA  | sizeHS | cName    | major          | decision |
+-----+-------+------+--------+----------+----------------+----------+
| 123 | Amy   |  3.9 |   1000 | Berkeley | CS             |        1 |
| 123 | Amy   |  3.9 |   1000 | Cornell  | EE             |        1 |
| 123 | Amy   |  3.9 |   1000 | Stanford | CS             |        1 |
| 123 | Amy   |  3.9 |   1000 | Stanford | EE             |        0 |
| 234 | Bob   |  3.6 |   1500 | Berkeley | biology        |        0 |
| 321 | Mary  |  2.5 |   1200 | MIT      | history        |        0 |
| 321 | Mary  |  2.5 |   1200 | MIT      | psychology     |        1 |
| 345 | Craig |  3.5 |    500 | Cornell  | bioengineering |        0 |
| 345 | Craig |  3.5 |    500 | Cornell  | CS             |        1 |
| 345 | Craig |  3.5 |    500 | Cornell  | EE             |        0 |
| 345 | Craig |  3.5 |    500 | MIT      | bioengineering |        1 |
| 543 | Craig |  3.4 |   2000 | MIT      | CS             |        0 |
| 678 | Fay   |  3.8 |    200 | Stanford | history        |        1 |
| 765 | Jay   |  2.9 |   1500 | Cornell  | history        |        0 |
| 765 | Jay   |  2.9 |   1500 | Cornell  | psychology     |        1 |
| 765 | Jay   |  2.9 |   1500 | Stanford | history        |        1 |
| 876 | Irene |  3.9 |    400 | MIT      | biology        |        1 |
| 876 | Irene |  3.9 |    400 | MIT      | marine biology |        0 |
| 876 | Irene |  3.9 |    400 | Stanford | CS             |        0 |
| 987 | Helen |  3.7 |    800 | Berkeley | CS             |        1 |
| 987 | Helen |  3.7 |    800 | Stanford | CS             |        1 |
+-----+-------+------+--------+----------+----------------+----------+
*/

-- -----------------------------------------------------------------------
-- student name and GPA of students who applied in "CS" but were not accepted
-- inner join
select "*** query #3a ***" as "";
select sName, GPA
    from Student
    inner join Apply using (sID)
    where major = "CS" and not decision;

/*
+-------------------+
| *** query #3a *** |
+-------------------+
+-------+------+
| sName | GPA  |
+-------+------+
| Craig |  3.4 |
| Irene |  3.9 |
+-------+------+
*/

-- -----------------------------------------------------------------------
-- subquery (with in)
select "*** query #3b ***" as "";
select sName, GPA
    from Student
    where sID in
        (select sID
            from Apply
            where major = "CS" and not decision);

/*
+-------------------+
| *** query #3b *** |
+-------------------+
+-------+------+
| sName | GPA  |
+-------+------+
| Craig |  3.4 |
| Irene |  3.9 |
+-------+------+
*/

-- -----------------------------------------------------------------------
-- student name and GPA of students who applied in "CS" to colleges with an enrollment greater than 20000
-- inner join
select "*** query #4 ***" as "";
select sName, GPA
    from Student
        inner join Apply   using (sID)
        inner join College using (cName)
    where major = "CS" and enrollment > 20000;

/*
+------------------+
| *** query #4 *** |
+------------------+
+-------+------+
| sName | GPA  |
+-------+------+
| Amy   |  3.9 |
| Helen |  3.7 |
| Craig |  3.5 |
+-------+------+
*/

-- -----------------------------------------------------------------------
-- name of college and state if there's another college in the same state
-- self join (using as)
select "*** query #5a ***" as "";
select R.cName, R.state
    from College as R
    inner join College as S
    where R.cName != S.cName and R.state = S.state;

/*
+-------------------+
| *** query #5a *** |
+-------------------+
+----------+-------+
| cName    | state |
+----------+-------+
| Stanford | CA    |
| Berkeley | CA    |
+----------+-------+
*/

-- -----------------------------------------------------------------------
-- subquery (with exists)
select "*** query #5b ***" as "";
select cName, state
    from College as R
    where exists
        (select *
            from College as S
            where R.cName != S.cName and R.state = S.state);

/*
+-------------------+
| *** query #5b *** |
+-------------------+
+----------+-------+
| cName    | state |
+----------+-------+
| Berkeley | CA    |
| Stanford | CA    |
+----------+-------+
*/

-- -----------------------------------------------------------------------
-- subquery (with group by and having)
select "*** query #5c ***" as "";
select cName, state
    from College
    natural join
        (select State
            from College
            group by State
            having count(State) > 1) as T;

/*
+-------------------+
| *** query #5c *** |
+-------------------+
+----------+-------+
| cName    | state |
+----------+-------+
| Berkeley | CA    |
| Stanford | CA    |
+----------+-------+
*/

exit
