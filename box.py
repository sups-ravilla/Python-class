box_1 = {"Chips", "Triple choclate cookies", "Orange juice", "Rasin box", "Apple slices"}
box_2 = {"Apple slices", "Orange juice", "Raisin box"}
print("Here is Snack box 1:", box_1)
print("Here is Snack box 2:", box_2)

box_2.add("Banana")
print("")
print("Here is Snack box 2 after adding a banana:", box_2)

common_snacks = box_1.intersection(box_2)
print("")
print("Here are the snacks that are in both boxes:", common_snacks)

import array as arr
snack_counts = arr.array('i', [4, 6, 3, 5])
print("")
print("Snack counts array:", snack_counts)

snack_counts.insert(0, 2)
snack_counts.append(7)
print("")
print("Snack counts after adding items:", snack_counts)

count_of_3 = snack_counts.count(3)
print("")
print("Number of times 3 appears:", count_of_3)

snack_counts.reverse()
print("")
print("Reversed snack counts array:", snack_counts)

print("")
print("===== SCHOOL SNACK COUNTER =====")
print("Snack Box 1:", box_1)
print("Snack Box 2:", box_2)
print("Shared snacks:", common_snacks)
print("Snack counts:", snack_counts)
print("================================")