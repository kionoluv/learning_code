//CODECADEMY: OBJECT-ORIENTED JAVA LESSON, INHERITANCE
/*
 Created a fully functioning class with definitions of terms,
 remarks on things I noticed/learned,
 and notes on what my code did and what it means.
*/

 // This is supposed to run in conjuction with the Animal_inherit file
 
/*
 def inheritance: object-oriented concept that allows the reuse and maintainence of code more efficiently,
                  used to share/inherit behavior from another class.
 keyword extends: used to indicate that a class inherits the behavior defined in another class 
*/

class Dog extends Animal_inherit {
  
  int age;
  
  public Dog(int dogsAge) {
    
    age = dogsAge;
    
  }
  
  public void bark() {
		
    System.out.println("Woof!");
    
	}
	
  public void run(int feet) {
    
    System.out.println("Your dog ran " + feet + " feet!");

	}

  public int getAge() {

    return age;

  }

	public static void main(String[] args) {
    
    Dog spike = new Dog(5);

    spike.bark();

    spike.run(15);

    System.out.println(spikeAge);

    /*
    note: calls checkStatus from Animal_inherit on spike object
    remark: spike inherits the behavior of Anime_inherit by calling checkStatus to it
    */
    spike.checkStatus();

	}

}