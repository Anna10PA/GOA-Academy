""" 3) შექმენით სია რომელშიც გექნებათ ათიცალი სხვადასხვა რიცხვი შემდეგ კი დაბეჭდეთ ამ სიიდან მხოლოდ 10ზე დაბალი რიცხვები გამოიყენეთ for loop"""
number = [1, 20, 5, 2, 10, 40, 8, 9, 3, 4]
for i in range(len(number)):
    if number[i] < 10:
        print(str(number[i]) + ' არის 10-ზე ნაკლები')