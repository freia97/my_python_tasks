table_cards =  ["A_S", "J_H", "7_D", "8_D", "10_D"]
hand_cards = ["J_D", "3_D"]

l1 = [x[-1] for x in table_cards]
l2 = [x[-1] for x in hand_cards]

sg = l1 + l2

flash = False
for i in "CHSD":
    if sg.count(i) >= 5:
        flash = True

if flash:
    print("flush!")
else:
    print("no flush!")
