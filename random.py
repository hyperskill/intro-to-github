import random
def chooseFastFood(numOptions):
    listOfFastFood = ['Taco Bell', 'Panda Express', 'In-N-Out', 'Habit Burger', 'Chipotle', 'Five Guys', 'Burger King', 'Wendys', 'McDonalds',
                      'Jack in the Box', 'Carls Jr.', 'Subway']
    chosen = []
    if numOptions < len(listOfFastFood):
        for i in range(numOptions):
            chosen.append(random.choice(listOfFastFood))
        return chosen
    else:
        return "You requested too many options."

def main():
    num_str = input("How many options of fast food places would you like? ")
    print(chooseFastFood(int(num_str)))

if __name__ == '__main__':
    main()
