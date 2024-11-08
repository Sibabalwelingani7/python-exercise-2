# Question 1: Arithmetic and Assignment Operators

# TODO: Add 3 to x using the += operator
x=2
x+=3
print("x")
# TODO: Multiply y by 2 using the *= operator
y=2
x*=2
print("y")
# TODO: Divide x by y and store the result in a variable called 'result'
x = 2
results: x / y
print(result)

# TODO: Print the value of 'result'
print(results)
#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators

# TODO: Create a condition that checks if a is greater than b
a=10
b=5
if a>b:

# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
modulus = b%2
print(modulus==0)

# TODO: Create a condition that checks if c is less than or equal to a
a=10
c=3

    

# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a
final_condition = (a>b or b%2 and c<=0)

# TODO: Print the value of 'final_condition'
print(final_condition)

#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
score=input("please enter a test score (0-100):")
# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
     answer = 0
 if test_score >= 90 and test_score<101:
        print("A")
    elif test_score >= 80 and test_score <=89:
        print("B")
    elif test_score >= 70 and test_score<=79:
        print("C")
    elif test_score >= 60 and test_score<=69:
        print("D")
    else:
        print("F")

# TODO: Print the grade for the given score
    print(score)
#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1 = int(input("enter the first number(num1):"))
num2 = int(input("enter the second number(num1):"))
# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation = input("enter an operation (+,-,*,/): ")
# TODO: Use conditional statements to perform the chosen operation on num1 and num2
if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    if num2 == 0:
        print("Division by zero is not allowed.")
    else:
        print(num1/num2)
else:
    print("Error: Invalid operation.")
# TODO: Handle the case of division by zero

# TODO: Print the result of the operation
print(answer)