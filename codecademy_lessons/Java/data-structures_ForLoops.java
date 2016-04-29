//CODECADEMY: DATA STRUCTURES JAVA, FOR LOOPS

/*
 Code has notes with definitions of terms,
 remarks on things I noticed/learned,
 and notes on what my code did and what it means
*/

 /*
	def control statements: runs a task repeatedly
	def for loop: a control statement that runs a block of code until a specified condition is met
 */

public class For {
	public static void main(String[] args) {

		/*
			remarks: the statements within the for loop is composed of
				1 Initialiation: int variable named waterLevel is initialized to value of 0 before loop runs
				2 Test Condition: boolean expression waterLevel < 7 is conditional statement that is evaluated before code in control statement
					if expression in true, code within block will run, if expression is false for loop stops running
				3 Increment: each time the loop completes, increment statement is run
					waterLevel++ increases waterLevel by 1 after each loop
			remarks: code continues to execute until the boolean expression is false
		*/
		for (int waterLevel = 0; waterLevel < 7; waterLevel++) {

			System.out.println("The pool's water level is at " + waterLevel + " feet.");

		}
	}
}