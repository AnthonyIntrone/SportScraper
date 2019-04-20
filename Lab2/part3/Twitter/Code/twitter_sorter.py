# Opening file and converting each line into a key value pair and appending to list
with open("../WordCountData/twitter_wc.txt","r") as twit:
    tuple_list = []
    data = twit.readlines()
    for line in data:
        lst = line.split()
        tup = (lst[0],int(lst[1]))
        tuple_list.append(tup)
        tuple_list.sort(key = lambda x: x[1], reverse = True)  
    with open("../WordCountData/twitter_wc_sorted.txt","w") as new_twit:
        for element in tuple_list:
            string = element[0] + " " + str(element[1])
            new_twit.write(string + "\n")
twit.close()
new_twit.close()