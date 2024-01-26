pyramid_scheme = int(input("insert number "))

for row in range(pyramid_scheme, 0, -1):
    for column in range(row):
        print("*", end=' ')
