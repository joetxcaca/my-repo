// -----------
// Fri, 29 Apr
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
StrategyPattern6.java
*/

// ---------------------
// StrategyPattern6.java
// ---------------------

import java.util.Vector;

/*
Collection
AbstractCollection

List
AbstractList

ArrayList
LinkedList
*/

interface Price {
    double amount (int daysRented);
    int    points (int daysRented);}

abstract class AbstractPrice implements Price {
    public int pointsHelper (int daysRented) {        // const
        return 1;}}

class RegularPrice extends AbstractPrice {
    public double amount (int daysRented) {   // const
        double result = 2;
        if (daysRented > 2)
            result += (daysRented - 2) * 1.5;
        return result;}}

    public int points (int daysRented) {      // const
        return super.pointsHelper(daysRented)

class NewReleasePrice extends AbstractPrice {
    public double amount (int daysRented) {   // const
        return daysRented * 3;}

    public int points (int daysRented) {      // const
        return (daysRented > 1) ? 2 : 1;}}

class ChildrensPrice extends AbstractPrice {
    public double amount (int daysRented) {   // const
        double result = 1.5;
        if (daysRented > 3)
            result += (daysRented - 3) * 1.5;
        return result;}}

    public int points (int daysRented) {      // const
        return super.pointsHelper(daysRented)

class HorrorPrice extends AbstractPrice {
    public double amount (int daysRented) {   // const

    public int points (int daysRented) {      // const

class John {}

/*
for every class that you define in Java
Java will create a special instance of of class Class that describes your class
*/

class Connor {
    public int f ()
    public static int sf () {}
    }

Connor.sf();

Connor c = new Connor();
c.f();

class Class {
    public static Class forName (string s) {...}
    ...}

enum

class Movie {
    public static final string REGULAR     = "RegularPrice";
    public static final string NEW_RELEASE = "NewReleasePrice";
    public static final string CHILDRENS   = "ChildrensPrice";
    public static final string HORROR      = "HorrorPrice";

    private String _title;
    private Price  _price;

    public Movie (String title, string priceName) {
        _title = title;
        setPrice(priceName);}

    public void setPrice (string priceName) { // let's pretend "HorrorPrice"
        Class c1 = Class.forName(priceName);  // c1 is an instance of class Class that describes class HorrorPrice
        Class c2 = Class.forName(priceName);
        System.out.println(c1 == c2);         // true
        _price = (Price) c1.newInstance();               // o is an instance of class HorrorPrice

/*
        switch (priceCode) {                                                  // used once, still have a switch!
            case Movie.REGULAR:
                _price = new RegularPrice();
                break;
            case Movie.NEW_RELEASE:
                _price = new NewReleasePrice();
                break;
            case Movie.CHILDRENS:
                _price = new ChildrensPrice();
                break;
            case Movie.HORROR
                _price = new HorrorPrice();
                break;
            default:
                throw new IllegalArgumentException("Incorrect Price Code");}}
*/

    public double amount (int daysRented) { // const
        return _price.amount(daysRented);}

    public int points (int daysRented) {   // const
        return _price.points(daysRented);}

    public String statement (int daysRented) {                  // const
        return
            "\t" + _title                             +
            "\t" + String.valueOf(amount(daysRented)) + "\n";}}

class Rental {
    private Movie _movie;
    private int   _daysRented;

    public Rental (Movie movie, int daysRented) {
        _movie      = movie;
        _daysRented = daysRented;}

    public double amount () {               // const
        return _movie.amount(_daysRented);}

   public int points () {                   // const
        return _movie.points(_daysRented);}

     public String statement () {               // const
        return _movie.statement(_daysRented);}}

class Customer {
    private String         _name;
    private Vector<Rental> _rentals = new Vector<Rental>();

    public Customer (String name) {
        _name = name;}

    public void addRental (Rental rental) {
        _rentals.addElement(rental);}

    private double amount () {           // const, O(n)
        double result = 0;
        for (Rental rental : _rentals) {
            result += rental.amount();}
        return result;}

    private int points () {              // const, O(n)
        int result = 0;
        for (Rental rental : _rentals) {
            result += rental.points();}
        return result;}

    public String statement () {                             // const, O(3n)
        String result = "Rental Record for " + _name + "\n";
        for (Rental rental : _rentals) {
            result += rental.statement();}
        result +=
            "Amount owed is "        +
            String.valueOf(amount()) + "\n";
        result +=
            "You earned "              +
            String.valueOf(points())   +
            " frequent renter points";
        return result;}}

final class StrategyPattern6 {
    public static void main (String[] args) {
        System.out.println("StrategyPattern6.java");

        Customer x = new Customer("Penelope");
        assert x.statement().equals(
            "Rental Record for Penelope\n" +
            "Amount owed is 0.0\n"         +
            "You earned 0 frequent renter points");

        x.addRental(new Rental(new Movie("Shane", Movie.REGULAR), 2));
        assert x.statement().equals(
            "Rental Record for Penelope\n" +
            "\tShane\t2.0\n"               +
            "Amount owed is 2.0\n"         +
            "You earned 1 frequent renter points");

        x.addRental(new Rental(new Movie("Red River", Movie.REGULAR), 5));
        assert x.statement().equals(
            "Rental Record for Penelope\n" +
            "\tShane\t2.0\n"               +
            "\tRed River\t6.5\n"           +
            "Amount owed is 8.5\n"         +
            "You earned 2 frequent renter points");

        x.addRental(new Rental(new Movie("Giant", Movie.NEW_RELEASE), 1));
        assert x.statement().equals(
            "Rental Record for Penelope\n" +
            "\tShane\t2.0\n"               +
            "\tRed River\t6.5\n"           +
            "\tGiant\t3.0\n"               +
            "Amount owed is 11.5\n"        +
            "You earned 3 frequent renter points");

        x.addRental(new Rental(new Movie("2001", Movie.NEW_RELEASE), 3));
        assert x.statement().equals(
            "Rental Record for Penelope\n" +
            "\tShane\t2.0\n"               +
            "\tRed River\t6.5\n"           +
            "\tGiant\t3.0\n"               +
            "\t2001\t9.0\n"                +
            "Amount owed is 20.5\n"        +
            "You earned 5 frequent renter points");

        x.addRental(new Rental(new Movie("Big Country", Movie.CHILDRENS), 3));
        assert x.statement().equals(
            "Rental Record for Penelope\n" +
            "\tShane\t2.0\n"               +
            "\tRed River\t6.5\n"           +
            "\tGiant\t3.0\n"               +
            "\t2001\t9.0\n"                +
            "\tBig Country\t1.5\n"         +
            "Amount owed is 22.0\n"        +
            "You earned 6 frequent renter points");

        x.addRental(new Rental(new Movie("Spartacus", Movie.CHILDRENS), 5));
        assert x.statement().equals(
            "Rental Record for Penelope\n" +
            "\tShane\t2.0\n"               +
            "\tRed River\t6.5\n"           +
            "\tGiant\t3.0\n"               +
            "\t2001\t9.0\n"                +
            "\tBig Country\t1.5\n"         +
            "\tSpartacus\t4.5\n"           +
            "Amount owed is 26.5\n"        +
            "You earned 7 frequent renter points");

        System.out.println("Done.");}}
