#create analysis student score
import numpy as np

student = ["Jonh", "Paul", "Samuel", "Selena", "Ronaldo"]

student_score = [45, 80, 70, 95, 90]

scores = np.array(student_score) #numpy value

print(f"The highest scores is: {scores.max()}")
print(f"The lowest scores is: {scores.min()}")
print(f"The average scores is: {scores.mean()}")

name = np.array(student)
print(name)

passing_score = 50
passed = scores >= passing_score
print(passed)

passed_score = scores[scores >= passing_score]
print(f"Total passed score: {passed_score} ")