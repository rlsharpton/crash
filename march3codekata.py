def sumofNum(n):
    """Simple function to sum numbers from 1 to n """
    num = 1
    total = 0
    while num < (n + 1):        
        total = total + num
        print(f"total is: {total}")
        num += 1
        print(f"num is: {num}")

    return total


try:
    addTo = input("Please enter an integer to add up to: ")
    number = int(addTo)
except ValueError:
    print("You have not entered an integer")

print(f"the sum of {number} is {sumofNum(number)}")


    
