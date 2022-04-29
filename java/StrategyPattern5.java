// ---------------------
// StrategyPattern5.java
// ---------------------

/*
Replace Type Code with State/Strategy (227)
move Method(142)

Replace Conditional with Polymorphism (225)
create Price
create RegularPrice
create NewReleasePrice
create ChildrensPrice

remove getPriceCode()
remove getTitle()

change setPriceCode() to setPrice()
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
        _priceCode = priceCode;}

    public double amount (int daysRented) {           // const
        double result = 0;
        switch (getPriceCode()) {                     // why not _priceCode
            case Movie.REGULAR:
                result += 2;
                if (daysRented > 2)
                    result += (daysRented - 2) * 1.5;
                break;
            case Movie.NEW_RELEASE:
                result += daysRented * 3;
                break;
            case Movie.CHILDRENS:
                result += 1.5;
                if (daysRented > 3)
                    result += (daysRented - 3) * 1.5;
                break;}
        return result;}

    public int points (int daysRented) {             // const
        if ((getPriceCode() == Movie.NEW_RELEASE) && // why not _priceCode
            (daysRented     >  1))
            return 2;
        return 1;}

    public String statement (int daysRented) {                  // const
        return
            "\t" + getTitle()                         +
            "\t" + String.valueOf(amount(daysRented)) + "\n";}}

class Rental {
    private Movie _movie;
    private int   _daysRented;

    public Rental (Movie movie, int daysRented) {
        _movie      = movie;
        _daysRented = daysRented;}

    public double amount () {               // const
        return _movie.amount(_daysRented);}

    public int points () {                  // const
        return _movie.points(_daysRented);}

    public String statement () {                // const
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
