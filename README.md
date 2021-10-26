# intro-to-github
This is a demo repository to practice using GitHub.

It has two files in the **Code** tab:
- **README.md** is a file that describes this repo (you are currently reading it)
- **.gitignore** is a file that specifies which files and directories must be ignored by Git

You cannot directly modify files in this repo because you are not a *collaborator*.

The **Issues** tab is used to discuss ideas, enhancements, bugs, questions, and so on. They are grouped by *Open* and *Closed*.

The **Pull requests** tab contains proposals to make some changes in the files located in the repository. Repo's owners may review a request and put your changes if they look good.

You can create an *Issue* or make a *Pull request (PR)* to contribute to the project.

If you want to propose some changes to this repo, you may *fork* it, modify the content, and create *PR*. A *fork* is just a copy that allows you to change the content without affection the original project.
def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    # write your code here
    print("What language was named after TV series ?")
    print("""
1. JAVA
2. PYTHON
3. HTML
4. JAVA SCRIPT """)
    asd = 2
    while True:
        answer = int(input())
        if answer == asd:
            break
        else:
            print("Please, try again.")

def end():
    print('Congratulations, have a nice day!')


greet('Aid', '2020')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
