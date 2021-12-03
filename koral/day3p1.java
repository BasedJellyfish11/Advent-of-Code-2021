package packy;

import java.lang.Math;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class day3
{
	public static int zero;
	public static int one;
	public static String gamma = "";
	public static String epsilon = "";
	
	public static ArrayList<String> yea = new ArrayList<String>();
	public static void main(String[] args)
	{
		try {
		      File myObj = new File("day3.txt");
		      Scanner myReader = new Scanner(myObj);
		      while (myReader.hasNextLine()) {
		        String data = myReader.nextLine();
		        yea.add(data);
		        //System.out.println(Integer.parseInt(data, 2));
		      }
		      myReader.close();
		    } catch (FileNotFoundException e) {
		      System.out.println("An error occurred.");
		      e.printStackTrace();
		    }
		
		for(int i = 0; i < 12; i++)
		{
			for(int j = 0; j < yea.size(); j++)
			{
				if(yea.get(j).charAt(i) == '0')
				{
					zero++;
				}
				else
				{
					one++;
				}
			}
			System.out.println(zero);
			System.out.println(one);
			if(zero > one)
			{
				gamma = gamma + "0";
				epsilon = epsilon + "1";
			} else
			{
				gamma = gamma + "1";
				epsilon = epsilon + "0";
			}
			zero = 0;
			one = 0;
		}
		System.out.println("Gamma rate: " +gamma);
		System.out.println("Epsilon rate: " +epsilon);
		int total = Integer.parseInt(epsilon, 2) * Integer.parseInt(gamma, 2);
		System.out.println(total);
	}
}
