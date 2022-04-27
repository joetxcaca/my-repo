// -----------
// Wed, 27 Apr
// -----------

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
14. prefer enums to final ints
15. prefer generic containers
16. prefer StringBuilder to strings
*/

/*
StrategyPattern5.java
*/

/*
in Java
what are the consequences of an abstract method
1. the class becomes abstract
2. the children must define the method OR they become abstract
3. can NOT define!!!
*/

abstract class Price {
    abstract amount
    abstract points
    pointsHelpler


class RegularPrice extends Price {
    public double amount (int daysRented) {           // const
        double result = super.amountHelper(daysRented)      // MAYBE
        result += 2;
        if (daysRented > 2)
            result += (daysRented - 2) * 1.5;
        break;
        return result;}

    public points
        super.pointsHelper
        same as Children

class NewPrice extends Price {
    public double amount (int daysRented) {           // const
        double result = 0;
        result += daysRented * 3;
        return result;}

    public points
        special code

class ChildrensPrice extends Price {
    public double amount (int daysRented) {           // const
        double result = 0;
        result += 1.5;
        if (daysRented > 3)
            result += (daysRented - 3) * 1.5;
        return result;}

    public points
        same as Regular

5189

class Movie {
    public static final int REGULAR     = 0;
    public static final int NEW_RELEASE = 1;
    public static final int CHILDRENS   = 2;

    private String _title;
    private Price   _price;

    public Movie (String title, int priceCode) {
        _title = title;
        setPrice(priceCode);}

    public int getPriceCode () { // const
        return _priceCode;}

    public String getTitle () { // const
        return _title;}

    public void setPrice (int priceCode) {
        switch to create the right kind of price object

    public double amount (int daysRented) {           // const
        return _price.amount();

    protected double amountHelper (int days Rented) {
        ...}

    public int points (int daysRented) {             // const
        return _price.points();

    public String statement (int daysRented) {                  // const
        return
            "\t" + getTitle()                         +
            "\t" + String.valueOf(amount(daysRented)) + "\n";}}


final class StrategyPattern5 {
    private static void my_assert(Boolean b) {
        if (!b)
            throw new RuntimeException();}

    public static void main (String[] args) {
        System.out.println("StrategyPattern5.java");

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

