""" 4) შექმენით სია რომელშიც იქნება საჭმელების სახელები შექმენით მეორე სია რომელშიც იქნება მანქანების სახელები შემდეგ კი ეს ორი სია გააერთიანეთ და დაბეჭდეთ გაერთიანებული სია """

food = ['ხაჭაპური', 'ლობიანი', 'პიცა', 'ხინკალი', 'მწვადი', 'ღომი', 'სალათი']
car = ["BMW", 'Mersedes', 'Audi', 'Toyota', 'Honda']

# 1
list = []
list.extend(food)
list.extend(car)
print(list)

# 2
food.extend(car)
print(food)
