 import java.util.*;

public class fragile
{
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter flag: ");
        String userInput = scanner.next();
        String input = userInput.substring("rtcp{".length(),userInput.length()-1);
        System.out.println("What you inputed is: ");
        System.out.println(userInput);
        System.out.println("Stripped flag is:" );
        System.out.println(input);
        System.out.println("Reversed answer is: ");
        reverse();
        if (check(input)) {
            System.out.println("Access granted.");
        } else {
            System.out.println("Access denied!");
        }
    }
    
    public static boolean check(String input){
        boolean h = false;
        String flag = "h1_th3r3_1ts_m3";
        String theflag = "";
        if(input.length() != flag.length()){
            return false;
        }
        for(int i = 0; i < flag.length(); i++){
            theflag += (char)((int)(flag.charAt(i)) + (int)(input.charAt(i)));
        }
        return theflag.equals("ÐdØÓ§åÍaèÒÁ¡");
    }

    public static void reverse(){
        String flag = "h1_th3r3_1ts_m3";
        String realFlag = "ÐdØÓ§åÍaèÒÁ¡";
        String theflag = "";
        for(int i = 0; i < flag.length(); i++){
            theflag += (char)((int)(realFlag.charAt(i)) - (int)(flag.charAt(i)));
        }
        System.out.println("rtcp{"+ theflag + "}");
    }
}