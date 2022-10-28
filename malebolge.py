from multiprocessing.connection import wait
import random
import pyfiglet

#intro
print(pyfiglet.figlet_format("M a l e b o l g e"))
print("death comes at the end")
print("current version: v0.1")
start_or_quit = input("\ntype start = ")
start_or_quit = start_or_quit.lower()
start_or_quit_checker = 0
insistor = ["I am running out of patience", "please just type start or leave me alone", "this is not difficult, are you fucking with me?"]
while start_or_quit_checker != 1:
    if start_or_quit == "start":
        print("\n\nvery well... let us begin\n\n")
        start_or_quit_checker += 1
        continue
    while start_or_quit != "start":
        print(random.choice(insistor))
        start_or_quit = input("please type what I asked you to.\nTYPE START = ")
        if start_or_quit == "start":
            start_or_quit_checker += 1


city_descr = [
"Its Gaudian spires seem to grate the hellish sky above.",
"Its stench wafts through the wasteland, riding the cold Autumn air.",
"You hear the clamor, the noise of the place, before reaching its walls.",
"The bright sun glitters off its countless spires.",
"A tower of Babel at its center breaks the horizon: a grand palace, or the fruits of untreated phallic insecurity?"]
walking_descr = [
"Others, equally lost, walk beside you. Their eyes dart about, seeking a leader.",
"You walk alone.",
"You are being followed. Best not look back."]
print("\n\nThe city of Malebolge looms before you.")
print(random.choice(city_descr))
print(random.choice(walking_descr))
print("God... How did you get here?")
prompts = ["Tell me, how??\nHOW?!?!?!?!\n\n\nHOOOOOOOOOW?! \n(type answer) = ", "\n\n\nAND TELL ME, WHAT DO YOU EXPECT TO FIND IN THAT ACCURSED CITY?! \n(type answer) = "]
choice = input(random.choice(prompts))
title = choice
print("\n\nI see... Perhaps a more important question would be...")
print("Who are you?")
print("Or, better yet: who WERE you?\nLet us find out together...\n\n\n")

#sin quiz (10 questions, determine the moral attributes of the player)
#moral compass values
consequentialism_deontology = 0
collectivism_individualism = 0
faith_in_humanity_antinatalism = 0
bliss_knowledge = 0

#question structure
class Quiz_Question:
    def __init__(self, text, answer1, answer_1_values, answer2, answer_2_values, answer3, answer_3_values):
        self.text = text
        self.a = answer1
        self.a_values = answer_1_values
        self.b = answer2
        self.b_values = answer_2_values
        self.c = answer3
        self.c_values = answer_3_values

    def __str__(self):
        rep = self.text + "\n" + self.a + "\n" + self.b + "\n" + self.c
        return rep

#answer calculator
def quiz_ask_question(question):
    answers = ["a", "b", "c"]
    value_1 = 0
    value_2 = 0
    value_3 = 0
    value_4 = 0
    print(question.__str__())
    user_answer = input("Your answer (a, b, or c)? = ")
    user_answer_lower = user_answer.lower()
    while user_answer_lower not in answers:
        user_answer = input("Please answer with a, b, or c = ")
        user_answer_lower = user_answer.lower()
    if user_answer_lower == "a":
         value_1 = question.a_values[0]
         value_2 = question.a_values[1]
         value_3 = question.a_values[2]
         value_4 = question.a_values[3]
    elif user_answer_lower == "b":
        value_1 = question.b_values[0]
        value_2 = question.b_values[1]
        value_3 = question.b_values[2]
        value_4 = question.b_values[3]
    else:
        value_1 = question.c_values[0]
        value_2 = question.c_values[1]
        value_3 = question.c_values[2]
        value_4 = question.c_values[3]
    values = [value_1, value_2, value_3, value_4]
    return values

