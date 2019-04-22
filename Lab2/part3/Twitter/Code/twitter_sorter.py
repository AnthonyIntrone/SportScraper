#Authors: Anthony Introne
#         Michael Klein
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

with open("../Co-OccurrenceData/reducer_output.txt","r") as twitter:
    tuple_list = []
    data = twitter.readlines()
    for line in data:
        word = line[:len(line) - 4]
        count = line[len(line) - 2:len(line) - 1]
        tup = (word, int(count))
        tuple_list.append(tup)
        print("almost")
    tuple_list.sort(key = lambda x: x[1], reverse = True) 
    print("yay")
    with open("../Co-OccurrenceData/output_sorted.txt","w") as new_twitter:
        for element in tuple_list:
            string = element[0] + " " + str(element[1])
            new_twitter.write(string + "\n")

        print("done")
twitter.close()
new_twitter.close()