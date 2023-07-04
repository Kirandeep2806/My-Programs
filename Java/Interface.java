import java.io.*;

interface Name {
    static final float PI = 3.14f;
    void setName(String name);
    String getName();
}

class Person implements Name {
    String name;

    @Override
    public void setName(String name) {
        this.name = name;
    }
    
    @Override
    public String getName() {
        return this.name;
    }
}

public class Interface {
    public static void main(String[] args)
    throws IOException {
        Person p = new Person();
        p.setName("Sanju");
        System.out.println(p.getName());
    }
}
