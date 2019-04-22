# Authors: Anthony Introne
#          Michael Klein
# Opening file and converting each line into a key value pair and appending to list
with open("demo_wc.txt","r") as demo:
    tuple_list = []
    data = demo.readlines()
    for line in data:
        lst = line.split()
        tup = (lst[0],int(lst[1]))
        tuple_list.append(tup)
    tuple_list.sort(key = lambda x: x[1], reverse = True)  
    with open("demo_wc_sorted.txt","w") as new_demo:
        for element in tuple_list:
            string = element[0] + " " + str(element[1])
            new_demo.write(string + "\n")
demo.close()
new_demo.close()

# Opening file and converting each line into a key value pair and appending to list
with open("reducer_output.txt","r") as demo:
    tuple_list = []
    data = demo.readlines()
    for line in data:
        word = line[:len(line) - 4]
        count = line[len(line) - 2:len(line) - 1]
        tup = (word, int(count))
        tuple_list.append(tup)
        print("almost")
    tuple_list.sort(key = lambda x: x[1], reverse = True) 
    print("yay")
    with open("output_sorted.txt","w") as new_demo:
        for element in tuple_list:
            string = element[0] + " " + str(element[1])
            new_demo.write(string + "\n")

        print("done")
demo.close()
new_demo.close()