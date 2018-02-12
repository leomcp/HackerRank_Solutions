/*
PROBLEM :
A manufacturer of metal pistons finds that, on average, 12% of the pistons they 
manufacture are rejected because they are incorrectly sized. What is the 
probability that a batch of 10 pistons will contain:
1. No more then 2 rejects?
2. At least 2 rejects?
 */
package Statistics;
////////////////////////////////////////////////////////////////////////////////
public class BinomialDistributionII {
    //--------------------------------------------------------------------------
    public static void main(String args[]){
        double p=0.12;
        int n=10;
        double result=0;
        //No more than 2 rejects 
        for (int x = 0; x <= 2; x++) {
            result += binomial(n, x, p);
        }
        System.out.format("%.3f%n", result);
        
        //At least 2 rejects
        result = 1 - binomial(n, 0, p) - binomial(n, 1, p);
        System.out.format("%.3f%n", result);
    }
    //--------------------------------------------------------------------------
    public static Double binomial(int x,int n, double p){
       if (p < 0 || p > 1 || n < 0 || x < 0 || x > n) {
            return null;
        }
        return combinations(n,x)*Math.pow(p, x)*Math.pow(1-p, n-x);
    }
    //--------------------------------------------------------------------------
    private static Long combinations(int n,int x){
        if(x<0 || n<0 || x>n){
            return null;
        }
        return factorial(n)/(factorial(x)*factorial(n-x));
    }
    //--------------------------------------------------------------------------
    private static Long factorial(int a){
        if(a<0){
            return null;
        }
        long result=1;
        while(a>0){
            result*=a--;
        }
        return result;
    }
    //--------------------------------------------------------------------------
}
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////