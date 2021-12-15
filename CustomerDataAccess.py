import sqlite3
from Customer import Customer

con = sqlite3.connect('C:\MorPython\pythonProject\Hanuka\hanukasql.db')

class CustomerDataAccess():

    def __init__(self, file_path):
        self.cursor = sqlite3.connect(file_path).cursor()


    def print_customers(self):
        self.cursor.execute("select * from CUSTOMER")
        for row in self.cursor:
           print(row)


    def insert_customer(self, customer):
        self.cursor.execute(f'INSERT INTO CUSTOMER VALUES ({customer.id}, "{customer.fname}", "{customer.lname}",'+
                            f' "{customer.address}", "{customer.mobile}")')
        con.commit();


    def delete_customer(self, id):
        self.cursor.execute(f'DELETE FROM CUSTOMER where id ={id}')
        con.commit();


    def get_all_customers(self):
        _lst1 = []
        for row in self.cursor:
            print(row)
            _lst1.append(Customer(row[0], row[1], row[2], row[3], row[4]))
        print(_lst1)
        con.commit();


    def get_customer_by_id(self, id):
        self.cursor.execute(f'select * from Customer where id = {id}')
        customer = None
        for row in self.cursor:
            customer = Customer(row[0], row[1], row[2], row[3], row[4])
        return customer
        con.commit();

    def update_customer(self, id, address):
        self.cursor.execute(f'UPDATE Customer SET address="{address}" where id ={id}')
        con.commit();
