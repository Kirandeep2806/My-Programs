import java.io.*;

class C1 {
    static int val = 10;
    String str;
    C1() {
        System.out.println("Hello");
    }

    C1(String str) {
        this.str = str;
    }

    int rv(int setVal) {
        val = setVal;
        return val;
    }

    int rv() {
        val = 10;
        return val;
    }
}

public class CompileTimePolymorphism {
    public static void main(String[] args)
    throws IOException {
        C1 c11 = new C1("Kiran");
        System.out.println(c11.str); // Kiran
        System.out.println(c11.rv(100)); // 100
        C1 c21 = new C1(); // Hello
        System.out.println(c21.rv()); // 10
    }
}
