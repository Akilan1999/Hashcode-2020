
#read file name 
f = open("", "r")


# first line read 
maxtypes = f.readline()

# can be stored to array if needed 
slices ,types = [int(word) for word in maxtypes.split()]

# reads other lines 
line = f.readline()

list1 = []

list1 = line.split()

print(list1)

answer_array = []
    

f = open("solution.out", "w")
f.write(str(len(answer_array)) + "\n")

for ans in answer_array:
    f.write(str(ans) + " ")
