from sympy import Point


questions=["Which city is famous for its kebab ?","Which city is famous for its ice cream?",
"Which city is famous its baklava? "]

questionsOne=["A)Adana" ,"B)Mersin" ,"C)Şanlıurfa","D)Konya"]
questionsTwo=["A)Sivas","B)Maraş" ,"C) İzmir", "D)Ankara "]
questionsThree=["A)Kilis", "B)Şanlıurfa", "C)Gaziantep","D)izmir "]
answers=["a","b","c"]

def ask():
    point=0
    print("QuestionOne: ",questions[0])
    for i in questionsOne:
        print(i)
    answerOne=input("What is your answer?")
    if (answerOne==questionsOne[0]):
       print("Congratulations.Your answer is True.")
       point+=1

    else:
        print("Your answer is False.Correct answer is A.")
        point-=1 

    answerTwo=input("What is your answer?") 
    if (answerTwo==questionsTwo[1]):
        print("Congratulations.Your answer is True.")
        point+=1
    else:
        print("Your answer is False.Correct answer is B.")
        point-=1
      
    answerThree=input("What is your answer?") 
    if (answerThree==questionsThree[2]):
        print("Congratulations.Your answer is True.")
        point+=1
    else:
        print("Your answer is False.Correct answer is C.")
        point-=1
        

print("Game is over.Your total point is {point}")
ask()

