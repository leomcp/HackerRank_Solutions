/*
PROBLEM : 
Given two n-element data sets, X and Y, calculate the value of Spearman's rank 
correlation coefficient.
 */
package Statistics;
////////////////////////////////////////////////////////////////////////////////
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;
////////////////////////////////////////////////////////////////////////////////
public class SpearmanRankCorrelationCoefficient {
    public static double xElems[];
    public static double yElems[];
    public static int n=0;
    //--------------------------------------------------------------------------
    public static void main(String args[]){
        Scanner scn=new Scanner(System.in);
        n=scn.nextInt();
        
        xElems=new double[n];
        yElems=new double[n];
        
        for(int i=0; i<n; i++)
            xElems[i]=scn.nextDouble();
        
        for(int i=0;i<n;i++)
            yElems[i]=scn.nextDouble();
        
        scn.close();
        
        System.out.format("%.3f",spearmansCorrCoeff());
    }
    //--------------------------------------------------------------------------
    public static Double spearmansCorrCoeff(){
        
        if (xElems == null || yElems == null || xElems.length != yElems.length) {
            return null;
        }
        
        int [] rankX = getRanks(xElems);
        int [] rankY = getRanks(yElems);

        //Spearman's formula 
        int n = xElems.length;
        double numerator = 0;
        for (int i = 0; i < n; i++) {
            numerator += Math.pow((rankX[i] - rankY[i]), 2);
        }
        numerator *= 6;
        return 1 - numerator / (n * ((n * n) - 1));
    }
    //--------------------------------------------------------------------------
     public static int[] getRanks(double [] array) {
        int n = array.length;
        
        // Create pairs and sort by values 
        Pair [] pair = new Pair[n];
        for (int i = 0; i < n; i++) {
            pair[i] = new Pair(i, array[i]);
        }
        
        Arrays.sort(pair, new PairValueComparator());

        /* Create and return ranks[] */
        int [] ranks = new int[n];
        int rank = 1;
        for (Pair p : pair) {
            ranks[p.index] = rank++;
        }
        return ranks;
    }
    //--------------------------------------------------------------------------
}
////////////////////////////////////////////////////////////////////////////////
class Pair {
    public final int    index;
    public final double value;
    //--------------------------------------------------------------------------
    public Pair(int index, double value) {
        this.index = index;
        this.value = value;
    }
    //--------------------------------------------------------------------------
}
////////////////////////////////////////////////////////////////////////////////
class PairValueComparator implements Comparator<Pair> {
    double epsilon = 0.0001; // shouldn't use " == " to compare "doubles"
    @Override
    //--------------------------------------------------------------------------
    public int compare(Pair p1, Pair p2) {
        if (Math.abs(p1.value - p2.value) < epsilon) {
            return 0;
        } else if (p1.value < p2.value) {
            return -1;
        } else {
            return 1;
        }
    }
    //--------------------------------------------------------------------------
}
////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////////
/*
OUTPUT :

*/