#all the questions HERE
ayn = Quiz_Question(
"\n\nYour thoughts on Ayn Rand? Have you read Atlas Shrugged?",
"A: Read, assimilated, and put to practice. Now get the fuck out of my way.", [-1, 3, 1, 2],
"B: Ayn who?", [0, 0, -1, -3],
"C: Atlas Shrugged Deez Nuts!", [1, -2, -1, 3 ])
buddha = Quiz_Question(
"\n\nBefore losing everything and ending up here, did you consider yourself a Buddhist?",
"A: You only lose what you cling to.", [0, 3, -1, -3],
"B: I never really gave it a chance...", [-1, 0, 3, -1],
"C: Nope. Can't be Buddhist in a Ferrari. *drives away*", [0, 3, 0, 2])
jesus = Quiz_Question(
"\n\nJesus?",
"A: Probably nothing like that skinny white dude you're thinking of.", [-1, -2, 1, 3],
"B: That's what your mom was screaming last night.", [-2, 1, 0, -3],
"C: Love the guy.", [3, -1, -2, 0])
trolley_problem = Quiz_Question(
"\n\nThe trolley problem?",
"A: My name ain't trolley, and that ain't my problem.", [3, 3, 0, -2],
"B: Save the majority. Then start a union, and perhaps afterwards an orgy!", [-3, -3, -2, 0],
"C: KANSAI DOUBLE RAIL DRIFT! KILL THEM ALL!!!!", [0, -3, -3, -1])
game = Quiz_Question(
"\n\nHow do you like this game so far?",
"A: This is neato, gj mate!", [2, 0, -2, -2],
"B: Fuck this", [0, 0, 0, 0],
"C: I have only the most reasonable expectations for this videoludic experience.", [-1, 0, 0, 3])
news = Quiz_Question(
"\n\nHow do you ingest the daily correspondence?",
"A: With my mouth?", [-2, 1, 1, -2],
"B: Facebook and cable, mostly.", [2, -3, 2, 2],
"C: Go through various unsexy, reputable sources and form a well-thought out opinion, like the productive member of society I am.", [2, 2, 0, 3])
#complete list of questions
questions = [ayn, buddha, jesus, trolley_problem, game, news]

#set up the number of questions for this run
#ask for input
game_setting_question_number_string = (input("\n\nHow many questions does it take to know you?\n\nYour answer (numerical, please) = "))
#correct for errors
while not game_setting_question_number_string.isnumeric() or 0 >= int(game_setting_question_number_string) or int(game_setting_question_number_string) > len(questions): #BUG! INT CHECKER CAN BE BYPASSED BY WRITING A STRING IN THE SECOND OR THIRD WHILE LOOP, and just by going out of order
    if not game_setting_question_number_string.isnumeric():
        game_setting_question_number_string = input("\n\nCan we stop being creative for a second?\nThe only correct answer to this question is a number.\n\nHow MANY (AS IN AMOUNT, NUMBER!!!!!) questions does it take to know you? = ")
        int_checker = game_setting_question_number_string.isnumeric()

    elif int(game_setting_question_number_string) > len(questions):
        game_setting_question_number_string = input("\n\nSorry, there's no way you are that interesting.\nAnd I don't have all day.\n\nThink smaller... \nhow many questions does it take to know you? = ")

    elif int(game_setting_question_number_string) < 0:
        game_setting_question_number_string = input("\n\nWhat does that even mean?\n\nPlease, can we just answer? \nHow many questions does it take to know you? = ")

    elif int(game_setting_question_number_string) == 0:
        game_setting_question_number_string = input("\n\nAhhhhh I see...\nNot much substance on that soul, is there?\n\n\n")

game_setting_question_number = int(game_setting_question_number_string)
#collect sample of questions
randomly_selected_questions = []
for i in range(game_setting_question_number):
    question = questions.pop(random.randint(0, len(questions) - 1))
    randomly_selected_questions.append(question)

#quiz loop
for i in range(game_setting_question_number):
    quest = randomly_selected_questions.pop(random.randint(0, len(randomly_selected_questions) - 1))
    values = quiz_ask_question(quest)
    consequentialism_deontology += values[0]
    collectivism_individualism += values[1]
    faith_in_humanity_antinatalism += values[2]
    bliss_knowledge += values[3]
    #print(consequentialism_deontology)  #THESE ARE HERE TO DEBUG IF NEEDED
    #print(collectivism_individualism)
    #print(faith_in_humanity_antinatalism)
    #print(bliss_knowledge)


#player character
#stats, name, and appearance are based on results of the quiz
names = ["bob"]


class Character:
    def __init__(self, c_d, c_i, f_a, b_k):
        skill_mind = c_d
        body_skill = c_i
        soul_body = f_a
        soul_mind = b_k

        self.body = -body_skill + soul_body + random.randint(-3, 3)
        self.mind = soul_mind + skill_mind + random.randint(-3, 3)
        self.soul = -soul_mind - soul_body + random.randint(-3, 3)
        self.skill =  -skill_mind + body_skill + random.randint(-3, 3)


        self.name = random.choice(names)
    def __str__(self):
        rep = "\n\n\nYour name is " + self.name + ". \nYour value, neatly quantified:\nBody: " + str(self.body) + "\nMind: " + str(self.mind) + "\nSoul: " + str(self.soul) + "\nSkill: " + str(self.skill)
        return rep

dearly_beloved = Character(consequentialism_deontology, collectivism_individualism, faith_in_humanity_antinatalism, bliss_knowledge)
print(dearly_beloved.__str__())



