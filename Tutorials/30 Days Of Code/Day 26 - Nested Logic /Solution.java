import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scn = new Scanner(System.in);
        
        int da = scn.nextInt();
        int ma = scn.nextInt();
        int ya = scn.nextInt();
        int de = scn.nextInt();
        int me = scn.nextInt();
        int ye = scn.nextInt();
        
        int fine = 0;
        
        if(ye == ya){
            if(me < ma){
                fine = (ma - me) * 500;
            }
            else if((ma == me) && (de < da)){
                fine = (da - de) * 15;
            }
        }
        else if(ye < ya){
            fine = 10000;
        }
        
        System.out.println(""+fine);
            
    }
}