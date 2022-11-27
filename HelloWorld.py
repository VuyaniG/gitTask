def reverse(item):
  '''
  Function to reverse string'''
  rev = item[::-1]
  return rev

print("Hello World! Welcome to string manipulation!")
choice = ''
# program requests user to choose to input a new string to reverse or quit
while choice != 'quit':
   print('Enter (R) to reverse and print your inputted string\nEnter (QUIT) to quit') 
   choice = input("Enter choice: ").lower()
   if choice == 'r':
      slice = input("enter something: ").lower()
      print(reverse(slice))
   else:
      pass   

    
