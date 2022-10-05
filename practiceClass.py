'''Create two class definitions

1) a Play class that has attributes for
id, name, number of seats, date and status. Set the value of
the status attribute to True as default. Create an accessor
method each for the name, seats and status attributes only. 
Create a method called 'seats_left' that will reduce the 
number of seats by 1 every time it is called.
Create a mutator method called 'set_status' that will
change the status attribute to False.

2) a Booking class that has attributes for customer name and
seat number. Create accessor methods for both attributes.'''



class Play:

    def __init__(self, id, name, number_of_seats, date, status):
        self.__id = id
        self.__name = name 
        self.__numberofseats = number_of_seats
        self.__date = date
        self.__status = status

    def getName(self, name):
        self.__name = name
        return self.__name

    def getNumberofseats(self, number_of_seats):
        self.__numberofseats = number_of_seats
        return self.__numberofseats

    def getStatus(self, status):
        self.__status = status
        status = True
        return self.__status

    def seats_left(self, number_of_seats):
        self.__numberofseats = number_of_seats
        if number_of_seats == True:
            number_of_seats -= 1

    def set_status(self, status):
        self.__status = status
        status = False



class Booking:
    def __init__(self, customer_name, seat_number):
        self.__customer_name = customer_name
        self.__seat_number = seat_number

    def getCustomerName(self, customer_name):
        self.__customer_name = customer_name
        return self.__customer_name

    def getSeatNumber(self, seat_number):
        self.__seat_number = seat_number
        return self.__seat_number


