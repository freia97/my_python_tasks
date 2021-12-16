up = 100
down = 0
n = (up + down) // 2
while True:
    print("> или < ", n)
    answer = int(input("1 =" + " " + "2 >" + " " + "3 <"))
    if answer == 1:
        print("угадал")
        break
    if answer == 2:
        down = n
        n = (up + down) // 2
    if answer == 3:
        up = n
        n = (up + down) // 2