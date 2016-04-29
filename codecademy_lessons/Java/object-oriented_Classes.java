//CODECADEMY: OBJECT-ORIENTED JAVA LESSON, CLASSES
/*
 Created a fully functioning class with definitions of terms,
 remarks on things I noticed/learned,
 and notes on what my code did and what it means
*/

/* def class: set of intructions that describe how data structure behaves
note: created class called Dog
*/
class Dog {
  
  /*
  def instance variable: specifies details for class to include
  remark: instance variable can be represented by a data type
  note: created instance of age using int data type
  */
  int age;
  
  /* 
  def class constructor: allows the creation of instances of the class
  remark: class constructors can set information about its corresponding class
  note: class constructor below is public Dog()

  def parameter: allows data types to be created with specific attributes
  note: added int parameter of dogsAge to Dog constructor
  remark: consrtuctor block is within the soft brackets following class construtor
  */
  public Dog(int dogsAge) {
    
    //note: in constructor block set instance variable age equal to dogsAge parameter
  	age = dogsAge;
    
  	}
  
  /*
  def method: pre-defined set of instructions that are declared within a class
  remark: method is located between constructor and main method
  note: method is called bark
  */
  public void bark() {
		
    /*
    note: system prints Woof!
    remark: print statement is within method block
    */
    System.out.println("Woof!");
    
	}
	
  /*
  remark: methods can be customized to accept parameters
  note: created method called run
  remark: parameters being add go between the parantheses following the method
  note: parameter for run is an int data type called feet
  */
  public void run(int feet) {
    
    //print statement includes the int parameter called feet
    System.out.println("Your dog ran " + feet + " feet!");

	}

  /*
  remark: there are different return types
  remark: void is a return type that says no value should be returned by method after it executes logic
  def void: keyword indicates to method that no return value is returned after calling that method
  remark: can use data types as keywords to specify that method should return value of that data type
  note: this method will return int data type
  */
  public int getAge() {

    /*
    note: specified that the return is age, which is an int data type
    note: age is set to equal dogsAge which has been previously established as int data type
    */
    return age;

  	}

  	/*
  	remark: public static void main(String[] args) { } is Java's built in main method
  	remark: code within main method is what is executed when Java runs program
  	remark: below is  main block
  	*/
	public static void main(String[] args) {
    
    /*
    note: Dog constructor creates Dog object named spike
    remark: spike's age is 5
    */
    Dog spike = new Dog(5);

    /*
    def calling: applying method to object
    note: calling bark to spike, hence spike is going to bark when program runs
    */
    spike.bark();

    /*
    note: calling run to spike
    remark: passed in int parameter of 15
    note: will print that spike ran 15 feet
    */
    spike.run(15);

    // note: set int variable spikeAge to value returned by calling getAge to spike
    int spikeAge = spike.getAge();

    System.out.println(spikeAge);

	}

}