# This is a part of assignment from the University of Nebraska at Omaha for the course Web Application Development
Objectives:

Develop an object-oriented python program consisting of multiple Python files that reads information from a file in a Python list of Objects and allows a user to find a value in the list.
This assignment provides an introduction and/or review of the following Python features, including:
1) Reading data from a csv file
2) Handling file exceptions if a file is not found or reading data fails
3) Storing data in a Python list
4) Defining multiple Python files for a single program
5) Defining and using Python Classes and Objects
6) Utilizing good programming practice, including the following features: Descriptive variable and function names

Example program execution in the console window:

<img width="1269" alt="Screen Shot 2022-09-27 at 5 41 12 PM" src="https://user-images.githubusercontent.com/111935093/192650314-688b63bf-eb40-48f1-b6a6-84b78c6d01e6.png">

<img width="929" alt="Screen Shot 2022-09-27 at 5 42 59 PM" src="https://user-images.githubusercontent.com/111935093/192650468-ba1f64a6-fbaf-4352-84c3-4f8d3c62752a.png">

Python file 1: Customer.py

Create a Python file that defines a Customer class to store a customer’s data as defined in the UML class diagram below.

<img width="830" alt="Screen Shot 2022-09-27 at 5 44 00 PM" src="https://user-images.githubusercontent.com/111935093/192650589-0603524e-81f0-4b49-91cc-3a1593f8b19e.png">

Methods and Properties:
1. Define the __init__ method to initialize a Customer object using values passed as parameters. You do not need to perform data validation.
2. Define the __str__ method to create a String representation of the Customer. The format of the String should be identical to the output shown in the example program run above.
a. This method should use the cust_name(self) and cust_fullAddress(self) properties/methods as defined below.
3. Define a property or method cust_name(self) that returns the full name in the format shown in the example program run above with one space between the first and last names.
4. Define a property or method cust_fullAddress(self) that returns the full address.
a. The address should have two lines if the company attribute is empty or three lines if the company
attribute is not empty.
5. Create a property or method to return the value of the customer ID.
6. Create a property or method to return the value of the company name. Note that this property/method is not called in the CustomerViewer.py file but is provided for completeness.

Python File #2: CustomerViewer.py

Create a second Python file that implements the following:
1. A function to read the customer data from a CSV file and create a list of Customer objects using the data from the file. Optionally, this method may be created in a separate CustomerDB.py file. Be sure to import CustomerDB in CustomerViewer.py if you place this method in the CustomerDB.py file.
 
 a. The first line of the file contains column headings and should be read by your program but not saved in a Customer object. It should be ignored.
 
 b. If the file does not open or the records are not read successfully, raise an exception.
 
 c. A copy of the data file with the customer information is posted with this assignment on Canvas.
2. A function to display the customer ID and name of each customer (one per line).
3. A function to find a customer with a specified customer number. You will need to search through each Customer object in the list of Customer objects and check whether the specified ID matches the ID stored in the Customer object.
  
  a. Return the customer object if the customer is found.
  
  b. Return None if the customer is not found. Reminder: None is a reserved word and should not be in
    quotations when returned. It should also be capitalized as shown here.
4. A main function to perform the following actions:
  
  a. Call the function from step ‘1’ above to read the customer information from the file into a list of
     Customer objects.
  
  i. If the file does not open and the records are not read successfully, display an error message
  and end the program.
  
  b. Call the function from step ‘2’ above to display the customers’ IDs and names – 1 per line.
  
  c. Create a repetition structure to prompt the user for a customer number and attempt to lookup the
    customer using the find method created in step ‘3’ above. This may also be in a function if desired.

  i. If the customer is not found, display an error message.

  ii. If the customer is found, display the customer data as shown in the sample program execution provided.
  
  iii. If the user enters invalid values for the customer number, display an error message and allow the customer to enter a new customer number.
  
  iv. The user should be allowed to continue looking up customers until they choose to end the program.
