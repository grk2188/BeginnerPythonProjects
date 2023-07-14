
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

p1, p2 = position[0], position[1]
p1 = int(p1)
p2 = int(p2)
p1 -= 1
p2 -= 1
map[p2][p1] = 'X'

print(f"{row1}\n{row2}\n{row3}")

