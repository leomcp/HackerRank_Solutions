/*
Problem : Implements Multiple Linear Regression 
for more information visit :-- https://www.hackerrank.com/challenges/s10-multiple-linear-regression
 */
package Statistics;
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
import java.util.Scanner;
import java.util.Arrays;
////////////////////////////////////////////////////////////////////////////////
public class MultipleLinearRegression {
    //--------------------------------------------------------------------------
    public static void main(String args[]){
        //Taking the input features and labels 
        Scanner scn=new Scanner(System.in);
        //m: No of feautres observed  n : No of feautres set 
        int n=scn.nextInt();
        int m=scn.nextInt();
        //Initializing matrices 
        double X[][]=new double[n][m+1];
        double Y[][]=new double[n][1];
        
        //Getting the data 
        for(int rows=0;rows<n;rows++){
            X[rows][0]=1;
            for(int cols=0;cols<m;cols++){
                X[rows][cols]=scn.nextDouble();
            }
            Y[rows][0]=scn.nextDouble();
        }
        
        //Finding matrix B 
        double XTX[][]=multiplyMatrix(transposeMatrix(X),X);
        double XTXInv[][]=inverseOfMatrix(XTX);
        double XTY[][]=multiplyMatrix(transposeMatrix(X),Y);
        double B[][]=multiplyMatrix(XTXInv,XTY);
        
        
        //Finding values for Q set 
        int q = scn.nextInt();
        for (int i = 0; i < q; i++) {
            double result = B[0][0];
            for (int row = 1; row < B.length; row++) {
                result += scn.nextDouble() * B[row][0];
            }
            System.out.println(result);
        }
        
        scn.close();
    }
    //--------------------------------------------------------------------------
    public static double[][] multiplyMatrix(double[][] A,double[][] B){
        int aRows = A.length;
        int aCols = A[0].length;
        int bRows = B.length;
        int bCols = B[0].length;
        
        double [][] C = new double[aRows][bCols];
        int cRows = C.length;
        int cCols = C[0].length;
        
        for (int row = 0; row < cRows; row++) {
            for (int col = 0; col < cCols; col++) {
                for (int i = 0; i < aCols; i++) {
                    C[row][col] += A[row][i] * B[i][col];
                }
            }
        }
        return C;
    }
    //--------------------------------------------------------------------------
    public static double[][] transposeMatrix(double[][] X){
         int originalRows =X.length;
        int originalCols = X[0].length;
        int rows = originalCols;
        int cols = originalRows;
        double [][] transpose = new double[rows][cols];
        
        /* Fill our new 2D array */
        for (int row = 0; row < originalRows; row++) {
            for (int col = 0; col < originalCols; col++) {
                transpose[col][row] = X[row][col];
            }
        }
        return transpose;
    }
    //--------------------------------------------------------------------------
    //--------------------------------------------------------------------------
    // to find inverse of a matrix is from 
    //http://www.sanfoundry.com/java-program-find-inverse-matrix/
    //--------------------------------------------------------------------------
    //--------------------------------------------------------------------------
    public static double[][] inverseOfMatrix(double a[][]) {
        int n = a.length;
        double x[][] = new double[n][n];
        double b[][] = new double[n][n];
        int index[] = new int[n];
        for (int i=0; i<n; ++i) 
            b[i][i] = 1;
        // Transform the matrix into an upper triangle
        gaussian(a, index);

        // Update the matrix b[i][j] with the ratios stored
        for (int i=0; i<n-1; ++i)
            for (int j=i+1; j<n; ++j)
                for (int k=0; k<n; ++k)
                    b[index[j]][k]
                    	    -= a[index[j]][i]*b[index[i]][k];
 
        // Perform backward substitutions
        for (int i=0; i<n; ++i) {
            x[n-1][i] = b[index[n-1]][i]/a[index[n-1]][n-1];
            for (int j=n-2; j>=0; --j) {
                x[j][i] = b[index[j]][i];
                for (int k=j+1; k<n; ++k) {
                    x[j][i] -= a[index[j]][k]*x[k][i];
                }
                x[j][i] /= a[index[j]][j];
            }
        }
        return x;
    }
 
    // Method to carry out the partial-pivoting Gaussian
    // elimination.  Here index[] stores pivoting order.
 
    public static void gaussian(double a[][], int index[]) {
        int n = index.length;
        double c[] = new double[n];
 
        // Initialize the index
        for (int i=0; i<n; ++i) 
            index[i] = i;
 
        // Find the rescaling factors, one from each row
        for (int i=0; i<n; ++i) {
            double c1 = 0;
            for (int j=0; j<n; ++j) {
                double c0 = Math.abs(a[i][j]);
                if (c0 > c1) c1 = c0;
            }
            c[i] = c1;
        }
 
        // Search the pivoting element from each column
        int k = 0;
        for (int j=0; j<n-1; ++j) {
            double pi1 = 0;
            for (int i=j; i<n; ++i) {
                double pi0 = Math.abs(a[index[i]][j]);
                pi0 /= c[index[i]];
                if (pi0 > pi1) {
                    pi1 = pi0;
                    k = i;
                }
            }
  
        // Interchange rows according to the pivoting order
            int itmp = index[j];
            index[j] = index[k];
            index[k] = itmp;
            for (int i=j+1; i<n; ++i) 	{
                double pj = a[index[i]][j]/a[index[j]][j];
 
        // Record pivoting ratios below the diagonal
                a[index[i]][j] = pj;
 
        // Modify other elements accordingly
                for (int l=j+1; l<n; ++l)
                    a[index[i]][l] -= pj*a[index[j]][l];
            }
        }
    }
    //--------------------------------------------------------------------------
}
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
/*
Output :
2 7
0.18 0.89 109.85
1.0 0.26 155.72
0.92 0.11 137.66
0.07 0.37 76.17
0.85 0.16 139.75
0.99 0.41 162.6
0.87 0.47 151.77
4
0.49 0.18
0.57 0.83
0.56 0.64
0.76 0.18
105.21455835106984
142.6709513072996
132.9360546912473
129.7017540450249
*/
