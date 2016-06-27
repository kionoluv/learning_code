//CODECADEMY: DATA STRUCTURES JAVA, ARRAYLIST & FOR EACH LOOPS

/*
 Code has notes with definitions of terms,
 remarks on things I noticed/learned,
 and notes on what my code did and what it means
*/

/*
	def ArrayList: list of data of specified type
	remark: ArrayList is pre-defined Jave class, to use must create an ArrayList object
	remark: an ArrayList type is Integer
*/
import java.util.ArrayList;

public class Temperature {

	public static void main (String[] args) {

		//note: created ArrayList objec named weeklyTemperature that stores Integer Data
		ArrayList<Integer> weeklyTemperatures = new ArrayList<Integer>();
		
		/*
		remark: add method adds integers to the ArrayList
		note: add method on weeklyTemperatures adds provided integers to ArrayList
		*/
		weeklyTemperatures.add(78);
		weeklyTemperatures.add(67);
		weeklyTemperatures.add(89);
		weeklyTemperatures.add(94);

		/*
		def index: an element's position in the list, refers to location within ArrayList
		remark: Java ArrayLists are 0-indexed so the starting position in 0
		remark: to access values, provide its index to the get method
		note: used get method to print out lowest temp contained in weeklyTemperatures
		note: index of lowest temp is at 1
		*/
		System.out.println(weeklyTemperatures.get(1) );

		/*
		remark: this variation of add method inserts temp at the third position (2) into list
		remark: all other elements in list will be shifted down one b/c of new insert*/
		weeklyTemperatures.add(2, 111);

		//note: uses get method to print out temp 89 which is now at index 3
		System.out.println(weeklyTemperatures.get(3) );

		/*
		remark: for loop breakdown of elements printed from an ArrayList
			1 Initialization: int variable j is set to 0
			2 Test Condition: code in block will run as long as j is less than size of weeklyTemperatures
			3 Increment: j will increment by 1 with j++ after each loop
		remark: size method returns int that'll represent how many total elements are stored within weeklyTemperatures
		def iteration: process of going through each element in ArrayList
		*/
		for (int j = 0; j < weeklyTemperatures.size(); j++) {

			System.out.println(weeklyTemperatures.get(j) );
		}

		/*
		def for each loop: Java shotcut to reduce amoutn fo written code to write loops
		remark: for each loops do not need a counter
		remark: colon(:) read as "in"
		note: for each Integer temperature in weeklyTemperatures, print out the value of temperature
		*/
		for (Integer temperature : weeklyTemperatures) {
			System.out.println(temperature);
		}

	}
}
