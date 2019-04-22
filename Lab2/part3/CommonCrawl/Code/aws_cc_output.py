#Authors: Anthony Introne
#         Michael Klein
# Combining the aws output files into one
with open("../WordCountData/cc_wc.txt","w") as cc:
    with open("../WordCountData/cc_part1","r") as file1:
        data1 = file1.readlines()
        for data in data1:
            cc.write(data)
        print("First File Finished")
    with open("../WordCountData/cc_part2","r") as file2:
        data2 = file2.readlines()
        for data in data2:
            cc.write(data)
        print("Second File Finished")
    with open("../WordCountData/cc_part3","r") as file3:
        data3 = file3.readlines()
        for data in data3:
            cc.write(data)
        print("Third File Finished")

file1.close()
file2.close()
file3.close()
cc.close()