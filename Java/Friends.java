import java.util.Scanner;
import java.io.*;
//This program write date to a file
public class Friends
{
	public static void main(String[] args) throws IOException
	{
		String filename;
		String friendName;
		int numFriends;
		// a scanner object for keyboard input
		Scanner keyboard = new Scanner(System.in);
		// get the number  of friends
		System.out.print("How many friends do you have ?");
		numFriends = keyboard.nextInt();
		//consume the remaining newline character
		keyboard.nextLine();
		
		System.out.print("Enter the filename: ");
		filename = keyboard.nextLine();
		
		PrintWriter outputFile = new PrintWriter(filename);
		
		for(int i=1; i<=numFriends;i++){
			System.out.print("Enter the name of friend "+ "number " + i + ": ");
			friendName = keyboard.nextLine();
			outputFile.println(friendName);
		}
		
	outputFile.close();	
	System.out.println("Data written in file!");	
	}
}
