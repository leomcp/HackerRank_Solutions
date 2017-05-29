/*
Problem : Program to implement Linear Regression techniques 

for more details visit : https://www.hackerrank.com/challenges/s10-least-square-regression-line
 */
package Statistics;
////////////////////////////////////////////////////////////////////////////////
public class LeastSquareRegressionRate {
    //--------------------------------------------------------------------------
    public static void main(String args[]){
        //Input data
        double [] x = {95, 85, 80, 70, 60};
        double [] y = {85, 95, 70, 65, 70};
        double student_Score = 80;
        //Get coefficients for least square regression line 
        double b = pearsonCorrCoff(x, y) * (calStdDeviation(y) / calStdDeviation(x));
        double a = calMean(y) - b * calMean(x);
        //Calculate and print predicted score 
        double result = a+b*student_Score;
        System.out.format("%.3f",result);
        
    }
    //--------------------------------------------------------------------------
    public static double pearsonCorrCoff(double x[],double y[]){
        return (covXY(x, y)/(x.length*calStdDeviation(x)*calStdDeviation(y)));
    }
    //--------------------------------------------------------------------------
    public static Double covXY(double x[],double y[]){
        if(x==null || y==null || x.length!=y.length)
            return null;
        
        double xMean=calMean(x);
        double yMean=calMean(y);
        double cov=0.0;
        for(int i=0;i<x.length;i++)
            cov+=((x[i]-xMean)*(y[i]-yMean));
        
        return cov;
    }
    //--------------------------------------------------------------------------
    public static Double calMean(double arr[]){
        if(arr ==null){
            return null;
        }
        double sum=0;
        for(double elem:arr)
            sum+=elem;
        return sum/arr.length;
    }
    //--------------------------------------------------------------------------
    public static Double calStdDeviation(double arr[]){
        if(arr==null)
            return null;
        double sum=0.0;
        double mean=calMean(arr);
        for(double elem:arr)
            sum+=Math.pow((elem-mean), 2);
        return Math.sqrt((sum/arr.length));
    }
    //--------------------------------------------------------------------------
    
}
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
/* 
OUTPUT :
78.2888
*/