#Reverse word order of a string input by the user.

from audioop import reverse
#prompt user to input a string and assigns it to this variable "user_string"
user_string = input("Type a multi-word sentence and press return. I will reverse the order of the words!")
#splits string into separate items in a list
split_string = user_string.split()
#takes list of words and reverses the order
reverse_words = list(reversed(split_string))
#joins the words without commas in between
join_words = " ".join(reverse_words)
#output
print(f"Here is your sentence printed backwards: {join_words}")