""" 5) შექმენით სია რომელშიც გექნებათ ოცი სხვადასხვა რიცხვი შემდეგ კი დაბეჭდეთ მხოლოდ 20 ზე მეტი რიცხვები ისე რომ იყოს თან სამის ჯერადი გამოიყენეთ for loop"""

number = [1, 4, 6, 10, 6, 12, 5, 3, 9, 19, 20, 40, 26, 32, 39, 22, 8, 30, 300, 33]
for i in range(len(number)):
    if number[i] > 20 and number[i] % 3 == 0:
        print(str(number[i])+ ' არის 20-ზე მეტი და 3-ზე იყოფა')