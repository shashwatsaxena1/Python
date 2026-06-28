Num1 = int(input("Enter the first number: "))
Num2 = int(input("Enter the second number: "))
Op = int(input('''select the operation you want to perform:
1. Sum
2. Difference
3. Product
4. Division
Type you option number: '''))
if Op == 1:
    print("Sum of", Num1, "and", Num2, "is", Num1 + Num2)
elif Op == 2:
    print("Difference of", Num1, "and", Num2, "is", Num1 - Num2)
elif Op == 3:
    print("Product of", Num1, "and", Num2, "is", Num1 * Num2)
elif Op == 4:
    print("Division of", Num1, "and", Num2, "is", Num1 / Num2)
else:
    print("You entered an invalid operation.")
