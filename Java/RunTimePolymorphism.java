import java.io.*;
import java.util.*;

class ParentClass {
    void name(String name) {
        System.out.println("Parent name is : " + name);
    }
}

class ChildClass extends ParentClass {
    @Override
    void name(String childName) { // overriding the method of parent class with same signature and return
        // Override happens even if we no annotation is specified
        // If u change the method name here it gives error
        super.name(childName); // calling superclass's version to print its own value    
        System.out.println("\nChild Name: " + childName+"\t");
    }
}


public class RunTimePolymorphism {
    public static void main(String[] args)
    throws IOException {
        // Scanner sc = new Scanner(System.in);
        // String name = sc.nextLine();
        ParentClass parent=new ParentClass();
        parent.name("Kiran");
        ParentClass child = new ChildClass();
        child.name("Deep");
        // sc.close();
    }
}
