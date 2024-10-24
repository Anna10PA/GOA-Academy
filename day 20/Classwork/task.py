#                                                   for loop

# : ნიშნავს რაღაცის დასრულებას და შემდეგ პირობა იწერება რაც უნდა შესრულდეს
# loop - რაღაცის უსასრულოდ გაგრძელება/გამეორება

# for i in range - მეშვეობით მოქმედების გამეორება შეიძლება რამდენჯერმე

# i - ცვლადის სახელი (iteration)
# საიტერაციო ცვლადია (i) 
# იტერაცია გამეორებას ნიშნავს

# range() - ფარგლებში/სიშორე

# i არის იტერაციის ცვლადი რომელიც გვიჩვენებს რამდენჯერ მეორდება

# CPU - კომპიუტერის დატვირთვას აჩვენებს

# ათვლა დაიწყება 10-დან
# ავა 20-მდე (19 იქნება ბოლო)

#                                                task example
# 1. რაღაციდან რაღაცამდე ასვლა
for i in range(10, 20, 2):
    print(i)

    # ათვლა დაიწყება 10-დან
    # ავა 20-მდე (19 იქნება ბოლო)
    # 2-ის გამოტოვებით დაიბეჭდება (10,12,14,16,18)

# 2. ჯამი 
sum = 0

for i in range(1, 4):
    sum = sum + i
    print(sum)

    # sum ცვლადში დავითვლით ჯამს და ყოველ ჯერზე ახალი მნიშვნელობა მიენიჭება. ახალი მნიშვნელობა გახდება ძველ მნიშვნელობას დამატებული i 
    # 1-დან 4-მდე შეიკრიბება (3 ბოლო)
    # 0 + 1 = 1 ;  1 + 2 = 3 ;  3 + 3 = 6 

