import random
#read file name 
f = open("d_tough_choices.txt", "r")


# first line read 
maxtypes = f.readline()

# can be stored to array if needed 
books ,library, days = [word for word in maxtypes.split()]

score_book = f.readline()

score_books = []

score_books = [word for word in score_book.split()]



array = []

for lib in range(int(library)):
    pro_lib = f.readline()
    book,day,ship = [word for word in pro_lib.split()]
    array.append([book,day,ship])
    pro_lib = f.readline()
    temp_list = []
    temp_list = [word for word in pro_lib.split()]
    another_array = []
    for i in range(len(temp_list)):
        v1 = int(temp_list[i])
        v2 = score_books[v1]
     #   print(v2)
        another_array.append([v1,v2])
        
    array[lib].append(another_array)

#print(array)

answer_array = []

for i in range(int(len(array)/2)):
    running = True
    while running:
       
        rand = random.randint(0,(int(len(array)) - 1))
        running = False
        for x in range(len(answer_array)):
          
            if rand == answer_array[x][0]:
                running = True

    answer_array.append([rand,[]])
    
    for j in range(len(array[rand][3])):
        answer_array[i][1].append(array[rand][3][j][0])
       # print(answer_array[i])

#[[0,[1,2]]]



f = open("solution.txt", "w")
f.write(str(len(answer_array)) + "\n")

for i in range(len(answer_array)):
    f.write(str(answer_array[i][0]) + " " + str(len(answer_array[i][1])) + "\n")
    for a in range(len(answer_array[i][1])):
        if a == 0:
            f.write(str(answer_array[i][1][a]) + " ")
        elif a == 1:
            f.write(str(answer_array[i][1][a]))
        else:
            f.write(" " + str(answer_array[i][1][a]))

    f.write("\n")





# reads other lines 
#line = f.readline()

#list1 = []

#list1 = line.split()

#print(list1)

#answer_array = []
    

#f = open("solution.out", "w")
#f.write(str(len(answer_array)) + "\n")

#for ans in answer_array:
#    f.write(str(ans) + " ")
