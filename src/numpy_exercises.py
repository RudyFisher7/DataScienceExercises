import numpy as np


# Matrix math.
print('Matrix Math')

# Adding 1D vectors together:
# [1, 2, 3, 4] + [5, 6, 7, 8] = [1+5, 2+6, 3+7, 4+8] = [6, 8, 10, 12]
# It's the same process for subtractions, multiplication, and division: it is element-wise.
x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 8])
print(x + y)


# Adding a scalar to a 1D vector:
# [1, 2, 3, 4] + 3 = [4, 5, 6, 7]
# It's the same process for subtractions, multiplication, and division: add the scalar to each element.
print(x + 3)

# Getting the dot product of matrices (2D vectors):
# The dimensions are: 4x2 x 2x4 = 4x4
# [[1,2], [3,4], [4,5], [6,7]] x [[6,7,8,9], [3,4,5,6]] = 
# [
#   [(1*6)+(2*3), (1*7)+(2*4), (1*8)+(2*5), (1*9)+(2*6)],
#   [(3*6)+(4*3), (3*7)+(4*4), (3*8)+(4*5), (3*9)+(4*6)],
#   [(4*6)+(5*3), (4*7)+(5*4), (4*8)+(5*5), (4*9)+(5*6)],
#   [(6*6)+(7*3), (6*7)+(7*4), (6*8)+(7*5), (6*9)+(7*6)],
# ]
# = [[12,15,18,21], [30,37,44,51], [39,48,57,66], [57,70,83,96]]

x1 = np.array([[1, 2], [3, 4], [4, 5], [6, 7]])
y1 = np.array([[6, 7, 8, 9], [3, 4, 5, 6]])
print(np.dot(x1, y1))


# The dimensions are: 2x4 x 4x2 = 2x2
# [[6,7,8,9], [3,4,5,6]] x [[1,2], [3,4], [4,5], [6,7]] = 
# [
#   [(6*1)+(7*3)+(8*4)+(9*6), (6*2)+(7*4)+(8*5)+(9*7)],
#   [(3*1)+(4*3)+(5*4)+(6*6), (3*2)+(4*4)+(5*5)+(6*7)],
# ]
# = [[113, 143], [71, 89]]
print(np.dot(y1, x1))


# Some NumPy functions.
print('Some NumPy Functions')

x2 = np.arange(12).reshape(3, -1)
print(x2)

x3 = np.arange(16).reshape(-1, 4) # Automatically calculates the number of rows needed to produce the number of columns.
print(x3)


# Slicing.
# NOTE:: Unlike Python lists, NumPy arrays return views of original array when slicing, not a copy.
print('Slicing')
x4 = x2[:2] # First 2 elements (rows).
print(x4)

x5 = x2[1:3, -2:] # Last 2 columns of rows [1, 3).
print(x5)

# Indexing.
# NOTE:: Indexing returns a copy.
print('Indexing')
x6 = x2 % 2 == 0 # Returns a boolean array (True at indexes where elements are even.).
print(x6)

x7 = x2[x6] # Can use the boolean array for indexing.
print(x7)

x8 = x2[x2 % 2 != 0] # Select all the odd elements.
print(x8)


print('Fancy Indexing')
x9 = np.zeros((8, 4), dtype=np.int64)
for i in range(len(x9)):
    x9[i] = i # Assigns all elements in the row to i.

print(x9)

print(x9[[5, 2, 4]]) # Selects the elements at these indexes, in the order they appear in the index array.

print(x9[[-3, -5, -1, 1]])

x10 = np.arange(32).reshape((-1, 4)) 

print(x10)

print(x10[[2, 3, 4, 5], [0, 1, 2, 3]]) # Selects elements on the diagonal starting at index [2, 0] and ending at [5, 3].
print(x10[[2, 3, 4, 5], [0, 3, 2, 1]])

x11 = x10[[2, 3, 4, 5]]
print(np.shares_memory(x10, x11)) # Can be used to check if x10 is a view or a copy from x11.
print(x11)

# Still returns a copy instead of a view.
print(x11[:, [0, 3, 2, 1]]) # This selects the rectangular area in the 2D array, then rearranges elements to match the index array order.


print('Transposing and Swapping Axes')
x12 = np.arange(15).reshape((3, -1))
print(x12)
print(x12.T) # If rows are the samples (typical for a data table), this makes the features the rows.
print(x12.swapaxes(0, 1)) # General function for swapping axes.


print('Conditional Logic as Arrays')
asc = np.arange(16)
desc = np.flip(asc)
print(asc)
print(desc)
print(np.shares_memory(asc, desc))

cond = asc % 3 == 0
print(cond)
whered = np.where(cond, asc, desc) # Selects asc[i] if cond[i] else desc[i] as a new array.
print(whered)
print(np.shares_memory(whered, asc))


print('Statistical Methods and More Math')
x13 = np.random.standard_normal((5, 4))
print(x13)
print(x13.mean())
print('Sums:')
print(x13.sum(axis=0))
print(x13.sum(axis=1))
print('Cumsums:')
print(x13.cumsum(axis=0))
print(x13.cumsum(axis=1))