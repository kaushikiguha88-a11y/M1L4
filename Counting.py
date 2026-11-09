amount = int(input("Enter your amount of notes"))
note1 = amount // 100
note2 = (amount % 100)// 50
note3 = (((amount % 100)% 50)// 10)
print("You require ", note1," notes of 100 and ", note2," notes of 50 and ", note3 ," notes of 10")
