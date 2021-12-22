import java.util.*;

class Person {
    protected String firstName;
    protected String lastName;
    protected int idNumber;

    // Constructor
    Person(String firstName, String lastName, int identification) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.idNumber = identification;
    }

    // Print person data
    public void printPerson() {
        System.out.println(
                "Name: " + lastName + ", " + firstName
                        + "\nID: " + idNumber);
    }

}

class Day12 extends Person { // class Day12 extends Person
    private int[] testScores;

    public Day12(String firstName, String lastName, int identification, int[] testScores) { // public Day12
        super(firstName, lastName, identification);
        this.testScores = testScores;
    }

    public char calculate() {
        int sum = 0, score = 0;
        for (int i : this.testScores)
            sum += i;
        // System.out.println(i);
        score = sum / this.testScores.length;
        if (90 <= score && score <= 100)
            return 'O';
        else if (80 <= score && score < 90)
            return 'E';
        else if (70 <= score && score < 80)
            return 'A';
        else if (55 <= score && score < 70)
            return 'P';
        else if (40 <= score && score < 55)
            return 'D';
        else
            return 'T';
    }

    /*
     * Class Constructor
     * 
     * @param firstName - A string denoting the Person's first name.
     * 
     * @param lastName - A string denoting the Person's last name.
     * 
     * @param id - An integer denoting the Person's ID number.
     * 
     * @param scores - An array of integers denoting the Person's test scores.
     */
    // Write your constructor here

    /*
     * Method Name: calculate
     * 
     * @return A character denoting the grade.
     */
    // Write your method here

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String firstName = scan.next();
        String lastName = scan.next();
        int id = scan.nextInt();
        int numScores = scan.nextInt();
        int[] testScores = new int[numScores];
        for (int i = 0; i < numScores; i++) {
            testScores[i] = scan.nextInt();
        }
        scan.close();

        Day12 s = new Day12(firstName, lastName, id, testScores);
        s.printPerson();
        System.out.println("Grade: " + s.calculate());
    }
}