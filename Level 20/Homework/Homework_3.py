''' 3) შექმენით სია და for loop დახმარებით გამოიტანეთ მხოლოდ ლუწი ინდექსებზე მდგომი ელემენტები
'''

list = [1, 2, 3, 4, 5, 6, 10, 39, 14, 90]
for i in range(len(list)):
    if i % 2 == 0:
        print(list[i])