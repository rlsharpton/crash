def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " was not found."
        print(msg)
    else:
        # Count approximate number of words in file.
        words = contents.split()
        num_words = len(words)
        word_to_count = input("enter a word to count: ")
        common = words.count(word_to_count)
        print("The file " + filename + " has about " + str(num_words)
              + " words.")
        print("\nThere are " + str(common) + " occurances of the word " + word_to_count)

filenames = ['alice.txt', 'siddhart.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)


# value1 = 0
# while value1 != 'q':
#     value1 = input("\nPlease enter a number: ")
#     value2 = input("please enter the second number: ")
#     try:
#         sum_of_inputs = int(value1) + int(value2)
#     except ValueError:
#         print("Either " + value1 + " or " + value2
#               + " is not a number.")
#     else:
#         print("the sum of the values is: " + str(sum_of_inputs))

def count_words2(filename2):
    """My shot at the count words function"""
    try:
        with open(filename2) as f2_obj:
            contents2 = f2_obj.read()
    except FileNotFoundError:
        pass
    else:
        words2 = contents2.split()
        num_words2 = len(words2)
        print(filename2 + " has " + str(num_words2) + " words.")

count_words2('dogs.txt')

