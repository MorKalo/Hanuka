import sqlite3
from Customer import Customer
from CustomerDataAccess import CustomerDataAccess


dao = CustomerDataAccess('C:\MorPython\pythonProject\Hanuka\hanukasql.db')
def manu():
    print()
    print('***MANU of this program***')
    print('[1] Get all customers')
    print('[2] Get customer by id')
    print('[3] Insert customer')
    print('[4] Delete customer')
    print('[5] Update customer')
    print('[6] Exit')
    choice_option()

def choice_option():
    option=int(input('Enter your option: '))
    if option==1:
        dao.get_all_customers()
        another_choice()
    elif option==2:
            id=int(input('Enter the id of the customer you want to get: '))
            print(dao.get_customer_by_id(id))
            another_choice()
    elif option==3:
        new_customer=Customer(input('plz enter the customer details: id, last name, first name, address, mobile number'))
        dao.insert_customer(new_customer)
        another_choice()
    elif option==4:
        id = int(input('Enter the id of the customer you want to DELETE: '))
        dao.delete_customer(id)
        another_choice()
    elif option==5:
        uid=int(input('Enter the id of the customer you want to UPDATE:'))
        uaddress=str(input('Enter the NEW ADRESS:'))
        dao.update_customer(uid, uaddress)
        another_choice()
    elif option==6:
        print('thank u, GOOD BYE')


def another_choice():
    print('do you want to do another choice? ')
    print('[Y] YES')
    print('[N] NO')
    yn =input('Enter your choice: ')
    if yn=='Y' or yn=='y':
        manu()
    else:
        print('thank u, GOOD BYE')

manu()
print()



