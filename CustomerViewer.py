# Name: Abhishek Keri, NUID: 35718699
# Course: ISQA3900, Date: 09/26/2022

import csv
from customer import Customer
from CustomerDB import read_customers
import sys

FILENAME = "customers-1.csv"


def create_customer():
    """creating a customer object from Customer list that is returned from CustomerDB file"""
    customer_list = read_customers()
    customer_object = []
    for i, customers in enumerate(customer_list, start=1):
        customer_object.append(Customer(cust_num=customers[0],
                                        fname=customers[1],
                                        lname=customers[2],
                                        company=customers[3],
                                        street=customers[4],
                                        city=customers[5],
                                        state=customers[6],
                                        zipcode=customers[7]))

    return customer_object


def list_customers():
    """Printing list of all customers and their IDs"""
    print("CUSTOMER VIEWER")
    print("\nALL CUSTOMERS")
    customer_list = create_customer()
    """Iterating through elements from the customer list"""
    for i in customer_list:
        print(f"{i.customer_id()}: {i.cust_name()}")


def search_customers():
    """Creating a function that searches for a customer ID and returns the value according to the search value"""
    while True:
        try:
            id = input("\nEnter Customer ID: ")
        except ValueError:
            return f"Customer {id} does not exist"
        else:
            customer_list = create_customer()
            """Iterating through elements from the customer list"""
            for i in customer_list:
                if id == i.cust_id:
                    return f"{i.cust_name()}\n{i.cust_fullAddress()}"
            return f"Customer {id} does not exist"


def exit_program():
    """Exit function that can be used when csv file is not read"""
    print("Terminating program.")
    sys.exit()


def main():
    """calling functions 1 and 2 if csv file exist or else exiting the function"""
    while True:
        try:
            create_customer()
            list_customers()
            break
        except FileNotFoundError as e:
            print(f"Could not find {FILENAME} file.")
            exit_program()
        except Exception as e:
            print(type(e), e)
            exit_program()
    """Calling the search function and keeping the continue/no option that loops through or breaks"""
    while True:
        returned_value = search_customers()
        print(returned_value)
        userChoice = input("Would you like to continue (y/n): ").lower()
        if userChoice == 'y':
            continue
        elif userChoice == 'n':
            break
        else:
            print("Enter a valid choice: y/n")


"""Calling the main function"""
main()
