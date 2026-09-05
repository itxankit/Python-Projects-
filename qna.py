questions = (("1. what is the prime minister of India?"),("2. what is the capital of France?"),("3. who wrote 'Pride and Prejudice'?") )

options = (("A.Narendra Modi", "B.Rahul Gandhi", "C.Manmohan Singh"),("A.Paris", "B.London", "C.Berlin"),("A.Jane Austen", "B.Charlotte Brontë", "C.Emily Dickinson"))

answers = ("A", "A", "A")
guesses = []
score = 0
questions_num = 0

print(" ")
print('WELCOME TO QUIZZ GAME !!!')
print("--------------------------")

print('Here is your 1st question...')
print(" ")


for que in questions:
    print("--------------------------")
    print(que,end = " ")
    print('')
    for ops in options[questions_num]:
        print(ops, end = "")
        print('')

    guess = input("Choose Your Answer (A,B,C):").upper()
    guesses.append(guess)
    if guess.upper() == answers[questions_num]:
        print("✔️Corrent Answer !!!")
        score += 1
        questions_num = questions_num+1
        print(f"⚠️your current status- Q.{questions_num}score:{score}" )
        questions_num = questions_num-1
    else:
        print("❌Wrong Answer !!!")
        questions_num = questions_num+1
        print(f"⚠️your current status- Q.{questions_num}score:{score}" )
        questions_num = questions_num-1
    questions_num = questions_num+1
    print('')

print("--------------------------")