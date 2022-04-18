-- ---------
-- JoinT.sql
-- ---------

use test;

-- -----------------------------------------------------------------------
-- ID, name, and GPA of students who applied in CS
-- MUST USE inner join

select "*** query #1 ***";
select distinct sID, sName, GPA
    from Student
    inner join Apply using (sID)
    inner join Apply on    (Student.sID = Apply.sID)
    natural join
    where major = "CS";

/*
+------------------+
| *** query #1 *** |
+------------------+
| *** query #1 *** |
+------------------+
+-----+-------+------+
| sID | sName | GPA  |
+-----+-------+------+
| 123 | Amy   |  3.9 |
| 345 | Craig |  3.5 |
| 543 | Craig |  3.4 |
| 876 | Irene |  3.9 |
| 987 | Helen |  3.7 |
+-----+-------+------+
*/

-- -----------------------------------------------------------------------
-- ID, name, and GPA of students who applied in CS
-- MUST USE subquery

select "*** query #2a ***";
select sID, sName, GPA
    from Student
    where sID in
        (select sID              -- 1 col, many rows, with duplicates
            from Apply
            where major = "CS");

/*
+-------------------+
| *** query #2a *** |
+-------------------+
| *** query #2a *** |
+-------------------+
+-----+-------+------+
| sID | sName | GPA  |
+-----+-------+------+
| 123 | Amy   |  3.9 |
| 345 | Craig |  3.5 |
| 543 | Craig |  3.4 |
| 876 | Irene |  3.9 |
| 987 | Helen |  3.7 |
+-----+-------+------+
*/

-- with distinct
select "*** query #2b ***";
select sID, sName, GPA
    from Student
    where sID in
        (select distinct sID
            from Apply
            where major = "CS");

/*
+-------------------+
| *** query #2b *** |
+-------------------+
| *** query #2b *** |
+-------------------+
+-----+-------+------+
| sID | sName | GPA  |
+-----+-------+------+
| 123 | Amy   |  3.9 |
| 345 | Craig |  3.5 |
| 543 | Craig |  3.4 |
| 876 | Irene |  3.9 |
| 987 | Helen |  3.7 |
+-----+-------+------+
*/

-- -----------------------------------------------------------------------
-- GPA of students who applied in CS
-- sorted in descending order

-- this is not right, why?
select "*** query #3a ***";
select GPA
    from Student
    inner join Apply using (sID)
    where major = "CS"
    order by GPA desc;

/*
+-------------------+
| *** query #3a *** |
+-------------------+
| *** query #3a *** |
+-------------------+
+------+
| GPA  |
+------+
|  3.9 |
|  3.9 |
|  3.9 |
|  3.7 |
|  3.7 |
|  3.5 |
|  3.4 |
+------+
*/

-- this is still not right, why?
select "*** query #3b ***";
select distinct GPA
    from Student
    inner join Apply using (sID)
    where major = "CS"
    order by GPA desc;

/*
+-------------------+
| *** query #3b *** |
+-------------------+
| *** query #3b *** |
+-------------------+
+------+
| GPA  |
+------+
|  3.9 |
|  3.7 |
|  3.5 |
|  3.4 |
+------+
*/

-- this is right
select "*** query #3c ***";
select GPA
    from Student
    where sID in
        (select sID
            from Apply
            where major = "CS")
    order by GPA desc;

/*
+-------------------+
| *** query #3c *** |
+-------------------+
| *** query #3c *** |
+-------------------+
+------+
| GPA  |
+------+
|  3.9 |
|  3.9 |
|  3.7 |
|  3.5 |
|  3.4 |
+------+
*/

-- this is also right (with distinct)
select "*** query #3d ***";
select GPA
    from Student
    where sID in
        (select distinct sID
            from Apply
            where major = "CS")
    order by GPA desc;

/*
+-------------------+
| *** query #3d *** |
+-------------------+
| *** query #3d *** |
+-------------------+
+------+
| GPA  |
+------+
|  3.9 |
|  3.9 |
|  3.7 |
|  3.5 |
|  3.4 |
+------+
*/

-- -----------------------------------------------------------------------
-- ID of students who have applied in CS but not in EE

