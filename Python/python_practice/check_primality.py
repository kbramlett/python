#check primality function

#creates flag variable; will remain True until a user input is not prime
prime = True
#function signature with default argument in help_text.
def check_primality(help_text = "Input a number to check if it is prime: "):
  return int(input(help_text))

#Create a variable to hold each user input. The first prints the default argument "help text". The second and third calls of the function print the specified help text.
rand_input = check_primality()
user_input = check_primality("Input your favorite number: ")
input_again = check_primality("Input your least favorite number: ")

#the conditional statements that check if each input is prime or not
if user_input > 1:
      #loop to look for divisors in current range
  for i in range(2, user_input):
        #checks to see if input is divisible by any numbers in current range
    if(user_input % i) == 0:
      prime = False
      print(f"{user_input} is not a prime number.")
      break
    elif(user_input % i) > 0:
      prime = True
      print(f"{user_input} is a prime number.")
      break

if input_again > 1:
      #loop to look for divisors in current range
  for i in range(2, input_again):
        #checks to see if input is divisible by any numbers in current range
    if(input_again % i) == 0:
      prime = False
      print(f"{input_again} is not a prime number.")
      break
    elif(input_again % i) > 0:
      prime = True
      print(f"{input_again} is a prime number.")
      break

if rand_input > 1:
      #loop to look for divisors in current range
  for i in range(2, rand_input):
        #checks to see if input is divisible by any numbers in current range
    if(rand_input % i) == 0:
      prime = False
      print(f"{rand_input} is not a prime number.")
      break
    elif(rand_input % i) > 0:
      prime = True
      print(f"{rand_input} is a prime number.")
      break
