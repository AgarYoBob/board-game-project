from random import randint
import time

start = time.time()
triple = quartro = pento = mint = blue_fulsh = red_fulsh = straight = 0

n = int(input())
for t in range (n):
    dice = []
    cnt = [0, 0, 0, 0, 0, 0]
    for i in range (6):
        rand = randint(1,6)
        dice.append(rand)
        cnt[rand-1] += 1
    print(f"{t+1} | {dice}", end='')
    if len(set(dice)) == len(dice):
        straight += 1
        print(" | straight", end='')
    elif 6 in cnt:
        mint += 1
        print(" | mint", end='')
    elif 5 in cnt:
        pento += 1
        print(" | pento", end='')
    elif 4 in cnt:
        quartro += 1
        print(" | quartro", end='')
    elif 3 in cnt:
        triple += 1
        print(" | triple", end='')

    if cnt[1] + cnt[2] + cnt[4] == 6:
        blue_fulsh += 1
        print(" | blue_fulsh", end='')
    if cnt[0] + cnt[3] == 6:
        red_fulsh += 1
        print(" | red_fulsh", end='')
    print()


print("------------------------------------------------")
print(f"triple     {triple:7} | {triple/n*100:.3f}%")
print(f"quartro    {quartro:7} | {quartro/n*100:.3f}%")
print(f"pento      {pento:7} | {pento/n*100:.3f}%")
print(f"mint       {mint:7} | {mint/n*100:.3f}%")
print(f"blue_fulsh {blue_fulsh:7} | {blue_fulsh/n*100:.3f}%")
print(f"red_fulsh  {red_fulsh:7} | {red_fulsh/n*100:.3f}%")
print(f"straight   {straight:7} | {straight/n*100:.3f}%")
print(f"------------------------------------------------\nElapsed time : {time.time() - start:.3f} seconds")
