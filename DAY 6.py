rows = int(input("Enter the row number: "))
columns = int(input("Enter the column number: "))

matrix1 = []
matrix2 = []

sum = []
for i in range(rows):
    row = []
    for j in range(columns):
        value = int(input(f"Enter element at position [(i)(j)]:"))
        