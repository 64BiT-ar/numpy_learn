import numpy as np

# -------------- Level 1


A = [10, 20, 30, 40, 50]
B = [2, 4, 6, 8, 10]

a = np.array(A)
b = np.array(B)

# print(np.add(a,2))
# print(np.subtract(a,2))
# print(np.multiply(a,2))
# print(np.divide(a,2))
# print(np.square(a))
# print(np.power(a,3))

# Part 2

arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

# print(arr.ndim)
# print(arr.shape)
# print(arr.size)
# print(arr.dtype)
# print(arr.itemsize)

# Part 3

# print(arr[0,0])
# print(arr[1,2])
# print(arr[2,:])
# print(arr[:,1])
# print(arr[0][0:2])
# print(arr[1][1:3])

# Part 4

# zero_arr = np.zeros((5,5))
# print(zero_arr)
# ones_arr = np.ones((4,6))
# print(ones_arr)
# id_arr = np.eye(5)
# print(id_arr)

# print(np.arange(0,21)) #(1,5,2) print bw 1 to 5, and space bw of 2 numbers 5 is exc
# print(np.linspace(0,1,11))

# Part 5

arr = np.arange(1, 25)

# print(np.reshape(arr,(4,6)))
# print(np.reshape(arr,(6,4)))
# reshaped = np.reshape(arr,(6,4))
# print(np.reshape(arr,(2,3,4)))

# print(reshaped.flatten())


# ---------------------------------- Level 2

marks = np.array([72, 85, 91, 63, 77, 88, 95, 54, 69, 82])

# print(marks.mean())
# print(np.median(marks))
# print(marks.min())
# print(marks.max())
# print(marks.std())
# print(marks.var())
# print(marks.argmax())
# print(marks.argmin())
# print(marks[marks >= 80])


# Part 7

ages = np.array([17, 22, 19, 31, 25, 16, 28, 21, 15, 34])

# print(ages[ages >= 18])
# print(ages[(ages >= 18) & (ages <= 25)])
# print(ages[ages < 18])
# print(ages[ages >= 25])


# Part 8

temperatures = np.array([12, 25, 31, 18, 35, 9, 27, 40, 15])
temperatures[temperatures >= 30] = 30
temperatures[temperatures <= 15] = 15

# print(temperatures)


# Part 9

scores = np.array([55, 91, 73, 88, 62, 99, 70])

# print(scores.argsort())
# print(scores.sort())
# sorted_scores = np.sort(scores)  # Returns a brand new sorted array
# print(sorted_scores[-1:-4:-1])
# print(sorted_scores[0:3])


# Part 10

arr = np.random.randint(1,100, (5,5))
# print(arr)
# print(np.max(arr))
# print(np.min(arr))
# print(np.mean(arr))
# print(np.max(arr, axis = 1))
# print(np.max(arr, axis = 0))

# Part 11

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# print(np.sum(arr))
# print(np.sum(arr, axis=1))
# print(np.sum(arr, axis=0))

# print(np.mean(arr, axis=1))
# print(np.mean(arr, axis=0))


# Part 12

prices = np.array([
    [100, 200, 300],
    [150, 250, 350],
    [120, 220, 320]
])
tax = np.array([1.05, 1.10, 1.20], dtype='int64')

# print(prices * tax)


x = np.array([10, 20, 30, 40, 50])
normalized = (x - x.min()) / (x.max() - x.min())
x_min = np.min(x)
x_max = np.max(x)

# print(normalized)


x = np.array([10, 20, 30, 40, 50])
standardization = (x - x.mean()) / (x.std())

# print(standardization)
# print(np.mean(standardization))
# print(np.std(standardization))


# -------------------------------- Level 4

students = np.array([
    [80, 75, 90],
    [60, 55, 70],
    [95, 90, 92],
    [45, 50, 40],
    [70, 80, 75]
])
# Math, Python, AI
# Average score for each student
# Average score for each subject
# Best student
# Best student in each subject
# Students whose average ≥ 70
# Highest Math score
# Lowest AI score

# print(np.average(students, axis = 0))
# print(np.average(students, axis = 1))
# print(np.max(np.average(students, axis = 0)))
# print(np.max(np.average(students, axis = 1)))
# print(np.max(students, axis = 1))
# print(np.max(students[:, 1]))
# print(np.min(students[:, 2]))

# avg = np.average(students, axis = 0)
# print(avg[avg>=70])

x = np.array([
    [20, 50000],
    [25, 60000],
    [30, 80000],
    [35, 100000],
    [40, 120000]
])

x = (x - x.min(axis = 0)) / (x.max(axis = 0) - x.min(axis = 0))

# print(x)

weights = np.array([0.5, 0.3, 0.2])
features = np.array([80, 70, 90])

print(np.dot(weights,features))

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])
print(np.matmul(A, B))