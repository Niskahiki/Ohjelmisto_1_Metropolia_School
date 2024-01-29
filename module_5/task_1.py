import random

count_of_dice = int(input("Anna heitettävien arpakuutioiden määrä: "))

dice_sum = 0
for _ in range(count_of_dice):
    dice_sum += random.randint(1, 6)

print(f"Arvottujen arpakuutioiden summa: {dice_sum}")