# Name: Abhishek Keri, NUID: 35718699
# Course: ISQA3900, Date: 09/26/2022


class Customer:
    """Customer class to read the customer detail"""
    def __init__(self, cust_num, fname, lname, company, street, city, state, zipcode):
        """initializing a customer object"""
        self.cust_id = cust_num
        self.first_name = fname
        self.last_name = lname
        self.company_name = company
        self.address = street
        self.city = city
        self.state = state
        self.zip = zipcode

    def cust_name(self):
        """returning full name with space in between"""
        return f'{self.first_name} {self.last_name}'

    def cust_fullAddress(self):
        """returning two line address if company attribute is empty, else three line address"""
        if self.company_name == "":
            return f'{self.address}\n{self.city}, {self.state}  {self.zip}'
        else:
            return f'{self.company_name}\n{self.address}\n{self.city}, {self.state} {self.zip}'

    def customer_id(self):
        """method that returns the value of customer id"""
        return self.cust_id

    def company_name(self):
        """method that returns the value of company name"""
        return self.company_name

    def __str__(self):
        """creating the string representation of the customer"""
        return {self.cust_name}+"\n"+{self.cust_fullAddress}
