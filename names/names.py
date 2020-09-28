import time

start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# Another way

start_time3 = time.time()
dupli= []
for i in names_1:
  if i in names_2:
    if i not in dupli:
      dupli.append(i)
print("Rewritten single for loop: \n", dupli)

end_time3 = time.time()
print (f"runtime: {end_time3 - start_time3} seconds\n\n")


# Using intersection

start_time1 = time.time()
names_1_set = set(names_1)
names_2_set = set(names_2)

inter = list(names_1_set & names_2_set)
print(len(inter))
print("Using set Intersection: \n", inter)

end_time1 = time.time()
print (f"{len(inter)} duplicates\n\n")
print (f"runtime: {end_time1 - start_time1} seconds\n\n")


# Using Counter
from collections import Counter
start_time2 = time.time()

names = names_1 + names_2
print('With Counter: \n\n', [element for element, count in Counter(names).items() if count ==2])

end_time2 = time.time()
#print (f"{len(common(names_1, names_2))} duplicates\n\n")
print (f"runtime: {end_time2 - start_time2} seconds\n\n")



# Check if solution1 has the same elements as solution2
def common_member(a, b): 
    a_set = set(a) 
    b_set = set(b) 
  
    if (a_set & b_set): 
        return list(a_set & b_set) 
    else: 
        print("No common elements")  
           
print('***************************************')
print(len(common_member(duplicates, inter)))