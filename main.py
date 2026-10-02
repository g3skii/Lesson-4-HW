# სავარჯიშო ნ1

age = int(input("ასკი: "))
parent = input("მშობელთან ერთად ხართ? ")

if age >= 18 :
    result = "შესვლა დაშვებულია"

elif age >= 12:
    if parent == "კი":
       result = "შესვლა დაშვებულია"
    else:
        result = "შეზღუდულია წვდომა"
else:
    result = "არ დაიშვება"

print(result)


# სავარჯიშო ნ2

a = int(input("პირველი რიცხვი: "))
b = int(input("მეორე რიცხვი: "))
c = int(input("მესამე რიცხვი: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b>= c:
    largest = b
else:
    largest = c

print("უდიდესი რიცხვი: ", largest)