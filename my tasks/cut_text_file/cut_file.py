count = 0
with open("5815016.txt", "r") as file:
    temp = file.read()

for simvol in temp:
    if count % 10000 == 0:
        with open("result/part_" + str(count // 10000) + ".txt", "w") as file_write:
            file_write.write(temp[count - 10000:count])
    count += 1
