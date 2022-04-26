"""Code #1 ↓"""
list1 = [
  "Another one bites the dust", #String
  (0, 5, 10, 15, 20, 25),       #Tuplet
  ["Blue", "Green", "Yellow"]   #List
]

table = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

#shows all of the collections in the list using for
for collection in list1:
  print(collection)

#shows every element in their collection using nested for
for collection in list1:
  for elements in collection:
    print(elements)
  print("\n")

#shows all the elements in list "table" using nested for
for row in table:
  for column in row:
    print(column, end = " ")
  print()

"""Code #2 ↓"""
matrix = [
  [-10, 63, 7],
  [54, -15, 13],
  [26, 41, 0],
]

#changes the matrix values to 1 if odd and to 0 if even
for i, row in enumerate(matrix):
  for j, column in enumerate(row):
    if matrix[i][j] % 2 == 0:
      matrix[i][j] = 0
    else:
      matrix[i][j] = 1

""" Result in matrix:
    [0, 1, 1]
    [0, 1, 1]
    [0, 1, 0]
"""
