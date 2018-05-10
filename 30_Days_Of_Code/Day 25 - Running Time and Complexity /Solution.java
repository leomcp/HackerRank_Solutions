import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    
    public static boolean isPrime(int n){
        
        if((n > 2 && n % 2 == 0) || n == 1){
            return false;
        }
        
        int top = (int) Math.sqrt(n) + 1;
        for(int i = 3; i< top; i += 2){
            if(n % i == 0)
                return false;
        }
        
        return true;
    }

    public static void main(String[] args) {
        /* Enter your code here. */
        Scanner scn = new Scanner(System.in);
        int cases = scn.nextInt();   
        for(int i = 0; i< cases; i++){
            int num = scn.nextInt();
            if(isPrime(num))
                System.out.println("Prime");
            else
                System.out.println("Not prime"); 
        }
    }
}



