import random
response = str(input("Do you want to roll a dice? y/n "))


while response == str('y'):
    i = 0
    no = random.randint(1, 6)
    while i < 6:
        print(no)
        i += 1
    response = str(input("Do you want to keep spinning? y/n "))
