import random
import colors
import os
os.system('color')

def loadfile():
    words = []
    with open("test.txt", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split('] [')
            if len(parts) == 3:
                en = parts[0].replace('[', '').strip()
                trans = parts[1].strip()
                ru = parts[2].replace(']', '').strip()
                words.append([en, trans, ru])
    print("Words loaded:", len(words))
    return words

words = loadfile()
if words == []:
    print("File is empty")
    exit(0)

random.shuffle(words)
right = 0
total = min(10, len(words))

for i in range(total):
    en, trans, ru = words[i]
    print(f"\n{i + 1}. {ru} ({trans})")
    ans = input("Answer: ").strip()

    if ans.lower() == en.lower():
        print(colors.green("Right"))
        right += 1
    else:
        print(colors.red("Wrong"))
        print(f"Correct answer: {colors.blue(ru)}")

print(f"\nИтого: {right}/{total}")
