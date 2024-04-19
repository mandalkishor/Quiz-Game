questions=("KKKKK","MMMMMM","MMMMMM","MMMMMM","MMMMMM")

options=(("A. ","B. ","C. ","D"),
         ("A. ","B. ","C. ","D"),
         ("A. ","B. ","C. ","D"),
         ("A. ","B. ","C. ","D"),
         ("A. ","B. ","C. ","D"))

answers=("C","D","A","B")
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