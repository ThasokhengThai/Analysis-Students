import numpy as np
matrix2=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix2.shape)
print(matrix2[1,1]) 
print(matrix2[:,2]) 
print(matrix2[0,:])
print(matrix2[1:3,0:2]) 

import numpy as np
matrix3=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix3+matrix2)
print(matrix3-matrix2)
print(matrix3*matrix2)
print(matrix3/matrix2)

import numpy as np

# Define a square matrix
A = np.array([[1, 2],
              [3, 4]])


A_inv = np.linalg.inv(A)


print("Inverse of A:")
print(A_inv)

import numpy as np

# 3x3 identity matrix
I = np.eye(3)

print("Identity matrix:")
print(I)

#This is small playground related to data analysis created by using numpy library 
#System score for ITC student 
import numpy as np
scores = np.array([65, 70, 88, 90, 55, 76, 80, 95, 60, 72])

print("Scores:", scores)
print("Mean Score:", np.mean(scores))
print("Standard Deviation:", np.std(scores))
print("Median Score:", np.median(scores))
print("Maximum Score:", np.max(scores))
print("Minimum Score:", np.min(scores))
print("Variance:", np.var(scores))

import numpy as np
class Student:
    def __init__(self, name, GPA, subjects):
        self.name = name
        self.GPA = GPA
        self.subjects = subjects
    def info(self):
        print(f"Name: {self.name}")
        print(f"GPA: {self.GPA}")
        print(f"Subjects: {', '.join(self.subjects)}")

ronaldo = Student("Ronaldo", 3.5, ["Mechanics", "Chemistry", "Physics"])
messi   = Student("Messi",   3.8, ["Maths", "English", "Computer Science"])

ronaldo.info()
print()
messi.info()