-- this is not right, why?
select "*** query #4a ***";
select sID
    from Student
    where
        sID in (select sID from Apply where major  = "CS")
        and
        sID in (select sID from Apply where major != "EE");

/*
+-------------------+
| *** query #4a *** |
+-------------------+
| *** query #4a *** |
+-------------------+
+-----+
| sID |
+-----+
| 123 |
| 345 |
| 543 |
| 876 |
| 987 |
+-----+
*/

-- this is right
select "*** query #4b ***";
select sID
    from Student
    where
        sID     in (select sID from Apply where major = "CS")
        and
        sID not in (select sID from Apply where major = "EE");

/*
+-------------------+
| *** query #4b *** |
+-------------------+
| *** query #4b *** |
+-------------------+
+-----+
| sID |
+-----+
| 543 |
| 876 |
| 987 |
+-----+
*/

-- this is also right
select "*** query #4c ***";
select distinct sID
    from Apply
    where
        (major = "CS")
        and
        sID not in (select sID from Apply where major = "EE");

/*
+-------------------+
| *** query #4c *** |
+-------------------+
| *** query #4c *** |
+-------------------+
+------+
| sID  |
+------+
|  543 |
|  876 |
|  987 |
+------+
*/

-- -----------------------------------------------------------------------
-- name and enrollment of college with highest enrollment

-- subquery (with not exists)
select "*** query #5a ***";
select cName, enrollment
    from College as R
    where not exists
        (select *
            from College as S
            where R.enrollment < S.enrollment);

/*
+-------------------+
| *** query #5a *** |
+-------------------+
| *** query #5a *** |
+-------------------+
+----------+------------+
| cName    | enrollment |
+----------+------------+
| Berkeley |      36000 |
| UCF      |      36000 |
+----------+------------+
*/

-- subquery (with all)
select "*** query #5b ***";
select cName, enrollment
    from College
    where enrollment >= all
        (select enrollment
            from College);

/*
+-------------------+
| *** query #5b *** |
+-------------------+
| *** query #5b *** |
+-------------------+
+----------+------------+
| cName    | enrollment |
+----------+------------+
| Berkeley |      36000 |
| UCF      |      36000 |
+----------+------------+
*/

-- -----------------------------------------------------------------------
-- ID, name, and GPA of student with highest GPA

-- this is not right, why?
select "*** query #6a ***";
select sID, sName, GPA
    from Student as R
    where not exists
        (select *
            from Student as S
            where R.GPA < S.GPA);

/*
+-------------------+
| *** query #6a *** |
+-------------------+
| *** query #6a *** |
+-------------------+
+-----+-------+------+
| sID | sName | GPA  |
+-----+-------+------+
| 123 | Amy   |  3.9 |
| 320 | Lori  | NULL |
| 432 | Kevin | NULL |
| 456 | Doris |  3.9 |
| 654 | Amy   |  3.9 |
| 876 | Irene |  3.9 |
+-----+-------+------+
*/

-- this is right
select "*** query #6b ***";
select sID, sName, GPA
    from Student as R
    where
        not exists
            (select *
                from Student as S
                where R.GPA < S.GPA)
        and
        (GPA is not null);

/*
+-------------------+
| *** query #6b *** |
+-------------------+
| *** query #6b *** |
+-------------------+
+-----+-------+------+
| sID | sName | GPA  |
+-----+-------+------+
| 123 | Amy   |  3.9 |
| 456 | Doris |  3.9 |
| 654 | Amy   |  3.9 |
| 876 | Irene |  3.9 |
+-----+-------+------+
*/

-- this is also right, subquery (with all)
select "*** query #6c ***";
select sID, sName, GPA
    from Student
    where GPA >= all
        (select GPA
            from Student
            where GPA is not null);

/*
+-------------------+
| *** query #6c *** |
+-------------------+
| *** query #6c *** |
+-------------------+
+-----+-------+------+
| sID | sName | GPA  |
+-----+-------+------+
| 123 | Amy   |  3.9 |
| 456 | Doris |  3.9 |
| 654 | Amy   |  3.9 |
| 876 | Irene |  3.9 |
+-----+-------+------+
*/

exit
