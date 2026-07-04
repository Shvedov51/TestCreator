import random
import colors
import os
os.system('color')

engLang = 1;

def loadfile(name_file):
    words = []
    with open(name_file, encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split('] [')
            if len(parts) == 3:
                en = parts[0].replace('[', '').strip()
                trans = parts[1].strip()
                ru = parts[2].replace(']', '').strip()
                words.append([en, trans, ru])
    print("Words loaded:", len(words))
    return words

while True:
    print("1. Tests")
    print("2. Settings")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 3:
        break
    if choice == 2:
        os.system('cls')
        print("Question in:")
        print("1. English(default)")
        print("2. Russian")
        engLang = int(input("Enter your choice:"))
    if choice == 1:
        os.system('cls')
        print("Enter a name file like <test.txt>")
        name_file = input()
        words = loadfile(name_file)
        if words == []:
            print("File is empty")
            exit(0)

        random.shuffle(words)
        right = 0
        total = min(10, len(words))

        for i in range(total):
            en, trans, ru = words[i]

            if(engLang == 1):
                question = en
                answer = ru
            else:
                question = ru
                answer = en

            print(f"\n{i + 1}. {question} ({trans})")
            ans = input("Answer: ").strip()

            if ans.lower() == answer.lower():
                print(colors.green("Right"))
                right += 1
            else:
                print(colors.red("Wrong"))
                print(f"Correct answer: {colors.blue(answer)}")

        print(f"\nTotal: {right}/{total}")
        choice = 0
        continue













