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

class Child2 extends Child1 {
    Child2() {
        super();
    }
    void callParent() {
        super.callParent();
        // If u wont put super it'd give stack overflow coz it undergoes recursion
    }
}

public class MultilevelInheritance {
    public static void main(String[] args)
    throws IOException {
        Child2 c2  = new Child2();
        c2.callParent();
    }
}
