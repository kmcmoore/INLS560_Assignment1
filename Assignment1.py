# Assignment: Exploring Strings and Basic Operations in Python

## Tasks:

### 1. String Quoting:

string_single = 'I said, "UNC is superior to Duke."'
print(string_single)

string_double = "My favorite quote from Harry potter is, 'Happiness can be found even in the darkest of times if only one remembers to turn on the light' "
print(string_double)

string_triple = '''The UNC fencing team is very dedicated to their team culture. Specifically, they has 3 specific values:
Dedication
Responsibility
Determination'''
print(string_triple)

### 2. String Escaping:

string_escaped = 'There\'s many basketball players on the UNC team.'
print(string_escaped)

### 3. Type Conversion and Casting:
num_string = 5.7
num_int = int(num_string)
print(num_string)
print(num_int)

### 4. Input and Concatenation:
input_first_name = input("Enter first name: ")
input_last_name = input("Enter last name: ")
full_name = input_first_name + ' ' + input_last_name
print("Full name is ", full_name)

### 5. Using f-strings:
word_one = "foil" 
word_two = "fencing"
combo_sentence = f"I fence {word_one} on the UNC {word_two} team."
print(combo_sentence)

### 6. Math:
num_one = int(input("Enter first number: "))        
num_two = int(input("Enter second number: "))
num_three = int(input("Enter third number: "))
math_calculations = (num_one * num_two)**2 - num_three
print("The math calculation is: ", math_calculations)

### 7. Currency Formatting
num_one = float(input("Enter first number: "))        
num_two = float(input("Enter second number: "))
num_three = float(input("Enter third number: "))
math_calculations = (num_one * num_two)**2 - num_three
print(f"The math calculation (currency): ${math_calculations:,.2f}")

### 8. Demo the end parameter
print('Some text and')
print('some other text.')
print('Some text and', end=' ')
print('some other text.')

### 9. Demo the sep parameter
print('01', '29', '2024', sep = '-')