guests = [ 'john', 'paul', 'george', 'ringo']
print("I am inviting {}".format(guests))
print("Oh, {} can not come so now {} are coming.".format(guests[0], guests[1:]))
guests = guests.append('bob')
print("I will invite {} instead".format(guests))