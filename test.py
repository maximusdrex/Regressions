n = int(input("degree"))
mat1 = []
for i in range(n+1):
    row = "Sum(" + "yi * (xi ^ (" + str(n - i) + ")" + ")"
    mat1.append(row)
print(mat1)
print(str(len(mat1)) )

mat2 = []
for i in range(n+1):
    row = []
    for j in range(n+1):
        term = "a" + str(j + 1) + " * Sum(" + "xi ^ (" + str((n - i) + (n - j)) + "))"
        row.append(term)
    mat2.append(row)

print(mat2)
print(str(len(mat2)) + " " + str(len(mat2[0])) )
