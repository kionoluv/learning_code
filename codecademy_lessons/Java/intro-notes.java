//CODECADEMY: INTRO JAVA LESSON

/*
Summary: Data Types, Variables, White Sapce, Mathematics
*/

/*
 with definitions of terms,
 remarks on things I noticed/learned,
 and notes on what my code did and what it means
*/

/*
def int: data type that is short for integer
remark: all positive and negative and includes 0
remark: only allows values between -2,147,483,648 and 2,147,483,648
*/
public class DataTypes {
	public statis void main(String[] args) {

		System.out.println(7);

	}
}

/*
def boolean: data type that can only be true or false
*/
public class DataTypesB {
	public static void main(String[] args) {

		System.out.println(true);

	}
}

/*
def char: data type used to represent a single character
remark: all char values must be enclosed in single quote (' ')
*/
public class DataTypesC {
	public static void main (String[] args) {

		System.out.println('C');

	}
}

/*
def variable: ability to store a value
remark: in java all variables must have specified data type
*/
public class Variables {
	pulic static void main(String[] args) {

		//remark: semicolon is used to end all single code statements
		int myNumber = 23;
		boolean isFun = true;
		char movieRating = 'B';

	}
}

/*
def whitespace: one or more characters that don't produce a vible mark/text
remark: examples of whitespace are spaces, tabs, enter/return
remark: using whitespace helps make code easier to read
*/
public class WhiteSpace {
	public static void main(String[] args) {
		boolean isFormatted = false;
		System.out.println(isFormatted);
	}
}

//versus the same code with proper whitespace
public class WhiteSpace {
	public static void main(String[] args) {
		
		boolean isFormatted = false;
		System.out.println(isFormatted);

	}
}

//remark: this is a single-line comment

/*
remark: this is a multi-line comment
*/

/*
remark: can do math in java such as add, subtract, multiply, and divide 
note: example of math operations
*/
public class Arithmatic {
	public static void main(String[] args) {

		int sum = 2 + 3;
		int difference = 10 - 4;
		int product = 5 * 6;
		int quotient = 16 / 8;

		int myNumber = 123 * 45;
		System.out.println(myNumber);

	}
}

/*
def modulo % : returns the remainder of diving two numbers
remark: it's like using dividing but instead of using / you can use %
*/
public class Modulo {
	public static void main(String[] args) {

		int myRemainder = 7 %
	}
}

/*
def relational operators: compare data types that hve defined ordering
remark: ROs will always return boolean value of true/false
remark: examples of relational operations
	< less than
	<= less than equal to
	> greater than
	>= greater than equal to
def operands: terms being compared using the relational operators
*/
public class RelationalOperators {
	public static void main(String[] args) {

		//2 and 1 are the operands & console will print true
		System.out.println(2 > 1);
	}
}

/*
def equality operators: used to test equality
	== equal to
	!= not equal to
remark: EOs don't require that operands share the same ordering
remark: can test equality acccross boolean, char, int data types
*/
public class EqualityOperators {
	public static void main(String[] args) {

		//note: will print false
		System.out.println(true == false);

		char myChar = 'C'
		int myInt = 3;
		//note: will print false because values do not equal
		System.out.println(myChar == myInt);
	}
}