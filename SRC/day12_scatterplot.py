#TASK 1: Correlation Checker

import matplotlib.pyplot as plt
study_hours=[1,2,3,4,5,6,7,8]
scores=[50,55,65,70,75,85,90,95]
plt.xlabel("Study Hours")
plt.ylabel("Scores")
plt.title("Scatter Plot")
plt.scatter(study_hours,scores)
plt.show()