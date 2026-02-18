#Task 1: The Sample Space Map (Fundamentals)
ss1 = [["Click","Click"],["Click","Scroll"],["Click","Exit"],
      ["Scroll","Click"],["Scroll","Scroll"],["Scroll","Exit"]]
n=len(ss1)
x=0
for i in ss1:
    for j in i:
        if j == "Click":
            x=x+1
            break
print("Probability that customer clicks atleast once = ",x/n)


ss2 = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],
       [2,1],[2,2],[2,3],[2,4],[2,5],[2,6],
       [3,1],[3,2],[3,3],[3,4],[3,5],[3,6],
       [4,1],[4,2],[4,3],[4,4],[4,5],[4,6],
       [5,1],[5,2],[5,3],[5,4],[5,5],[5,6],
       [6,1],[6,2],[6,3],[6,4],[6,5],[6,6],
       ]
n2=len(ss2)
sum=0
            
for l in ss2:
    if l[0]+l[1] == 7:
        sum+=1
print("Probability of getting sum as 7 in 2 dice  = ",sum/n2)


#Task 2: The Logic of Dependency (Independent vs. Dependent)
p_head = 0.5
p_six = 1/6
p_both = p_head * p_six
print("probabilty of getting a head on a coin AND a six on a die = ",p_both)

nr = 5
nb = 5
p_red = nr/(nr+nb)
p_blue = nb/(nr+nb)
p_redred = p_red * (nr-1)/(nr+nb-1)
print("Probabilty of getting red twice without replacement = ",p_redred)



#Task 3: The Bayesian Filter (Conditional Probability & Bayes’ Theorem)

P_spam = 0.1
P_ham = 0.9

P_free_given_spam = 0.9
P_free_given_ham = 0.05


P_free = (P_free_given_spam * P_spam) + (P_free_given_ham * P_ham)


P_spam_given_free = (P_free_given_spam * P_spam) / P_free

print(P_spam_given_free)


