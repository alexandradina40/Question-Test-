from Proitect_Alegeri import Question

questions_prompts = [
    "True Or False, Wikipedia Is Written Only By Qualified Professionals?\n a)True\n b) False\n",
    "What country is sushi from?\n a)Thailand\n b)Japan\n c)India\n d)France\n",
    "According to the Old Testament, how many days did it take God to create the world?\n a)1\n b)7\n c)6\n d)2\n",
    "Which is the world's most populous country? a)China\n b)America \n c)India\n d)Brazil\n"
]  # these are 4 questions that i want to ask the user


questions = [
    Question(questions_prompts[0], "b"),
    Question(questions_prompts[1], "b"),
    Question(questions_prompts[2], "c"),
    Question(questions_prompts[3], "a")
] # these are the answers for the  each question_promts from above

def run_test(questions): # using this function we run the test
    score=0
    for question in questions:   # we go in a loop from 0th to the 3th questions and if the
        answer=input(question.prompt)  # answer is correct we add 1 to the score
        if answer==question.answer:
            score=score+1

    print("You got " +str(score)+ "/" + str(len(questions))+" correct!") # here i print the score the user got from
                                                                        # the max of score

run_test(questions)