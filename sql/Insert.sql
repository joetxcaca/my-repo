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
