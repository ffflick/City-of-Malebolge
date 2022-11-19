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
insistor = ["I am running out of patience", "please just  loc_type start or leave me alone", "this is not difficult, are you fucking with me?"]
while start_or_quit_checker != 1:
    if start_or_quit == "start":
        print("\n\nvery well... let us begin\n\n")
        start_or_quit_checker += 1
        continue
    while start_or_quit != "start":
        print(random.choice(insistor))
        start_or_quit = input("please  loc_type what I asked you to.\nTYPE START = ")
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
prompts = ["Tell me, how??\nHOW?!?!?!?!\n\n\nHOOOOOOOOOW?! \n( loc_type answer) = ", "\n\n\nAND TELL ME, WHAT DO YOU EXPECT TO FIND IN THAT ACCURSED CITY?! \n( loc_type answer) = "]
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
    print(question.__str__())
    user_answer = input("Your answer (a, b, or c)? = ")
    user_answer_lower = user_answer.lower()
    while user_answer_lower not in answers:
        user_answer = input("Please answer with a, b, or c = ")
        user_answer_lower = user_answer.lower()
    if user_answer_lower == "a":
        return question.a_values
    elif user_answer_lower == "b":
        return question.b_values
    else:
        return question.c_values

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
journey = Quiz_Question(
"\n\nWhat was the purpose of your insignificant journey?",
"A: The journey itself, of course.", [2, 1, 0, -1],
"B: Finding Heaven. Could this be it?", [-2, 2, -1, 1],
"C: Helping others with their own quests.", [3, -3, -3, 0])

#complete list of questions
questions = [ayn, buddha, jesus, trolley_problem, game, news, journey]

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

def player_archetype(c_d, c_i, f_a, b_k):
    archetype = []
    if c_d > 0:
        archetype.append("d")
    elif c_d < 0: 
        archetype.append("c")
    else:
        archetype.append("n")
    
    if c_i > 0:
        archetype.append("i")
    elif c_i < 0: 
        archetype.append("c")
    else:
        archetype.append("n")
    
    if f_a > 0:
        archetype.append("a")
    elif f_a < 0: 
        archetype.append("f")
    else:
        archetype.append("n")

    if b_k > 0:
        archetype.append("k")
    elif b_k < 0: 
        archetype.append("b")
    else:
        archetype.append("n")

    return archetype

pc_soul_type = player_archetype(consequentialism_deontology, collectivism_individualism, faith_in_humanity_antinatalism, bliss_knowledge)

#descriptor random tables: head determined by b_k, body by c_i, style by c_d, name by f_a
#first sublist is for negative result in corresponding stat
#second sublist is for neutral results
#third is for positive results
character_head_descriptors = [['that of a stubborn donkey, rude and intimidating', "covered in moss, beautifully flourishing, with roses and tulips for hair", "blue like the sky, your hair like clouds, your eyes like stars"],["just as it was in life, in the prime of your youth", "featureless, like an incomplete sculpture", "made of melting wax"],['owl-like, with great piercing eyes', "feline, with an ever-troubling glint of curiosity", "concealed by a mask of stained glass", "nothing but a thick gangle of eyes"]]
character_body_descriptors = [["always warm, alawys welcoming", "sturdy, and covered in thick white fur", "blocky and angular, like an old game cube sprite"],["just as it was in life, in the prime of your youth", "translucent, with three pulsing hearts visible through your bare chest", "thin as a scarecrow, and tall as a lightpost"],["lean and muscled, with the bottom half of a great python", "like a centaur's, your skin itches for freedom", "made of tin, sturdy and hollow", "robotic, powered by battery and arcane forces"]]
character_style_descriptor = [["Great goat-like horns adorn your head, and a pointed tail sprouts from your behind", "You have great bat-like wings", "Wherever you pass, nature whithers slightly"],["Aside from that, you are completely ordinary", "To all who see you, you appear blurry and difficult to discern", "Thick fog pours from your orifices"],["Great angel wings adorn your back", "A halo of rainbow light floats above your head", "Wherever you go, tiny flowers of all colors bloom in your wake"]]
names = [["Sprite", "Mikhaal", "Golda", "Childe of Man"],["Bob", "Richard", "REDACTED", "Dullard"],["K'Rririk", "FHWEIHQOWJFDQUWBFUIQWBFUMQWOFJIFG", "Brown Jenkin", "Keziah", "unpronouceable to all but yourself"]]
#the following function basically picks a table and rolls the dice for each
def character_aesthetics(attribute, table):
    result = ""
    if attribute > 0:
        result = random.choice(table[2])
    elif attribute < 0:
        result = random.choice(table[0])
    else:
        result = random.choice(table[1])
    return result


