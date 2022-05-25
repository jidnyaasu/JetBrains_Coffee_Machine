class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):
        self.avl_water = water
        self.avl_milk = milk
        self.avl_beans = beans
        self.avl_cups = cups
        self.avl_money = money
        self.action = None
        self.fill_list = []

    def what_to_do(self, usr_input):
        if self.action != "fill":
            self.fill_list = []
        if usr_input in ["buy", "fill", "remaining", "take"]:
            self.action = usr_input
        if usr_input == "remaining":
            self.print_state()
        if usr_input == "take":
            self.take()
        if self.action == "buy":
            if usr_input == "1":
                self.espresso()
            if usr_input == "2":
                self.latte()
            if usr_input == "3":
                self.cappuccino()
        if self.action == "fill":
            if usr_input not in ["fill", "buy", "remaining", "take"]:
                self.fill_list.append(int(usr_input))
            self.fill()

    def espresso(self):
        if self.avl_water >= 250 and self.avl_beans >= 16 and self.avl_cups >= 1:
            print("I have enough resources, making you a coffee!")
            self.avl_water -= 250
            self.avl_beans -= 16
            self.avl_cups -= 1
            self.avl_money += 4
        else:
            self.not_enough(250, 1, 16)

    def latte(self):
        if self.avl_water >= 350 and self.avl_milk >= 75 and self.avl_beans >= 20 and self.avl_cups >= 1:
            print("I have enough resources, making you a coffee!\n")
            self.avl_water -= 350
            self.avl_milk -= 75
            self.avl_beans -= 20
            self.avl_cups -= 1
            self.avl_money += 7
        else:
            self.not_enough(350, 75, 20)

    def cappuccino(self):
        if self.avl_water >= 200 and self.avl_milk >= 100 and self.avl_beans >= 12 and self.avl_cups >= 1:
            print("I have enough resources, making you a coffee!\n")
            self.avl_water -= 200
            self.avl_milk -= 100
            self.avl_beans -= 12
            self.avl_cups -= 1
            self.avl_money += 6
        else:
            self.not_enough(200, 100, 12)

    def not_enough(self, water, milk, beans):
        if self.avl_water // water == 0:
            print("Sorry, not enough water!\n")
        elif self.avl_milk // milk == 0:
            print("Sorry, not enough milk!\n")
        elif self.avl_beans // beans == 0:
            print("Sorry, not enough beans!\n")
        elif self.avl_cups == 0:
            print("Sorry, not enough disposable cups!\n")

    def fill(self):
        if len(self.fill_list) == 4:
            self.avl_water += self.fill_list[0]
            self.avl_milk += self.fill_list[1]
            self.avl_beans += self.fill_list[2]
            self.avl_cups += self.fill_list[3]

    def take(self):
        print(f"\nI gave you ${self.avl_money}\n")
        self.avl_money = 0

    def print_state(self):
        print(f"The coffee machine has:\n{self.avl_water} of water\n{self.avl_milk} of milk"
              f"\n{self.avl_beans} of beans\n{self.avl_cups} of disposable cups\n${self.avl_money} of money")


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)

while True:
    action = input("Write action (buy, fill, take, remaining, exit):\n")
    if action == "exit":
        break
    if action == "buy":
        coffee_machine.what_to_do(action)
        coffee = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if coffee == "back":
            continue
        else:
            coffee_machine.what_to_do(coffee)
    if action == "fill":
        coffee_machine.what_to_do(action)
        coffee_machine.what_to_do(input("\nWrite how many ml of water you want to add:\n"))
        coffee_machine.what_to_do(input("Write how many ml of milk you want to add:\n"))
        coffee_machine.what_to_do(input("Write how many grams of coffee beans you want to add:\n"))
        coffee_machine.what_to_do(input("Write how many disposable coffee cups you want to add:\n"))
    else:
        coffee_machine.what_to_do(action)
