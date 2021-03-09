list = [ "New York", "Los Angles", "Boston", "Denver" ]

print(list)     # prints all elements
print(list[0])  # print first element

list2 = [1,3,4,6,4,7,8,2,3]

print(sum(list2))
print(min(list2))
print(max(list2))
print(list2[0])
print(list2[-1])


"""The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True"""
#import time
#def sleep_in(weekday, vacation):
#   print(time())

#date_now = time()
#print(date_now)
#sleep_in()

from time import gmtime, strftime
#time_now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
time_now = strftime("%a")
print(time_now)
weekdays = ['Mon', ['Tue', 'Wed', 'Thur', 'Fri']]
for weekdays in time_now:
    if TRUE:
        print("its a weekday")
    else: 
        print("must be a weekend or its a mistake")