class Character:
    def __init__(self, c_d, c_i, f_a, b_k):
        #correlates attributes to stats
        skill_mind = c_d
        body_skill = c_i
        soul_body = f_a
        soul_mind = b_k
        #builds the player's character sheet
        self.body = -body_skill + soul_body + random.randint(-3, 3)
        self.mind = soul_mind + skill_mind + random.randint(-3, 3)
        self.soul = -soul_mind - soul_body + random.randint(-3, 3)
        self.skill =  -skill_mind + body_skill + random.randint(-3, 3)
        #rolls on the random tables to determin character aesthetics
        self.name = character_aesthetics(faith_in_humanity_antinatalism, names)
        self.body_descr = character_aesthetics(collectivism_individualism, character_body_descriptors)
        self.head_descr = character_aesthetics(bliss_knowledge, character_head_descriptors)
        self.style_descr = character_aesthetics(consequentialism_deontology, character_style_descriptor)
    def __str__(self):
        rep = "\n\n\nYour name is " + self.name + ".\nYour head is " + self.head_descr + "\nYour body is " + self.body_descr + "\n" + self.style_descr + "\n\n\nYour value, neatly quantified:\nBody: " + str(self.body) + "\nMind: " + str(self.mind) + "\nSoul: " + str(self.soul) + "\nSkill: " + str(self.skill)
        return rep


dearly_beloved = Character(consequentialism_deontology, collectivism_individualism, faith_in_humanity_antinatalism, bliss_knowledge)
print(dearly_beloved)
print("Now, with nowhere else to go, you enter the city.")


#district class, one for each sin. These determine the descriptors in the locations and encounters
class District:
    def __init__(self, name, loc_descriptors, char_descriptors, obj_descriptors, objects, location_table):
        self.name = name
        self.location_descriptors = loc_descriptors
        self.character_descriptors = char_descriptors
        self.object_descriptors = obj_descriptors
        self.randomstuff = objects
        self.locations = location_table
#bodies of the seven districts
lust = District("lust",
    ["perfumed", "luxurious", "intricately ornate", "covered in pillows", "golden"],
    ["sensual", "voluptious", "devious", "hungry-eyed", "horny", "soft", "beautiful", "elegant", "nude"],
    ["spiked", "gilded", "cushioned", "lubricatred", "studded", "ribbed", "leathery"],
    ["dildos", "chocolate truffles", "cherries", "grapes", "melons", "erotic statuettes"],
    {"market": 3})
gluttony = District("gluttony",
    ["pungent", "red", "rotting", "odorous", "excessive", "deliciously fragrant"],
    ["coupulent", "obese", "starving", "greasy"],
    ["edible", "half-eaten", "spiced", "greasy",],
    ["multilayered cakes", "pots and pans", "rats on a skewer"],
    {"market": 6})
greed = District("greed",
    ["golden", "bejewled", "excessive", "intricately engraved", "glistening"],
    ["elegant", "silk-clad", "gold and jewel-covered"],
    ["golden", "emerald", "ruby", "shiny"],
    ["jewels", "gold coins", "empty sacks", "ancient relics", "forbidden books"],
    {"market": 9})
sloth = District("sloth",
    ["messy", "pillowed", "deserted", "dusty", "ruined"],
    ["disheveled", "depressed", "asleep", "sickly", "slow-witted"],
    ["rotting", "falling apart", "dusty", "useless"],
    ["bedrolls", "pillows", "mushrooms"],
    {"market": 2})
wrath = District("wrath",
    ["clamorous", "bloody", "blackiron", "bustling", "scorching"],
    ["enraged", "bloodshot-eyed", "berserk", "oddly calm", "foaming at the mouth"],
    ["spiked", "bloodied", "sharp-edged", "dangerous"],
    ["zweihanders", "spears", "warhorses", "chariots", "mercenary golems"],
    {"market": 2})
envy = District("envy",
    ["dull", "tacky", "baroque"],
    ["hungry-eyed", "spiteful", "rag-clad", "miserly"],
    ["stolen", "chained", "locked"],
    [],
    {"market": 9})
pride = District("pride",
    ["towering", "gothic", "spired", "many-storied", "gilded", "obsidian"],
    ["regal", "elegant", "arrogant", "black-clad"],
    ["masterfully crafted", "beautiful beyond belief", "hypnotic", "fathomless"],
    ["coins", "construction tools", "cranes", "hammers", "deeds to far away mansions"],
    {"market": 1})

districts_no_envy = [lust, gluttony, greed, sloth, wrath, pride]
# populate random things in envy with stolen stuff from all districts
envy.randomstuff = []
for dis in districts_no_envy:
    for thing in dis.randomstuff:
        envy.randomstuff.append(thing)
districts = districts_no_envy + [envy]

#start player in random district
current_district = districts[random.randint(0, 6)]

# FORTOMMY: locations and probabilities by district (between 0 and 1: 0 is impossible, 1 is certain; 0.5 is 50% chance)
class Location:
    def __init__(self, text):
        self.text = text
    def __str__(self):
        rep = self.text
        return rep


market_probabilities = {district.name:district.locations["market"] for district in districts}
def location_maker(current_district, loc_type):
    if  loc_type == "market":
        return Location(
            "You stumble into a {} market. The {} stalls sell {} and {} to the {} patrons.".format(
            random.choice(current_district.location_descriptors),
            random.choice(current_district.location_descriptors),
            random.choice(current_district.randomstuff),
            random.choice(current_district.randomstuff),
            random.choice(current_district.character_descriptors)))

while True: 
    current_location = location_maker(
        current_district,
         loc_type = random.choices(list(current_district.locations.keys()), list(current_district.locations.values()), k = 1)[0])
    print(current_location) 
    next = input("bleh")
