import numpy as np

# ------------------- NP arrays

list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]

# arr = np.array(list1)
# arr = np.array([list1,list2]) # creates a 2d array
arr = np.array([[list1, list2, list3],[list1,list2,list3]], dtype="int32") # creates a 3d array
#                 r1    r2     r3      

# print(arr.ndim) # tells us dim of array
# print(arr)

# print(arr)
# print(arr[1,:,0]) # 1 matrix, every row ka 1st col
# print(arr.shape)

#           -----------  np Array attributes

# print(f"shape {arr.shape}")
# print(f"size {arr.size}")
# print(f"Datatype {arr.dtype}")
# print(f"Dimension {arr.ndim}")

#           ----- HW create 1d and 3d array and guess its attributes

alpha = np.array([10,20,30,40.2])
charlie = np.array([[[11,22,33],[2,4,6]], [[0,0,0],[0,-3,-55]]])

# print(alpha, charlie, sep="\n")

# print(f"shape {alpha.shape}") #(4,) no. of col
# print(f"size {alpha.size}")   # 4
# print(f"Datatype {alpha.dtype}") # 64
# print(f"Dimension {alpha.ndim}") # 1

# print(f"shape {charlie.shape}") #(2,2,3) downs, rows, col
# print(f"size {charlie.size}") # 12
# print(f"Datatype {charlie.dtype}") # 64
# print(f"Dimension {charlie.ndim}") # 3

# zeros array
zero_arr = np.zeros((3,2,3)) # tell shape, rows, col/ depth, rows, 
# print(zero_arr)

# one erosarray
ones_arr = np.ones((3,2,3)) # tell shape, rows, col/ depth, rows, 
# print(ones_arr)

# full_array
full_arr = np.full((2,3),8) # fill arr of that shape with number 8
# print(full_arr)

# identity matrix, diagonal value ones 3,3 - square one
id_matrix = np.eye(3, dtype='int64')
# print(id_matrix)

# empty array
# print(np.empty(2)) # gives 2 garbage value, empty array


# arrange, evenly spaced
# print(np.arange(1,5,2)) #(1,5,2) print bw 1 to 5, and space bw of 2 numbers 5 is exc

# linespace - equally spaced values bw a range
# print(np.linspace(1,10,5))

# random value array - float
ran = np.random.rand(3,3) # pass a shaep
# print(ran)

# random value array - integer
ran_int = np.random.randint(1,5,(3,3)) # pass a shaep
# print(ran_int)


# Array indexing, and slicing
# arr = np.array([1,2,3,4,5,6])
# print(arr[1])
# print(arr[-3])
# print(arr[:]) # all cols
# print(arr[1:-1]) #[1,2,steps=]

# on 2d arrays

arr2 = np.array([[1,2,3],
                 [4,5,6]])
# print(arr2)
# print(arr2[:][0:3]) # every [] happens on row, chain reaction [:] return full 2d arr, [0:3] slice from full 2d array return rows   
# , to acheive row/col use [: , 1:2] comma
# print(arr2[: , 1:3])


arr3 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
# print(arr3)
# print(arr3[::2,0]) # every row, jump 2, col 0


# Array reshapening, and flattening
#       change, rows/col - convert higher dimensional array to 1D array

arr = np.array([1,2,3,4])
print(arr)

# print(arr.reshape(1,4))
# print(arr.reshape(2,2))
# print(arr.reshape(4,1))
# print(arr.reshape(3,2)) # gives error

reshaped = arr.reshape(4,1) # 4 rows 1 col
print(reshaped.flatten()) # again to 1D array

#           -------------- Stacking and splitting

a = [1,2,3]
b = [4,5,6]
print(np.vstack((a,b)))
# [1 2 3]
# [4 5 6]
print(np.hstack((a,b)))
# [1 2 3 4 5 6]