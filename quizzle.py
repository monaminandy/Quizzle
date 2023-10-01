print("Welcome To Quizzle :)")
while True:
    i=input("""Enter W for word game
Enter Q for quiz game
Enter E to Exit:""")
    if i=='W':
        print("Arrange the given words to form a sentence")
        word={
            1:{
                "question":"the/sparrow/from/city/It/disappeared/house/has/seems/common/the/that",
                "answer" : "It seems that the common house sparrow has disappeared from the city."
                },
            2:{
                "question":"believed in/People of India/the sacredness of/have traditionally/wildlife",
                "answer" : "People of India have traditionally believed in sacredness of wildlife."
                },
            3:{
                "question":"they/in the/hall/for/two hours/watching/had been/television",
                "answer" : "They had been watching television in the hall for two hours."
                },
            4:{
                "question":"occupy/history/in/of/India/honoured/Rajputs/the/the/an/place",
                "answer" : "The Rajputs occupy honoured place in the history of India."
                },
            5:{
                "question":"factors/and/pollution/herbs/native/important/the/responsible/are/loss/shrubs/of/and",
                "answer" : "The important factors responsible are pollution and loss of native herbs and shrubs."
                },
            6:{
                "question":"to/the/popularity/every corner/junk food/has led/ of eating/joints/around/of/the/opening",
                "answer" : "The popularity of junk food has led to the opening of eating joints around every corner."
                },
            }
        score=0
        for question in word:
            print(word[question]['question'])
            answer=input("Enter answer:")
            if answer==word[question]['answer']:
                print("Correct answer")
                score+=1
                print("Score:",score)
            else:
                print("wrong answer")
                print('Correct answer:',word[question]['answer'])
                print("Score:",score)
        print('Thanks for playing Quizzle:)')
    elif i=='Q':
        print("Answer in one word")
        quiz={
            1:{
                "question":"I turn once,what is out will not get in. I turn again, what is in will not get out. What am I?",
                "answer" : "Key"
                },
            2:{
                "question":"If you drop me I am sure to crack, but give me a smile and I will always smile back. What am I?",
                "answer" : "Mirror"
                },
            3:{
                "question":"What begins with an 'E' and only contains one letter?",
                "answer" : "Envelope"
                },
            4:{
                "question":"People make me, save me, raise me,change me. What am I?",
                "answer" : "Money"
                },
            5:{
                "question":"What can travel all around the world without leaving its corner?",
                "answer" : "Stamp"
                },
            6:{
                "question":"I am an odd number. take away a letter and I become even. What number am I?",
                "answer" : "Seven"
                },
            }
        score=0
        for question in quiz:
            print(quiz[question]['question'])
            answer=input("Enter answer:")
            if answer==quiz[question]['answer']:
                print("Correct answer")
                score+=1
                print("Score:",score)
            else:
                print("wrong answer")
                print('Correct answer:',quiz[question]['answer'])
                print("Score:",score)
        print('Thanks for playing Quizzle:)')
    elif i=='E':
            break
    else:
        print("Enter either W or Q or E")