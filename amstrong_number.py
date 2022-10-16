


sayi=int(input("Kontrol edilecek sayı: "))
toplam=0
gecici=sayi
while (gecici>0):
    digit=gecici%10
    toplam+=digit**3
    gecici//=10

if sayi==toplam:
    print("Bu sayı amstrong sayısıdır.")
else:
    print("Bu sayı amstrong sayısı değildir.")