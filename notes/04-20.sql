-- -----------
-- Wed, 20 Apr
-- -----------

/*
Paper 13. What Happens to Us Does Not Happen to Most of You
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
13. some queries can't be done with a join, and need a subquery
*/

/*
CATME
JoinT.sql
StrategyPattern1.java
*/





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
        (select distinct sID     -- 1 col, many rows, with NO duplicates
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
        (select sID             -- 1 col, many rows, with duplicates
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
        (select distinct sID    -- 1 col, many rows, with NO duplicates
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

-- subquery (with max)
select "*** query #5c ***";
select cName, enrollment
    from College
    where enrollment =
        (select max(enrollment)
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

-- this is also right, subquery (with all)
select "*** query #6c ***";
select sID, sName, GPA
    from Student
    where GPA =
        (select max(GPA)
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

/*
refactoring
Martin Fowler
1999, in Java
2018, in JavaScript
*/

/*
trivial simulation of a video store
*/

/*
Movie class
Rental class
Customer class
*/

/*
first step in refactoring is to create some tests
*/

// ---------------------
// StrategyPattern1.java
// ---------------------

/*
Extract Method (110)
create Customer.amount()

Move Method (142)
move Customer.amount() to Rental.amount()

Replace Temp with Query (120)
changed thisAmount to rental.amount()
*/

import java.util.Vector;

class Movie {
    public static final int REGULAR     = 0;
    public static final int NEW_RELEASE = 1;
    public static final int CHILDRENS   = 2;

    private String _title;
    private int    _priceCode;

    public Movie (String title, int priceCode) {
        _title = title;
        setPriceCode(priceCode);}

    public int getPriceCode () { // const
        return _priceCode;}

    public String getTitle () { // const
        return _title;}

    public void setPriceCode (int priceCode) {
        _priceCode = priceCode;}}

class Rental {
    private Movie _movie;
    private int   _daysRented;

    public Rental (Movie movie, int daysRented) {
        _movie      = movie;
        _daysRented = daysRented;}

    public int getDaysRented () { // const
        return _daysRented;}

    public Movie getMovie () { // const
        return _movie;}}

class Customer {
    private String         _name;
    private Vector<Rental> _rentals = new Vector<Rental>();

    public Customer (String name) {
        _name = name;}

    public void addRental (Rental rental) {
        _rentals.addElement(rental);}

    public String statement () {                                         // const, O(n)
        double amount = 0;
        int    points = 0;
        String result = "Rental Record for " + _name + "\n";
        for (Rental rental : _rentals) {
            double thisAmount = 0;
            switch (rental.getMovie().getPriceCode()) {
                case Movie.REGULAR:
                    thisAmount += 2;
                    if (rental.getDaysRented() > 2)
                        thisAmount += (rental.getDaysRented() - 2) * 1.5;
                    break;
                case Movie.NEW_RELEASE:
                    thisAmount += rental.getDaysRented() * 3;
                    break;
                case Movie.CHILDRENS:
                    thisAmount += 1.5;
                    if (rental.getDaysRented() > 3)
                        thisAmount += (rental.getDaysRented() - 3) * 1.5;
                    break;}
            amount += thisAmount;
            ++points;
            if ((rental.getMovie().getPriceCode() == Movie.NEW_RELEASE) &&
                (rental.getDaysRented()           >  1))
                ++points;
            result +=
                "\t" + rental.getMovie().getTitle() +
                "\t" + String.valueOf(thisAmount) + "\n";}
        result +=
            "Amount owed is "      +
            String.valueOf(amount) + "\n";
        result +=
            "You earned "              +
            String.valueOf(points)     +
            " frequent renter points";
        return result;}}

final class StrategyPattern1 {
    private static void my_assert(Boolean b) {
        if (!b)
            throw new RuntimeException();}

    public static void main (String[] args) {
        System.out.println("StrategyPattern1.java");

        Customer x = new Customer("Penelope");
        my_assert(x.statement().equals(
            "Rental Record for Penelope\n" +
            "Amount owed is 0.0\n"         +
            "You earned 0 frequent renter points"));

        x.addRental(new Rental(new Movie("Shane", Movie.REGULAR), 2));
        my_assert(x.statement().equals(
            "Rental Record for Penelope\n" +
            "\tShane\t2.0\n"               +
            "Amount owed is 2.0\n"         +
            "You earned 1 frequent renter points"));

        x.addRental(new Rental(new Movie("Red River", Movie.REGULAR), 5));
        my_assert(x.statement().equals(
            "Rental Record for Penelope\n" +
            "\tShane\t2.0\n"               +
            "\tRed River\t6.5\n"           +
            "Amount owed is 8.5\n"         +
            "You earned 2 frequent renter points"));

        x.addRental(new Rental(new Movie("Giant", Movie.NEW_RELEASE), 1));
        my_assert(x.statement().equals(
            "Rental Record for Penelope\n" +
            "\tShane\t2.0\n"               +
            "\tRed River\t6.5\n"           +
            "\tGiant\t3.0\n"               +
            "Amount owed is 11.5\n"        +
            "You earned 3 frequent renter points"));

        x.addRental(new Rental(new Movie("2001", Movie.NEW_RELEASE), 3));
        my_assert(x.statement().equals(
            "Rental Record for Penelope\n" +
            "\tShane\t2.0\n"               +
            "\tRed River\t6.5\n"           +
            "\tGiant\t3.0\n"               +
            "\t2001\t9.0\n"                +
            "Amount owed is 20.5\n"        +
            "You earned 5 frequent renter points"));

        x.addRental(new Rental(new Movie("Big Country", Movie.CHILDRENS), 3));
        my_assert(x.statement().equals(
            "Rental Record for Penelope\n" +
            "\tShane\t2.0\n"               +
            "\tRed River\t6.5\n"           +
            "\tGiant\t3.0\n"               +
            "\t2001\t9.0\n"                +
            "\tBig Country\t1.5\n"         +
            "Amount owed is 22.0\n"        +
            "You earned 6 frequent renter points"));

        x.addRental(new Rental(new Movie("Spartacus", Movie.CHILDRENS), 5));
        my_assert(x.statement().equals(
            "Rental Record for Penelope\n" +
            "\tShane\t2.0\n"               +
            "\tRed River\t6.5\n"           +
            "\tGiant\t3.0\n"               +
            "\t2001\t9.0\n"                +
            "\tBig Country\t1.5\n"         +
            "\tSpartacus\t4.5\n"           +
            "Amount owed is 26.5\n"        +
            "You earned 7 frequent renter points"));

        System.out.println("Done.");}}
