import java.io.*;

class Parent {
    static int val = 10;
    Parent() {
        System.out.println("Parent constructor called");
    }
    void print() {
        val++;
        System.out.println("I am the Parent " + val);
    }
}

class Child1 extends Parent {
    Child1() {
        super();
    }
    void callParent() {
        print();
    }
}

class Child2 extends Parent {
    Child2() {
        super();
    }
    void callParent() {
        print();
    }
}

public class HierarchicalInheritance {
    public static void main(String[] args)
    throws IOException {
        Child1 c1 = new Child1();
        Child2 c2 = new Child2();
        c1.callParent();
        c2.callParent();
    }
}
