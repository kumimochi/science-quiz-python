name = input("Enter your name: ")
n = name.capitalize()
print("Welcome", n, "let's start playing.")

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "How many systems does the body have?\n(a) 12\n(b) 24\n(c) 36\n",
    "How many blood groups are there?\n(a) 2\n(b) 4\n(c) 6\n",
    "How many pairs of chromosomes does a cell have?\n(a) 13\n(b) 23\n(c) 33\n",
    "What is the only body part that can't repair itself?\n(a) Eyes\n(b) Teeth\n(c) Nails\n",
    "What is the largest organ of the body?\n(a) Kidney\n(b) Heart\n(c) Skin\n",
    "What time of the day are we tallest?\n(a) Morning\n(b) Afternoon\n(c) Evening\n",
    "Men can get aroused post mortem\n(a) True\n(b) False\n",
    "What cheese is associated with vivid dreams?\n(a) Cheddar\n(b) Mozzarella\n(c) Blue\n",
    "What is the color of the universe?\n(a) Cosmic Latte\n(b) Cosmic Coffee\n(c) Cosmic Mocha\n",
    "Who have more pain receptors and higher tolerance for pain?\n(a) Men\n(b)Women\n",
    "What is the majority content of Air?\n(a) Oxygen\n(b) Nitrogen\n(c) Hydrogen\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "c"),
    Question(question_prompts[5], "a"),
    Question(question_prompts[6], "a"),
    Question(question_prompts[7], "c"),
    Question(question_prompts[8], "a"),
    Question(question_prompts[9], "b"),
    Question(question_prompts[10], "b"),
]

def quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got", score, "out of", len(questions), ", " n)

quiz(questions)
