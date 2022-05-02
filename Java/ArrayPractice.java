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

        Object[] obj = arrayList1.toArray();

        for (Object i : obj) {
            System.out.println(i);
        }

        Integer[] arr = new Integer[] { 31, 4, 30 };
        Arrays.sort(arr);
        for (int i : arr)
            System.out.println(i);

        System.out.println(arr.getClass());


        // Arrays.sort(arr, Collections.reverseOrder()); // Arrays.sort() accepts array & Comparator(optional) as arguments.

        Collections.sort(Arrays.asList(arr), Collections.reverseOrder()); // Collections.sort() accepts List & Comparator(optional) as argumentS.
        
        for (Integer i : arr) {
            System.out.println(i);
        }

        System.out.println(Arrays.asList(arr).getClass());
        System.out.println(arr.getClass());

        List<Integer> list = new ArrayList<>(Arrays.asList(arr));
        list.add(32);

        Collections.sort(list);

        for (Integer i : list) {
            System.out.println(i);
        }

    }
}
