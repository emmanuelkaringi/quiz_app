import random
from string import ascii_lowercase

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS = {
    "How old was Sheldon when he got his first P.h.d?": [
        "16",
        "18",
        "20",
        "22",
    ],
    "What’s Amy’s job": [
        "Neurobiologist",
        "Marine biologist",
        "Forensic biologist",
        "Microbiologist",
    ],
    "Which couple gets married first?": [
        "Bernadette and Howard",
        "Penny and Leonard",
        "Amy and Sheldon",
        "Emily and raj",
    ],
    "What is Leonard primary health concern?": [
        "He is lactose intolerant",
        "He is allergic to peanuts",
        "He has to eat gluten free",
        "He has diabetes",
    ],
    "Who does Howard meet while serving Thanksgiving dinner at a shelter?": [
        "Elon Musk",
        "Jeff Bezos",
        "Bill Gates",
        "Steve Jobs",
    ]
}

num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS))
questions = random.sample(list(QUESTIONS.items()), k=num_questions)

num_correct = 0
for num, (question, alternatives) in enumerate(questions, start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(
        zip(ascii_lowercase, random.sample(alternatives, k=len(alternatives)))
    )
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    answer = labeled_alternatives[answer_label]
    if answer == correct_answer:
        num_correct += 1
        print("⭐ Correct! ⭐")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

print(f"\nYou got {num_correct} correct out of {num} questions")