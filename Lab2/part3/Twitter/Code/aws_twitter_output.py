
with open("../WordCountData/twitter_wc.txt","w") as Twitter:
    with open("../WordCountData/twitter_part1","r") as file1:
        data1 = file1.readlines()
        for data in data1:
            Twitter.write(data)
        print("First File Finished")
    with open("../WordCountData/twitter_part2","r") as file2:
        data2 = file2.readlines()
        for data in data2:
            Twitter.write(data)
        print("Second File Finished")
    with open("../WordCountData/twitter_part3","r") as file3:
        data3 = file3.readlines()
        for data in data3:
            Twitter.write(data)
        print("Third File Finished")

file1.close()
file2.close()
file3.close()   
Twitter.close()