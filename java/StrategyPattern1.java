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
