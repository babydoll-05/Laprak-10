filename = input("nama file1: ")

def load_questions(filename):
    questions = []
    with open(filename, 'r') as file:
        for line in file:
            question, answer = line.strip().split(" || ")
            questions.append((question, answer))
    return questions

questions = load_questions(filename)
for i, (question, answer) in enumerate(questions, 1):
    print(f"{i}. {question}")
    user_answer = input("Jawab: ").strip().lower()
    if user_answer == answer.lower():
        print("Jawaban benar!")
    else:
        print("Jawaban salah!")