import java.util.*;


public class Test {
    public static void main(String[] args) throws Exception{
        String regix = "(\\w*)\\((\\w,*)\\)";
        String text = "adb(ag,va分隔符afaa)";
        String result = text.replaceAll(regix, "|");
        System.out.print(result);

    }
}
