phone_number = input("What's your number?\n")
AreaCode = phone_number [0:3]
print (AreaCode)
FirstPart = phone_number [3:6]
LastPart = phone_number [6:10]
print("(",AreaCode,") ",FirstPart,"-",LastPart)
