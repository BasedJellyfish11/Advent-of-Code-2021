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
	public static String temp = ""; 
	public static ArrayList<String> yea = new ArrayList<String>();
	public static ArrayList<String> oneStart = new ArrayList<String>();
	public static ArrayList<String> zeroStart = new ArrayList<String>();
	public static ArrayList<String> oneLeftover = new ArrayList<String>();
	public static ArrayList<String> zeroLeftover = new ArrayList<String>();
	
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
		int count = 0;
		for(int i  = 0; i < 12; i++)
		{	
			for(int k = 0; k < yea.size(); k++)
			{
				if(yea.get(k).charAt(i) == '0')
				{
					zeroStart.add(yea.get(k));
				}
				else
				{
					oneStart.add(yea.get(k));
				}
			}
			while(count < oneStart.size())
			{
				if(oneStart.size() > zeroStart.size())
			    {
					if(oneStart.get(count).charAt(i) != '1')
					{
						System.out.println(oneStart.get(count));
						oneLeftover.add(oneStart.get(count));
					}
				}
				count++;
			}
			count = 0; //garbage
		}
		System.out.println(oneLeftover.size());
		System.out.println("Gamma rate: " +oneLeftover.get(4));
		System.out.println("Epsilon rate: " +epsilon);
	}
}

/*
for(int i = 12; i > -1; i--)
{
	for(int j = 0; j < yea.size(); j++)
	{
		double temp = 0;
		double temp2 = Math.pow(1, i);
		temp = yea.get(j) / temp2;
		if(temp == 0)
		zero++;
		if(temp == 1)
	    one++;	
	}
	if(zero > one)
	{
		gamma = gamma + "0";
		epsilon = epsilon + "1";
	} else
	{
		gamma = gamma + "1";
		epsilon = epsilon + "0";
	}
}

		for(int i = 0; i < 12; i++)
		{
			for(int j = 0; j < 12; j++)
			{
				for(int k = 0; k < yea.size(); k++)
				{
					if(yea.get(k).charAt(j) == '0')
					{
						zeroStart.add(yea.get(k));
					}
					else
					{
						oneStart.add(yea.get(k));
					}
				}
				if(zeroStart.size() > oneStart.size())
				{
					zeroStart.forEach((temp) -> zeroLeftover.add(temp));
					if(zeroLeftover.get(j).charAt(i) != '0')
					{ 
						zeroLeftover.remove(j);					
					}	
				}
				zeroStart.clear();
				oneStart.clear();
			}
		}
		System.out.println(zeroLeftover.size());
		System.out.println("Gamma rate: " +zeroLeftover.get(0));
		System.out.println("Epsilon rate: " +epsilon);
	}
}
*/
