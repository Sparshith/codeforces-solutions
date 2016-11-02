'''
Very soon there will be a parade of victory over alien invaders in Berland. Unfortunately, all soldiers died in the war and now the army consists of entirely new recruits, many of whom do not even know from which leg they should begin to march. The civilian population also poorly understands from which leg recruits begin to march, so it is only important how many soldiers march in step.

There will be n columns participating in the parade, the i-th column consists of li soldiers, who start to march from left leg, and ri soldiers, who start to march from right leg.

The beauty of the parade is calculated by the following formula: if L is the total number of soldiers on the parade who start to march from the left leg, and R is the total number of soldiers on the parade who start to march from the right leg, so the beauty will equal |L - R|.

No more than once you can choose one column and tell all the soldiers in this column to switch starting leg, i.e. everyone in this columns who starts the march from left leg will now start it from right leg, and vice versa. Formally, you can pick no more than one index i and swap values li and ri.

Find the index of the column, such that switching the starting leg for soldiers in it will maximize the the beauty of the parade, or determine, that no such operation can increase the current beauty.
'''

from sys import stdin
 
lines = stdin.read().splitlines()
lines.pop(0)

rows = []
initialLeftSum = 0
initialRightSum = 0
for line in lines:
    row = [int(x) for x in line.split()]
    rows.append(row)
    initialLeftSum += row[0]
    initialRightSum += row[1]

maxBeauty = abs(initialLeftSum - initialRightSum)
rowtoswitch = 0

for idx,row in enumerate(rows):
    rowMaxBeauty = abs(initialLeftSum - initialRightSum + 2*(row[1] - row[0]))
    if(rowMaxBeauty > maxBeauty):
        maxBeauty = rowMaxBeauty
        rowtoswitch = idx + 1
print(rowtoswitch)

