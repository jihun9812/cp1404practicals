"a"
for i in range(0, 101, 10):
    print(i, end=" ")

"b"
for i in range(20, 0, -1):
    print(i, end=" ")

"c"
star = "*"
stars_number = int(input("Enter the number of stars: "))
for i in range(stars_number):
    print(star, end="")

"d"
star = "*"
stars_number = int(input("Enter the number of stars: "))
for i in range(1, stars_number + 1):
    print(i * star)
