import random

aliens = []
colors = ['green', 'yellow', 'red']
points = [5, 10, 15]
speed = ['slow', 'medium', 'fast']

for i in range(30):
    idx = random.randint(0, 2)

    colour = colors[idx]
    print("the index is: {} The colour is: {}".format(idx, colour))
    if colour == 'green':
        point_val = 5
        speed_val = speed[0]
    elif colour == 'yellow':
        point_val = 10
        speed_val = speed[1]
    else:
        point_val = 15
        speed_val = speed[2]

    new_alien = {'color': colour, 'points': point_val, 'speed': speed_val}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print("...")

print("total aliens " + str(len(aliens)))