import java.util.*;

/**
 * ArrayPractice
 */
public class ArrayPractice {

    public static void main(String[] args) {
        ArrayList<String> arrayList1 = new ArrayList<>();
        ArrayList<String> arrayList2 = new ArrayList<>();
        arrayList1.add("Hello");
        arrayList1.add("World");
        arrayList1.add("!");
        arrayList1.add(0, "Kiran, ");

        arrayList2.add("I'm John.");
        arrayList2.add("I'm good boy");

        System.out.println(arrayList1);
    }
}
