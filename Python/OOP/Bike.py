class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self): #have this method display the bike's price, maximum speed, and the total miles.
        print "The price for this bike is "+ self.price
        print "The maximum speed for this bike is "+ self.max_speed
        print "The total miles of the bike is ", (self.miles)

    def ride(self): #have it display "Riding" on the screen and increase the total miles ridden by 10
        print 'Riding'
        self.miles += 10

    def reverse(self): # have it display "Reversing" on the screen and decrease the total miles ridden by 5...
        print 'Reversing'
        self.miles -= 5


#Have the first instance ride three times, reverse once and have it displayInfo(). 
bike1 = Bike("200", "25mph")
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

#Have the second instance ride twice, reverse twice and have it displayInfo().  
bike2 = Bike("200", "25mph")
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

# Have the third instance reverse three times and displayInfo().
bike3 = Bike("200", "25mph")
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()