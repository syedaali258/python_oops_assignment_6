class Countdown:
    def __init__(self, start):
        self.start = start  #set the starting number
        self.current = start  #initialize current to the starting number 

    def __iter__(self):
       # return the iterator object itself
       return self
    def next(self):
        #if current is less than 0 stop the iteration
        if self.current < 0:
            raise StopIteration
        #decrease current by 1 and return the value
        self.current -= 1
        return self.current  + 1

#creaTING AN OBJECT OF COUNTDOWN
countdown = Countdown(5)

#using the countdown object in a for loop
for number in countdown:
    print(number)

