

def calculator(number1,number2,process):
    sonuc=0
    if (process==1):
        result = number1 + number2
        return result
    elif (process==2):
        result= number1 - number2
        return result
    elif (process==3):
        result= number1 * number2
        return result 
    elif (process==4):
        result= number1 / number2
        return result 
    elif (process==5):
        result =number1**number2
        return result
    else:
        print("Please enter a valid number.")
     

number1= int(input("Please enter number1: "))
number2=int(input("Please enter number2: "))
process=int(input("Please enter process type: "))

process_result= calculator(number1,number2,process) #We call the function for run. 
print("Process result :",process_result)



    
        