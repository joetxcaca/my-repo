-- ------------
-- Select3T.sql
-- ------------

use test;

-- -----------------------------------------------------------------------
select "*** drop table Apply ***";
drop table if exists Apply;

-- -----------------------------------------------------------------------
select "*** drop table College ***";
drop table if exists College;

-- -----------------------------------------------------------------------
select "*** drop table Student ***";
drop table if exists Student;

-- -----------------------------------------------------------------------
select "*** create table Student ***";
create table Student (
    sID         int not null,
    sName       text,
    GPA         float,
    sizeHS      int,
    primary key (sID))
    engine = innodb;

-- -----------------------------------------------------------------------
select "*** create table College ***";
create table College (
    cName       varchar(8) not null,
    state       char(2),
    enrollment  int,
    primary key (cName))
    engine = innodb;

-- -----------------------------------------------------------------------
select "*** create table Apply ***";
create table Apply (
    sID         int,
    cName       varchar(8),
    major       text,
    decision    boolean,
    foreign key (sID)   references Student (sID),
    foreign key (cName) references College (cName))
    engine = innodb;

-- -----------------------------------------------------------------------
select "*** insert Student ***";
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

-- -----------------------------------------------------------------------
select "*** insert College ***";
insert into College values ("A&M",      "TX", 25000);
insert into College values ("Berkeley", "CA", 36000);
insert into College values ("Cornell",  "NY", 21000);
insert into College values ("MIT",      "MA", 10000);
insert into College values ("Stanford", "CA", 15000);
insert into College values ("UCF",      "FL", 36000);

-- -----------------------------------------------------------------------
select "*** insert Apply ***";
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

-- -----------------------------------------------------------------------
-- student ID, school name, and major of
-- applications that were accepted
-- sorted by school in ascending order

select "*** query #1 ***";
select sID, cName, major
    from Apply
    where decision
    order by cName;

/*
+------------------+
| *** query #1 *** |
+------------------+
+------+----------+----------------+
| sID  | cName    | major          |
+------+----------+----------------+
|  123 | Berkeley | CS             |
|  987 | Berkeley | CS             |
|  123 | Cornell  | EE             |
|  345 | Cornell  | CS             |
|  765 | Cornell  | psychology     |
|  321 | MIT      | psychology     |
|  345 | MIT      | bioengineering |
|  876 | MIT      | biology        |
|  123 | Stanford | CS             |
|  678 | Stanford | history        |
|  765 | Stanford | history        |
|  987 | Stanford | CS             |
+------+----------+----------------+
*/

-- -----------------------------------------------------------------------
-- distinct school name and decision of
-- applications to CS that were accepted
-- sorted by school in descending order
-- limited to two results

select "*** query #2 ***";
select distinct cName, decision
    from Apply
    where major = "CS" and decision
    order by cName desc
    limit 2;

/*
+------------------+
| *** query #2 *** |
+------------------+
+----------+----------+
| cName    | decision |
+----------+----------+
| Stanford |        1 |
| Cornell  |        1 |
+----------+----------+
*/

-- -----------------------------------------------------------------------
-- student name and high school size of
-- students whose names end in "y"

select "*** query #3 ***";
select sName, sizeHS
    from Student
    where sName like "%y";

/*
+------------------+
| *** query #3 *** |
+------------------+
+-------+--------+
| sName | sizeHS |
+-------+--------+
| Amy   |   1000 |
| Mary  |   1200 |
| Amy   |   1000 |
| Fay   |    200 |
| Jay   |   1500 |
| Gary  |    800 |
+-------+--------+
*/

-- -----------------------------------------------------------------------
-- min, max, and average high school size of
-- students whose names have three letters and end in "y"

select "*** query #4 ***";
select min(sizeHS), max(sizeHS), avg(sizeHS)
    from Student
    where sName like "__y";

/*
+------------------+
| *** query #4 *** |
+------------------+
+-------------+-------------+-------------+
| min(sizeHS) | max(sizeHS) | avg(sizeHS) |
+-------------+-------------+-------------+
|         200 |        1500 |    925.0000 |
+-------------+-------------+-------------+
*/

-- -----------------------------------------------------------------------
-- number of schools in CA or TX
-- MUST USE in

select "*** query #5 ***";
select count(*)
    from College
    where state in ("CA", "TX");

/*
+------------------+
| *** query #5 *** |
+------------------+
+----------+
| count(*) |
+----------+
|        3 |
+----------+
*/

-- -----------------------------------------------------------------------
-- state, min, max, and avg enrollment of
-- schools whose enrollment is between 20000 and 30000
-- for each state
-- MUST USE between

select "*** query #6 ***";
select state, min(enrollment), max(enrollment), avg(enrollment)
    from College
    where enrollment between 20000 and 30000
    group by state;

/*
+------------------+
| *** query #6 *** |
+------------------+
+-------+-----------------+-----------------+-----------------+
| state | min(enrollment) | max(enrollment) | avg(enrollment) |
+-------+-----------------+-----------------+-----------------+
| TX    |           25000 |           25000 |      25000.0000 |
| NY    |           21000 |           21000 |      21000.0000 |
+-------+-----------------+-----------------+-----------------+
*/

-- -----------------------------------------------------------------------
-- state, min, max, and average enrollment of
-- schools whose min enrollment is between 15000 and 25000
-- for each state
-- MUST USE having

select "*** query #7 ***";
select state, min(enrollment), max(enrollment), avg(enrollment)
    from College
    group by state
    having min(enrollment) between 15000 and 25000;

/*
+------------------+
| *** query #7 *** |
+------------------+
+-------+-----------------+-----------------+-----------------+
| state | min(enrollment) | max(enrollment) | avg(enrollment) |
+-------+-----------------+-----------------+-----------------+
| TX    |           25000 |           25000 |      25000.0000 |
| CA    |           15000 |           36000 |      25500.0000 |
| NY    |           21000 |           21000 |      21000.0000 |
+-------+-----------------+-----------------+-----------------+
*/

exit
