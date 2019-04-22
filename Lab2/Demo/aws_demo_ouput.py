with open("demo_wc.txt","w") as demo:
    with open("demo_part1","r") as file1:
        data1 = file1.readlines()
        for data in data1:
            demo.write(data)
        print("First File Finished")
    with open("demo_part2","r") as file2:
        data2 = file2.readlines()
        for data in data2:
            demo.write(data)
        print("Second File Finished")
    with open("demo_part3","r") as file3:
        data3 = file3.readlines()
        for data in data3:
            demo.write(data)
        print("Third File Finished")

file1.close()
file2.close()
file3.close()
demo.close()