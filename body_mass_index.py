
def bmi(w,h):#İki değişkenli bir fonksiyon oluşturuyoruz.
    global bmi #---> Fonksiyon dışında da kullanabilmek için global keyword kullanıldı.
    bmi= w/(h**2)
    print("Your bady mass index is : ")
    return bmi

w=float(input("Enter Your Weight: "))
h=float(input("Enter Your Height: "))

bmi(w,h)#--->Fonksiyonu çağırıyoruz.

if (bmi<18,5):
    print("Your are weak.", bmi )
elif (bmi>=18 and bmi<24,9):
    print("Your are normal.", bmi)
elif (bmi>=24,9 and bmi<29,9 ):
    print("You are overweight.", bmi)
elif("bmi>=29,9" and bmi<39,9):
    print("You are fat.",bmi)
else:
    print("You are obese.",bmi)