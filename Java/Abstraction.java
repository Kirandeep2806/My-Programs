import java.io.*;
import java.util.*;

abstract class DBManage {
    HashMap<Integer, String> hm = new HashMap<>();
    public abstract void setData(int roll, String name);
    public abstract String getData(int roll);
}

class Google extends DBManage {
    @Override
    public void setData(int roll, String name) {
        hm.put(roll, name);
    }
    @Override
    public String getData(int roll) {
        return hm.get(roll);
    }
}

public class Abstraction {
    public static void main(String[] args)
    throws IOException {
        Google g = new Google();
        g.setData(313, "Kiran Deep");
        System.out.println(g.getData(313));
    }
}
