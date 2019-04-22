#Authors: Anthony Introne
#         Michael Klein
# Opening file and converting each line into a key value pair and appending to list
with open("../WordCountData/cc_wc.txt","r") as cc:
    tuple_list = []
    data = cc.readlines()
    for line in data:
        lst = line.split()
        tup = (lst[0],int(lst[1]))
        tuple_list.append(tup)
    tuple_list.sort(key = lambda x: x[1], reverse = True)  
    with open("../WordCountData/cc_wc_sorted.txt","w") as new_cc:
        for element in tuple_list:
            string = element[0] + " " + str(element[1])
            new_cc.write(string + "\n")
cc.close()
new_cc.close()

# Opening file and converting each line into a key value pair and appending to list
with open("../Co-OccurrenceData/reducer_output.txt","r") as cc:
    tuple_list = []
    data = cc.readlines()
    for line in data:
        word = line[:len(line) - 4]
        count = line[len(line) - 2:len(line) - 1]
        tup = (word, int(count))
        tuple_list.append(tup)
        
    tuple_list.sort(key = lambda x: x[1], reverse = True) 
    with open("../Co-OccurrenceData/output_sorted.txt","w") as new_cc:
        for element in tuple_list:
            string = element[0] + " " + str(element[1])
            new_cc.write(string + "\n")

cc.close()
new_cc.close()