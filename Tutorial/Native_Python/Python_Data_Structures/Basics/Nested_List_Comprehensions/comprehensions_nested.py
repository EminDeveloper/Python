matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print([[row[i] for row in matrix] for i in range(4)])

print("#########################################")

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)
print("#########################################")

transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)
print("#########################################")

print(list(zip(*matrix)))
print("#########################################")

