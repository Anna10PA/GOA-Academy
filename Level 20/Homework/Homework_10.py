''' 10) დაითვალე დადებითი და უარყოფითი რიცხვების ჯამი სიიდან '''

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

neg = 0
pos = 0

for i in list:
    if i >0:
        pos = pos + i
    else:
        neg = neg + i
print(pos)
print(neg)