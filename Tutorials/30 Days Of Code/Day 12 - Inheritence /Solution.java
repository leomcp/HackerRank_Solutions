class Student extends Person{
	private int[] testScores;

    /*	
    *   Class Constructor
    *   
    *   @param firstName - A string denoting the Person's first name.
    *   @param lastName - A string denoting the Person's last name.
    *   @param id - An integer denoting the Person's ID number.
    *   @param scores - An array of integers denoting the Person's test scores.
    */
    // Write your constructor here
    public Student(String firstname, String lastname, int id, int[] scores){
        super(firstname, lastname, id);
        this.testScores = scores;
    }
    /*	
    *   Method Name: calculate
    *   @return A character denoting the grade.
    */
    // Write your method here
    public char calculate(){
        double average = 0.0;
        
        for(int i=0; i<testScores.length; i++){
            average = average + testScores[i];
        }
        
        average = average / testScores.length;
        
        
        if(average<40)
            return 'T';
        else if(average<55)
            return 'D';
            else if (average<70)
                    return 'P';
                else if(average<80)
                    return 'A';
                    else if(average<90)
                        return 'E';
                        else
                            return 'O';
        
    }
}