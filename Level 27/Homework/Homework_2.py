'''2) მომხმარებელს შემოატანინეთ რიცხვი და შემდეგ for loop - ის გამოყენებით გამოიტანეთ ამ რიცხვამდე ყველა რიცხვის ჯამი(მაგალითად თუ შეიყვანს 10ს გამოიტანეთ 10მდე ყველა რიცხვის ჯამი მაგალითად).'''

number = int(input("Enter number: "))

sum = 0
for i in range(number + 1):
    sum += i
print(sum)