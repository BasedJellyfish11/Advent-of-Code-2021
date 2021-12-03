package packy;

import java.io.File;
import java.io.FileNotFoundException; 
import java.util.Scanner; 
import java.util.ArrayList;

public class day1 
{
	
  public static ArrayList<Integer> yea = new ArrayList<Integer>();
  public static int count; 
  
  public static void main(String[] args) {
    try {
      File myObj = new File("day1.txt");
      Scanner myReader = new Scanner(myObj);
      while (myReader.hasNextLine()) {
        String data = myReader.nextLine();
        yea.add(Integer.valueOf(data));
      }
      myReader.close();
    } catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
    
    for(int i = 0; i < yea.size(); i++)
    {
        if(i == yea.size() - 1)
        break;  //pepodab
        
    	if(yea.get(i + 1) > yea.get(i))
    	{
    	    count++;
    	}
    }
    System.out.println(count);
  }
}
