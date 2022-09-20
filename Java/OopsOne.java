import java.io.*;

class Dogs {

    /* Order of execution of initialization block : 
     * 1. Static Initialization block - static {...........}
     * 2. Naive Initialization block -  {.............}
     * 3. Constructor -                 <ClassName>() {......}
     */
    static String breed = "Pomarian";

    {
        breed = "Pug";
        System.out.println("I am Broono!!");
    }
    static {
        breed = "Husky";
        System.out.println("I am Kiran");
    }

    String dogName;
    int age;
    public Dogs() {
        breed = "Labrador";
        System.out.println("Hi I am a Dog");
    }
}

public class OopsOne {
    {
        System.out.println("hi");
    }
    public static void main(String[] args)
    throws IOException {
        Dogs d = new Dogs();
        int age = d.age;
        String name = d.dogName;
        System.out.println(age + " " + name + " " + Dogs.breed);
        System.out.println(Dogs.breed);
    }
}
