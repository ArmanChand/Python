# Get user input for their name
name = input("what is your name? ")

# Print a greeting message with the user's name (Single input)
print('hello , ' + name)

# Print a greeting message with the user's name using a comma and a space as separators (Multiple Input)
print('hello ,' , name)

# Print a greeting message with the user's name without a separator and without a newline character
print('hello, ', end='', sep='')
print(name)





# Printing a string with single quotes and double quotes
print(' hello, "friend" ')
print(" hello \"friend\"")




# Using f-string to print a variable inside a string
print(f"hello, {name}")





# Get user input for their last name
name = input("what is your last name? ")

# Strip any leading/trailing whitespace from the name
name = name.strip()

# Capitalize the first letter of the name
name = name.capitalize()

# Convert the first letter of every word in the name to uppercase
name = name.title()

# Print a personalized greeting message using the formatted string
print(f"hello, {name}")

# A more concise version of the code above, using method chaining to perform
# the same operations in a single line of code
name = input("what is your full name? ").strip().title()
print(f"hello, {name}")
