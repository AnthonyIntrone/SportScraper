#Authors: Anthony Introne
#         Michael Klein

# Combining the aws output files into one
with open("../output/HFinn/HFinn_wc.txt","w") as HFinn:
    with open("../output/HFinn/HFinn_part1","r") as file1:
        data1 = file1.readlines()
        for data in data1:
            HFinn.write(data)
        print("First HFinn File Finished")
    with open("../output/HFinn/HFinn_part2","r") as file2:
        data2 = file2.readlines()
        for data in data2:
            HFinn.write(data)
        print("Second HFinn File Finished")
    with open("../output/HFinn/HFinn_part3","r") as file3:
        data3 = file3.readlines()
        for data in data3:
            HFinn.write(data)
        print("Third HFinn File Finished")

file1.close()
file2.close()
file3.close()
HFinn.close()

# Combining the aws output files into one
with open("../output/PG345/pg345_wc.txt","w") as Pg345:
    with open("../output/PG345/pg345_part1","r") as file4:
        data1 = file4.readlines()
        for data in data1:
            Pg345.write(data)
        print("First Pg345 File Finished")
    with open("../output/PG345/pg345_part2","r") as file5:
        data2 = file5.readlines()
        for data in data2:
            Pg345.write(data)
        print("Second Pg345 File Finished")
    with open("../output/PG345/pg345_part3","r") as file6:
        data3 = file6.readlines()
        for data in data3:
            Pg345.write(data)
        print("Third Pg345 File Finished")

file4.close()
file5.close()
file6.close()
Pg345.close()