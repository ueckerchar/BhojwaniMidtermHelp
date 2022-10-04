import practiceClassKEY as p
import csv
shows = {
    "play1":{
        'id':3245,
        'name':'Phantom of the Opera',
        'capacity':65,
        'event_date':'03/01/2023'
    },
    "play2":{
        'id':1548,
        'name':'The Music Man',
        'capacity':45,
        'event_date':'05/15/2023'
    },
    "play3":{
        'id':9587,
        'name':'Hamilton',
        'capacity':124,
        'event_date':'07/21/2023'
    },
    "play4":{
        'id':6254,
        'name':'The Lion King',
        'capacity':89,
        'event_date':'09/29/2023'
    },

}

'''using the above dictionary iterate through it and create an instance of the 
play class that has id 9587
NOTE: Do not hard code the values to create the instance but use
keys and values from the dictionary '''

for s in shows:
    showid = shows[s]['id']
    showname = shows[s]['name']
    capacity = shows[s]['capacity']
    date = shows[s]['event_date']

    if showid == 9587:
        show = p.Play(showid,showname,capacity,date)


'''using the bookings.csv file process only those 
reservations for the same play (9587) 
if the play reaches capacity print out a 
error message as shown in the picture'''


#open the csv file in read mode
bookingsfile = open('bookings.csv','r')

#create a csv object from the file object from the step above
bookings = csv.reader(bookingsfile,delimiter=',')
next(bookings)


#use a for loop to iterate through each record in the bookings file
for b in bookings:

    if int(b[0]) == 9587:
        if show.get_status():
            x = p.Booking(b[1],b[2])
            show.seats_left()
            if show.get_seats() == 0:
                show.set_status()
        else:
            print()
            print()
            print("**********ERROR*************")
            print("Guest Name:",b[1])
            print('Sorry, show:',show.get_name(),' is sold out')
            print("*****************************")
            print()
            print()
