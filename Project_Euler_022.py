
# coding: utf-8

# # Project Euler Problem 22
# 
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
# 
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
# 
# What is the total of all the name scores in the file?
# 

# In[21]:


text_file = open("p022_names.txt", "r")
names = text_file.read().split('","')
names[0] = names[0].replace('"', '')
names[-1] = names[-1].replace('"', '')
sorted_names = sorted(names)

# name_score() uses the ord() function, which returns the ASCII
# value of a character.  For capital letters, ord('A') has a value of
# 65, ord('B') has a value of 66, etc.  So, if we subtract 64, we get
# the place of that letter in the alphabet.

def name_score(x):
    return sum(list(map(lambda y: ord(y) - 64, list(x))))

name_scores = list(map(name_score, sorted_names))

total_name_score = 0
for i in range(len(name_scores)):
    total_name_score += name_scores[i]*(i+1)
    
print("The total name score is {}".format(total_name_score))

