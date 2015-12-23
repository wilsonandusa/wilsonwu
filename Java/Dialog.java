import javax.swing.JOptionPane;

// /*This program demonstrate using dialogs with JOptionPane
// by Xiaosheng Wu  12/23/2015

public class Dialog{
	public static void main(String[] args) {
		String inputString;
		String name;
		int hours;
		double payRate;
		double grossPay;
		
		//get user's name
		
		name = JOptionPane.showInputDialog("What is your name?");
		
		inputString = JOptionPane.showInputDialog("How many hours did"
		+" you work toady");
		
		//convert the input to an int
		hours = Integer.parseInt(inputString);
		
		//get the hourly pay rate
		inputString = JOptionPane.showInputDialog("What is your"+
		"hourly pay rate?");
		
		payRate = Double.parseDouble(inputString);
		
		grossPay = hours*payRate;
		
		JOptionPane.showMessageDialog(null, "Hello "+name+". Your gross pay is $"+grossPay);
		
		System.exit(0);
	
	}
}
 
