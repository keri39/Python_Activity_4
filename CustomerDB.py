# Name: Abhishek Keri, NUID: 35718699
# Course: ISQA3900, Date: 09/26/2022

import csv
"""importing csv and giving that value to a variable"""
FILENAME = "customers-1.csv"


def read_customers():
    """creating a customers list from csv and returning that list"""
    customers = []
    with open(FILENAME) as f:
        next(f)
        reader = csv.reader(f)
        for line in reader:
            customers.append(line)
        return customers
