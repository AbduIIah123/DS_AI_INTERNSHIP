#TASK 1

import matplotlib.pyplot as plt
print("LINE PLOT")
months=[1,2,3,4,5] 
revenue=[2000,4500,4000,7500,9000]
plt.title("Monthly Revenue Growth")
plt.xlabel("Month")
plt.ylabel("Revenue in USD")
plt.plot(months,revenue)
plt.show()
