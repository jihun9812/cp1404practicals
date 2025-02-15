
name = input("Enter your name: ")

file = open("name.txt", "w")
file.write(name)
file.close()

file = open("name.txt", "r")
name = file.read().strip()
file.close()


print(f"Hi {name}!")



with open("numbers.txt",'r') as file:
    line1 = int(file.readline().strip())
    line2 = int(file.readline().strip())

    if line1 and line2:
        number1 = int(line1)
        number2 = int(line2)

        result = number1 + number2
        print(f'Sum of the first two numbers is {result}.')

    else:
         print("Error: 'numbers.txt' does not contain enough valid numbers.")

with open("numbers.txt",'r') as file:
    total = 0
    for line in file:
        line = line.strip()
        if line:
             total += int(line)

    print(f'The total of all numbers is: {total}')


