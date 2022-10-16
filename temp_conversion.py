# Celcius---->Fahrenheit // Fahrenheit=Celcius X (1.8) + 32
# Fahrenheit ----->Celcius // Celcius=(Fahrenheit -32)/1.8
# Celcius----->Kelvin // Kelvin=Celcius +273.15
# Kelvin ---->Celcius // Celcius= Kelvin -273.15

def CelciusToFahrenheit(celcius):
    Fahrenheit= celcius*1.8 +32
    return Fahrenheit
def FahrenheitToCelcius(Fahrenheit):
    Celcius=(Fahrenheit-32)/1.8
    return Celcius
def CelsiusToKelvin(celcius):
    Kelvin= celcius + 273.15
    return Kelvin
def KelvinToCelcius(Kelvin):
    Celcius=Kelvin - 273.15
    return Celcius

temperature=float(input("Please enter the degree in Celcius: "))
print("Fahrenheit",CelciusToFahrenheit(temperature))
print("Kelvin",CelsiusToKelvin(temperature))#------>Fonksiyonumuzu içine gönderiyoruz.


