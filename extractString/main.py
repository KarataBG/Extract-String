import re

if __name__ == '__main__':
    extractString = "Welcome to @ISI. If you need any help from HR you can write to @Milo#Minderbinder. For any technical problems you should contact @Major#Major. If you need any smart advises, please contact @Ali#Baba or @John#Yossarian. When you are sick, please stay at #Home."

    res = re.split(" ", extractString)

    for string in res:
        if string.__contains__("@"):
            if string.__contains__("#"):
                print(re.sub(r"[^a-zA-Z0-9 ]", " ", string).strip())
