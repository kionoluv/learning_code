//CODECADEMY: DATA STRUCTURES JAVA, HASHMAP

/*
 Code has definitions of terms,
 remarks on things I noticed/learned,
 and notes on what my code did and what it means
*/

/*
def HashMap: contains a set of keys and a value for each key
remark: providing the HashMap with a key that exists will bring the corresponding value associated with that key
remark: string object allows the storing of multiple characters such as wors in quotes
*/
import java.util.HashMap;

public class restaurant {
	public statis void main (String[] args) {

		/*
		note: created HashMap object called restaurantMenu
		note: restaurantMenu HashMap stores keys of String data types and values type Integer
		*/
		HashMap<String, Integer> restaurantMenu = new HashMap<String, Integer>();
		
		/*
		note: used put method to add String key and associated Integer value
		remark: String key is text in double-quotes " "
		remark: Integer is represented by the number
		*/
		restaurantMenu.put("Turkey Burger", 13);
		restaurantMenu.put("Naan Pizza", 11);
		restaurantMenu.put("Cranberry Kale Salad", 10);

		/*
		remark: accessing data in ArrayList needs index to be specified
		remark: accessing value in HashMap needs specified key
		note: get method on restaurantMenu HashMap using key "Naan Pizza"
		note: console prints value assocaited with "Naan Pizza" which is 11
		*/
		System.out.println(restaurantMenu.get("Naan Pizza") );

		// note: size method prints out size of restaurantMenu instance
		System.out.println(restaurantMenu.size() );

		// note: keySet method of HashMap returns a list of keys
		for (String item : restaurantMenu.keySet() ) {

			// note: accessing current keys item and restaurantMenu
			// note: console prints names and price of menu items
			System.out.println("A " + item + " costs " + restaurantMenu.get(item) + " collars.");
		}
	}
}
