Rows = int(input("Enter row number: "))
Columns = int(input("Enter column number: "))

matrix = []

for i in range(Rows):
    Rows = []
    for j in range(Columns):
        Value = int(input("Enter the value for (i),(j): "))
        Rows.append(Value)
    matrix.append(Rows)

print("matrix: ")
for r in matrix:
    print(r)


# printing lower triangle
# rows = int(input("Number of rows : "))
# cols = int(input("Number of cols : "))
# matrix = [[int(input(f"Enter value at [{r}][{c}] : ")) for c in range(cols)] for r in range(rows)]
# print("Original Matrix : ")
# for r in range(rows):
#     for c in range(cols):
#         print(matrix[r][c], end=" ")
#     print()
# print("Printing Lower Corner : ")
# for r in range(rows):
#     for c in range(r):
#         print(matrix[r][c], end=" ")
# print()

# printing diagonal elements
for i in range(Rows):
    for j in range(Columns):
        if i == j:
            print(matrix[i][j], end = " ")
        print()

