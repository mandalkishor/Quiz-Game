questions=("1. What does HTML stand for?",
           "2.What does CSS stand for?",
           "3.Which of the following is the correct way to use the standard namespace in C++?",
           "4.Which of the following is not a part of the string class",
           "5.Which of the following classes would allow random numbers to be generated?",
           "6.An applet doesn't have a _______ method",
           "7.What year was Java created?",
           "8.What company helped create Java?",
           "9.What is the name of the program we use to develop out Java programs?",
           "10.Which of the following are not one of the five main parts of a Java program?")

options=(("A.Hyper Trainer Marking Language ",
          "B.Hyper Text Marketing Language ",
          "C.Hyper Text Markup Language ",
          "D.Hyper Text Markup Leveler"),
         ("A.Computer Style Sheets ",
          "B.Creative Style Sheets ",
          "C.Colorful Style Sheets ",
          "D.Cascading Style Sheets"),
         ("A.Using namespace std; ",
          "B.Using namespace standard; ",
          "C.Using standard namespace; ",
          "D.Standard namespace used;"),
         ("A.CompareTo ","B.Length ","C.Concat ","D.ToString"),
         ("A.Math ","B.Random ","C.String ","D.Keyboard"),
         ("A.Main","B.Secondary","C.Primary","D.System"),
         ("A.1996","B.1994","C.1995","D.1999"),
         ("A.Microsoft","B.Sun Microsystem","C.Norton's","D.Dell"),
         ("A.Java Creator","B.JCreator","C.Creator Java","D.Visual Java 6.0"),
         ("A.Main Method","B.Class Header","C.Class Body","D.Main Body"))

answers=("C","D","A","D","B","A","C","B","B","D")
guesses=[]

score=0

question_num=0

for question in questions:
    print("__________________")
    print(question)

    for option in options[question_num]:
        print(option)


    guess=input("Enter(A, B, C, D):").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer") 

    question_num+=1
print("__________________")
print("     RESULTS      ")
print("__________________")

print("answers: ",end="")
for answer in answers:
     print(answer,end="")
print()

print("guesses: ",end="")
for guess in guesses:
        print(guess,end="")
print()

score=int(score/len(questions) * 100)
print(f"your score is:{score}%")
  
