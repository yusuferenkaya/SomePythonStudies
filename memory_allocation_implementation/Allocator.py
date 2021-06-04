import sys
try:
    file1 = open(sys.argv[1], "r")
    file2 = open("output.txt", "w")
    line_list = [list(map(int,line.strip().split(","))) for line in file1.read().splitlines() if line]
    memories, processes = line_list[0], line_list[1]
    # For first-fit algorithm
    file2.write("First-Fit Memory Allocation\n")
    file2.write(30*"-"+"\n\n")
    temp_memories = memories[:]
    file2.write("start => " + " ".join(list(map(str,temp_memories))) + "\n")
    for process in processes:
        allocated = None
        for memory in temp_memories:
            index = temp_memories.index(memory)
            if type(memory) == int and memory >= process:
                temp_memories[index] -= process
                if temp_memories[index] == 0:
                    temp_memories.remove(temp_memories[index])
                temp_memories.insert(index, str(process) + "*")
                file2.write("\n" + str(process) + "=> ")
                file2.write(" ".join(list(map(str, temp_memories))) + "\n")
                allocated = True
                break
        if not allocated:
            file2.write("\n" + str(process) + "=> " + "not allocated, must wait" + "\n")

    # Best-fit
    file2.write("\n\nBest-Fit Memory Allocation\n")
    file2.write(30*"-"+"\n\n")
    temp_memories = memories[:]
    file2.write("start => " + " ".join(list(map(str,temp_memories))) + "\n")

    for process in processes:
        try:
            to_be_partitioned = min([memory for memory in temp_memories if type(memory) == int and memory >= process])
            index = temp_memories.index(to_be_partitioned)
            temp_memories[index] -= process
            if temp_memories[index] == 0:
                temp_memories.remove(temp_memories[index])
            temp_memories.insert(index,str(process)+"*")
            file2.write("\n" + str(process) + "=> ")
            file2.write(" ".join(list(map(str,temp_memories))) + "\n")
        except:
            file2.write("\n" + str(process) + "=> " + "not allocated, must wait\n")
    # Worst-fit
    file2.write("\n\nWorst-Fit Memory Allocation\n")
    file2.write(30*"-"+"\n\n")
    temp_memories = memories[:]
    file2.write("start => " + " ".join(list(map(str,temp_memories))) + "\n")

    for process in processes:
        try:
            to_be_partitioned = max([memory for memory in temp_memories if type(memory) == int and memory >= process])
            index = temp_memories.index(to_be_partitioned)
            temp_memories[index] -= process
            if temp_memories[index] == 0:
                temp_memories.remove(temp_memories[index])
            temp_memories.insert(index,str(process)+"*")
            file2.write("\n" + str(process) + "=> ")
            file2.write(" ".join(list(map(str,temp_memories))) + "\n")
        except:
            file2.write("\n" + str(process) + "=> " + "not allocated, must wait\n")
    file2.write("\n")
    file1.close()
    file2.close()

except:
    print("There were some problem during reading the file."
          "Input file might not exist")
