package packy;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class day3
{
	public static ArrayList<String> yea = new ArrayList<String>();
	
	public static void fileRead(String file)
	{
		try {
		      File myObj = new File(file);
		      Scanner myReader = new Scanner(myObj);
		      while (myReader.hasNextLine()) {
		        String data = myReader.nextLine();
		        yea.add(data);
		        //System.out.println(Integer.parseInt(data, 2));
		      }
		      System.out.println("file read");
		      myReader.close();
		    } catch (FileNotFoundException e) {
		      System.out.println("An error occurred.");
		      e.printStackTrace();
		    }
	}
	
	public static void main(String[] args)
	{
	     fileRead("day3.txt");
	     String oxygen = oxygen(yea);
	     System.out.println(oxygen);
	     fileRead("day3.txt");
	     String carbon = carbon(yea);
	     System.out.println(carbon);
	     int total = Integer.parseInt(oxygen, 2) * Integer.parseInt(carbon, 2);
	     System.out.println(total);
	}
	
	public static boolean checkGreater(int first, int second)
	{
		if(first > second)
		return true;
		if(first < second)
		return false;
		//if(second == first)
		//return false;	
		
		return true;
	}
	
	public static boolean checkFewer(int first, int second)
	{
		if(first > second)
		return false;
		if(first < second)
		return true;
		//if(second == first)
		//return true;	
		
		return true;
	}
	
    public static String oxygen(ArrayList<String> array)
    {
		int zero = 0;
		int one = 0;
		int count = 0;
		String temp = "";
    	ArrayList<String> data = array;
    	for(int i = 0; i < 12; i++)
    	{
    		for(int j = 0; j < data.size(); j++)
    		{
    			if(data.get(j).charAt(i) == '0')
    			{
    				zero++;
    			} else
    				one++;
    		}
    		System.out.println("z: "+zero);
    		System.out.println("o: "+one);
    		if(checkGreater(zero, one) == false || zero == one) //if true, remove all ones, if false, remove all zeros
    		{
    			while(zero > 0)
    			{
    				if(count == data.size())
        				count = 0;
    				if(data.get(count).charAt(i) == '0')
    				{
	    				data.remove(count);
	    				zero--;
	    				count = 0;
    				}
    				count++;
    			}
    		} 
    		else if(checkGreater(zero, one) == true)
    		{
    			while(one > 0)
    			{
    				if(count == data.size())
        				count = 0;
    				if(data.get(count).charAt(i) == '1')
    				{
	    				data.remove(count);
	    				one--;
	    				count = 0;
    				}
    				count++;
    			}
    		}
    		zero = 0;
    		one = 0;
    		count = 0;
    		System.out.println(data);
    		if(data.size() == 1)
    		{
    			temp = data.get(0);
    			break;
    		}
    		temp = data.get(0);
    	}
    	return temp;
    }
    
    public static String carbon(ArrayList<String> array)
    {
		int zero = 0;
		int one = 0;
		int count = 0;
		String temp = "";
    	ArrayList<String> data = array;
    	for(int i = 0; i < 12; i++)
    	{
    		for(int j = 0; j < data.size(); j++)
    		{
    			if(data.get(j).charAt(i) == '0')
    			{
    				zero++;
    			} else
    				one++;
    		}
    		System.out.println("z: "+zero);
    		System.out.println("o: "+one);
    		if(checkFewer(zero, one) == false)
    		{
    			while(zero > 0)
    			{
    				if(count == data.size())
    				count = 0;
    				if(data.get(count).charAt(i) == '0')
    				{
	    				data.remove(count);
	    				zero--;
 	    				count = 0;
    				}
    				count++;
    			}
    		} 
    		else if(checkFewer(zero, one) == true || zero == one )
    		{
    			while(one > 0)
    			{
    				if(count == data.size())
        				count = 0;
    				if(data.get(count).charAt(i) == '1')
    				{
	    				data.remove(count);
	    				one--;
	    				count = 0;
    				}
    				count++;
    			}
    		}
    		zero = 0;
    		one = 0;
    		count = 0;
    		System.out.println(data);
    		if(data.size() == 1)
    		{
    			temp = data.get(0);
    			break;
    		}
    		temp = data.get(0);
    	}
    	return temp;
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

/*
int count = 0;
for(int k = 0; k < yea.size(); k++)
{
	if(yea.get(k).charAt(0) == '0')
	{
		zeroStart.add(yea.get(k));
	}
	else
	{
		oneStart.add(yea.get(k));
	}
}
for(int i  = 0; i < 12; i++)
{	
	while(count < oneStart.size())
	{
		if(oneStart.get(count).charAt(i) != '1')
		{
			oneLeftover.add(oneStart.get(count));
		}
		
		if(zeroStart.get(count).charAt(i) != '0')
		{
			zeroLeftover.add(zeroStart.get(count));
		}
		
		if(count < oneLeftover.size() || count < zeroLeftover.size())
		{
			if(oneLeftover.size() > zeroLeftover.size())
		    {
				if(oneLeftover.get(count).charAt(i) != '1')
				{
					oneLeftover.remove(count);
				}
			}
			if(zeroLeftover.size() > oneLeftover.size())
		    {
				if(zeroLeftover.get(count).charAt(i) != '0')
				{
					zeroLeftover.remove(count);
				}
			}
		}
		count++;
	}
	System.out.println(count);
	count = 0;
}
*/

/*

		    int count = 0;
		
			for(int i = 0; i < yea.size(); i++)
			{
				 if(yea.get(i).charAt(0) == '0')
				 {
					 zeroStart.add(yea.get(i));
				 } else
				 {
					 oneStart.add(yea.get(i));
				 }			 
			}
			System.out.println("Start: " +zeroStart.size());
			System.out.println("Start: " +oneStart.size());
			zero = 0;
			one = 0;
			
			while(oneStart.size() != 1)
			{
				int temp = oneStart.size();
				for(int h = 0; h < oneStart.size(); h++)
				{
					if(oneStart.get(h).charAt(count) == '0')
					 {
						 zero++;
					 } else
					 {
						 one++;
					 }			
				}
				System.out.println("zero: "+zero);
				System.out.println("one: "+one);
				System.out.println("count: "+count);
				
				if(zero < one)
				{
				oneFewer = true;
				//System.out.println(oneGreater);
				}
				else if (one < zero)
				{
				oneFewer = false;
				}
				else if(one == zero)
				{
				oneFewer = false;	
				}
				for(int i = 0; i < oneStart.size(); i++)
				{
					if(oneFewer == false)
					{
						if(oneStart.get(i).charAt(count) == '0')
						{
							//System.out.print(oneStart.get(i)+" ");
							//System.out.println(oneFewer);
							oneStart.remove(i);
						}
					}
					else if(oneFewer == true)
					{
						if(oneStart.get(i).charAt(count) == '1')
						{
							//System.out.println(oneFewer);
							oneStart.remove(i);
						}
					}
				  System.out.println("Size: " +oneStart.size());
				  bruh++;
				}
				System.out.println(bruh);
				//System.out.println("Size: " +oneStart.size());
				if(count == 11)
				count = 0;	
				count++;

				zero = 0;
				one = 0;
				bruh = 0;
			}
			zero = 0;
			one = 0;
			count = 0;
			while(zeroStart.size() != 1)
			{
				for(int h = 0; h < zeroStart.size(); h++)
				{
					if(zeroStart.get(h).charAt(count) == '0')
					 {
						 zero++;
					 } else
					 {
						 one++;
					 }			
				}
				System.out.println("zero: "+zero);
				System.out.println("one: "+one);
				System.out.println("count: "+count);
				if(zero > one)
				{
				oneGreater = false;
				//System.out.println(oneGreater);
				}
				else if (one > zero)
				{
				oneGreater = true;
				}
				else if(one == zero)
				{
				oneGreater = false;	
				}
				for(int i = 0; i < zeroStart.size(); i++)
				{
					if(oneGreater == false)
					{
						if(zeroStart.get(i).charAt(count) == '0')
						{
							zeroStart.remove(i);
						}
					}
					else if(oneGreater == true)
					{
					    //System.out.println(oneGreater);
						if(zeroStart.get(i).charAt(count) == '1')
						{
							zeroStart.remove(i);
						}
					}
					System.out.println("Size: " +zeroStart);
				}
				//System.out.println("Size: " +oneStart.size());
				if(count == 11)
				count = 0;	
				count++;

				zero = 0;
				one = 0;
			}
		System.out.println("Oxygen: " +zeroStart);
		System.out.println("CO2: " +oneStart);
		int total = Integer.parseInt(zeroStart.get(0), 2) * Integer.parseInt(oneStart.get(0), 2);
		System.out.println(total);
		
	}
}

*/

