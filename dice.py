import random,time#-----> Modüllerimizi import ediyoruz.

userscore1=0
userscore2=0

while True: #While doğru olduğunda çalışmaktadır.. 
    user1=random.randint(1,6)#random.randint----> rastgele sayı gönderir.Aralıklar dahildir.
    print("User1:",user1)
    time.sleep(1)

    user2=random.randint(1,6)
    print("User2",user2)
    time.sleep(1)#Kodlarımız arasına duraklama eklemek istediğimizde her durumda kullanabiliriz.

    if (user1>user2):
        print("user1 won the game.")
        userscore1+=1
    elif (user2>user1):
        print("user2 won the game")
        userscore2+=1
    else:
        print("Deuce")
    
    if (userscore1==5 or userscore2==5):
        print("user1:",userscore1,"-",userscore2,"user2")
        break