import random
import colors
import os
import time
os.system('color')

engLang = 1 # 1 - any, 2 - Russian
resolved_words = 0
mistakes = 0

def find_tc_files():
    files = []
    for file in os.listdir('.'):
        if file.endswith('.ctest'):
            files.append(file)
    return files


def loadfile(name_file):
    words = []

    if not os.path.exists(name_file):
        print(colors.red("Files not found! Use .ctest format: [word] [transcription] [translation]"))
        return words

    try:
        with open(name_file, encoding="utf-8") as f:
            for line in f:
                p = line.strip().split('] [')
                if len(p) == 3:
                    w = p[0].replace('[', '').strip()
                    t = p[1].strip()
                    r = p[2].replace(']', '').strip()
                    if w and r:
                        words.append([w, t, r])
    except:
        print(colors.red("Error to open file!"))
        return words

    print(colors.green(f"Loaded {len(words)} words"))
    return words

def settingsTab():
    os.system('cls')
    print("Question in:")
    global engLang
    if engLang == 1:
        print("1. Any language" + " (current)")
        print("2. Russian")
    else:
        print("1. Any language")
        print("2. Russian" + " (current)")

    while True:
        user_input = input("Enter your choice: ")
        if user_input == "":
            break
        engLang = int(user_input)
        if engLang in [1, 2]:
            break
        else:
            print("Invalid choice!")

def testTab():
    os.system('cls')
    tests = find_tc_files()

    for i, test in enumerate(tests, 1):
        print(f"{i}. {test}")
    test_number = int(input("Enter number of file:"))
    os.system('cls')

    if 1 <= test_number <= len(tests):
        selected_file = tests[test_number - 1]
        print(f"Selected: {selected_file}")
    else:
        print("Invalid number!")
        return

    words = loadfile(selected_file)
    start_time = time.time()
    if words == []:
        print("File is empty")
        exit(0)
    print(colors.blue("Enter <exit> to quit"))

    random.shuffle(words)
    global resolved_words
    global mistakes

    right = 0
    wrong_words = []
    total = min(20, len(words))

    for i in range(total):
        en, trans, ru = words[i]

        if (engLang == 1):
            question = en
            answer = ru
        else:
            question = ru
            answer = en

        print(f"\n{i + 1}. {question} ({trans})")
        ans = input("Answer: ").strip()

        if ans == 'exit':
            break

        resolved_words += 1

        if ans.lower() == answer.lower():
            print(colors.green("Right"))
            right += 1
        else:
            print(colors.red("Wrong"))
            print(f"Correct answer: {colors.blue(answer)}")
            wrong_words.append([en, trans, ru])
            mistakes += 1

    end_time = time.time()
    total_time = end_time - start_time
    print(f"\nTotal: {right}/{total} {right/total*100:.1f}% {total_time:.2f}s")
    print("Do u wanna resolve only mistakes?")
    print("y - yes, n - no")
    if input() == "y":
        os.system('cls')
        total = min(20, len(wrong_words))

        for i in range(total):
            en, trans, ru = wrong_words[i]

            if (engLang == 1):
                question = en
                answer = ru
            else:
                question = ru
                answer = en

            print(f"\n{i + 1}. {question} ({trans})")
            ans = input("Answer: ").strip()

            if ans == 'exit':
                break


            if ans.lower() == answer.lower():
                print(colors.green("Right"))
                right += 1
            else:
                print(colors.red("Wrong"))
                print(f"Correct answer: {colors.blue(answer)}")



    choice = 0
    return

def statTab():
    os.system('cls')
    print("Stats of this session")
    print(f"Learned words: {colors.green(resolved_words)}")
    print(f"Mistakes: {colors.red(mistakes)}")
    os.system('pause')

def main():
    while True:
        print("1. Tests")
        print("2. Settings")
        print("3. Statistic")
        print("4. Exit")
        user_input = input("Enter your choice: ")

        if user_input == "":
            continue

        if not int(user_input) in [1, 2, 3, 4]:
            continue

        choice = int(user_input)

        if choice == 4:
            exit()
        if choice == 3:
            statTab()
        if choice == 2:
            settingsTab()
        if choice == 1:
            testTab()

if __name__ == "__main__":
    main()