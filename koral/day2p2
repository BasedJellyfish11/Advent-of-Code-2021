package packy;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class day2
{
	public static int position;
	public static int depth;
	public static String[] temp;
	public static int aim;
	public static ArrayList<String> yea = new ArrayList<String>();
   
	public static void main(String[] args)
	{
		 try {
		      File myObj = new File("day2.txt");
		      Scanner myReader = new Scanner(myObj);
		      while (myReader.hasNextLine()) {
		        String data = myReader.nextLine();
		        yea.add(data);
		      }
		      myReader.close();
		    } catch (FileNotFoundException e) {
		      System.out.println("An error occurred.");
		      e.printStackTrace();
		    }
		 
		 for(int i = 0; i < yea.size(); i++)
		 {
			temp = yea.get(i).split(" ");
			if(yea.get(i).contains("forward"))
			{
				position = position + (Integer.valueOf(temp[1]));
				depth += ((Integer.valueOf(temp[1]) * aim));
			}
			else if(yea.get(i).contains("down"))
			{
				aim += Integer.valueOf(temp[1]);
			}
			else if(yea.get(i).contains("up"))
			{
				aim -= Integer.valueOf(temp[1]);
			}
		 }
	     int total = position * depth;
	     System.out.println(total);
	}
}
