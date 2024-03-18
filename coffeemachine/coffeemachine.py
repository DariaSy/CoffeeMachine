import sys

MILK = 'milk'
WATER = 'water'
BEANS = 'beans'
SUGAR = 'sugar'

WATER_CAPACITY_PER_CUP = 200
MILK_CAPACITY_PER_CUP = 50
BEANS_CAPACITY_PER_CUP = 15

ACTION_BUY = 'buy'
ACTION_FILL = 'fill'
ACTION_TAKE = 'take'
ACTION_REMAINING = 'remaining'
ACTION_EXIT = 'exit'

class FillRequest():
    def __init__(self, waterCapacity: int, milkCapacity: int, beansCapacity: int, cupsCapacity: int):
        self.waterCapacity = waterCapacity
        self.milkCapacity = milkCapacity
        self.beansCapacity = beansCapacity
        self.cupsCapacity = cupsCapacity

class CoffeeDrink:
    def __init__(self, number: int, name: str, waterCapacity: int, milkCapacity: int, beansCapacity: int, cashAmount: int):
        self.number = number
        self.name = name
        self.waterCapacity = waterCapacity
        self.milkCapacity = milkCapacity
        self.beansCapacity = beansCapacity
        self.cashAmount = cashAmount

class CoffeeMachine:
    def __init__(self, waterCapacity: int, milkCapacity: int, beansCapacity: int, cupsCapacity: int, cashAmount: int):
        self.waterCapacity = waterCapacity
        self.milkCapacity = milkCapacity
        self.beansCapacity = beansCapacity
        self.cupsCapacity = cupsCapacity
        self.cashAmount = cashAmount

    def __init__(self):
        self.waterCapacity = 400
        self.milkCapacity = 540
        self.beansCapacity = 120
        self.cupsCapacity = 9
        self.cashAmount = 550

    def __str__(self):
        return '{} of water\n{} of milk\n{} of coffee beans\n{} of disposable cups\n{} of money'.format(self.waterCapacity, self.milkCapacity, self.beansCapacity, self.cupsCapacity, self.cashAmount)

def countOfIngeredients(countOfCups: int):
    print('For {} cups you will need:'.format(countOfCups))
    neededWaterCapacity = WATER_CAPACITY_PER_CUP * countOfCups
    neededMilkCapacity = MILK_CAPACITY_PER_CUP * countOfCups
    neededBeansCapacity = BEANS_CAPACITY_PER_CUP * countOfCups
    print('{} ml of {}'.format(neededWaterCapacity, WATER))
    print('{} ml of {}'.format(neededMilkCapacity, MILK))
    print('{} g of {}'.format(neededBeansCapacity, BEANS))

def printHowManyCupsCanBeDone(countOfCups: int, coffeeMachine: CoffeeMachine):
    countOfCupsByWater = coffeeMachine.waterCapacity / WATER_CAPACITY_PER_CUP
    countOfCupsByMilk = coffeeMachine.milkCapacity / MILK_CAPACITY_PER_CUP
    countOfCupsByBeans = coffeeMachine.beansCapacity / BEANS_CAPACITY_PER_CUP
    countOfCupsCanBeDone = int(min(countOfCupsByWater, countOfCupsByMilk, countOfCupsByBeans))
    if (countOfCupsCanBeDone < countOfCups):
        print('No, I can make only {} cups of coffee'.format(countOfCupsCanBeDone))
    else:
        cupDiff = countOfCupsCanBeDone - countOfCups
        if (cupDiff < 1):
            print('Yes, I can make that amount of coffee')
        else:
            print('Yes, I can make that amount of coffee (and even {} more than that)'.format(cupDiff))

def printState(coffeeMachine: CoffeeMachine):
    print('The coffee machine has:')
    print(coffeeMachine)

def buyByCoffeeDrinkNumber(number: int, coffeeMachine: CoffeeMachine):
    if (espresso.number == number):
        buy(espresso, coffeeMachine)
    elif (latte.number == number):
        buy(latte, coffeeMachine)
    elif (cappuccino.number == number):
        buy(cappuccino, coffeeMachine)
    else:
        print('Unknown coffee drink')

def buy(coffeeDrink: CoffeeDrink, coffeeMachine: CoffeeMachine):
    waterAfterDone = coffeeMachine.waterCapacity - coffeeDrink.waterCapacity
    milkAfterDone = coffeeMachine.milkCapacity - coffeeDrink.milkCapacity
    beansAfterDone = coffeeMachine.beansCapacity - coffeeDrink.beansCapacity
    cupsAfterDone = coffeeMachine.cupsCapacity - 1
    cashAfterDone = coffeeMachine.cashAmount + coffeeDrink.cashAmount

    canBeDone = waterAfterDone >= 0 and milkAfterDone >= 0 and beansAfterDone >= 0 and cupsAfterDone >= 0
    if (canBeDone):
        coffeeMachine.waterCapacity = waterAfterDone
        coffeeMachine.milkCapacity = milkAfterDone
        coffeeMachine.beansCapacity = beansAfterDone
        coffeeMachine.cupsCapacity = cupsAfterDone
        coffeeMachine.cashAmount = cashAfterDone
        print('{} is done'.format(coffeeDrink.name))
    else:
        print('Not enough ingredients for {}'.format(coffeeDrink.name))

def fill(fillRequest: FillRequest, coffeeMachine: CoffeeMachine):
    coffeeMachine.waterCapacity += fillRequest.waterCapacity
    coffeeMachine.milkCapacity += fillRequest.milkCapacity
    coffeeMachine.beansCapacity += fillRequest.beansCapacity
    coffeeMachine.cupsCapacity += fillRequest.cupsCapacity

def take(coffeeMachine: CoffeeMachine):
    print('I gave you {}'.format(coffeeMachine.cashAmount))
    coffeeMachine.cashAmount = 0

def remaining(coffeeMachine: CoffeeMachine):
    printState(coffeeMachine)



#waterCapacity = int(input('Write how many ml of water the coffee machine has:\n'))
#milkCapacity = int(input('Write how many ml of milk the coffee machine has:\n'))
#beansCapacity = int(input('Write how many g of beans the coffee machine has:\n'))
#countOfCups = imt(input('Write count of cups:\n'))

espresso = CoffeeDrink(1, 'Espresso', 250, 0, 16, 4)
latte = CoffeeDrink(2, 'Latte', 350, 75, 20, 7)
cappuccino = CoffeeDrink(3, 'Cappucino', 200, 100, 12, 6)
coffeeMachine = CoffeeMachine()

while(True):
    action = input('Write action (buy, fill, take, remaining, exit):')
    if (ACTION_BUY == action):
            coffeeDrinkNumber = int(input('What do you want to buy? {} - {}, {} - {}, {} - {}:'.format(espresso.number, espresso.name, latte.number, latte.name, cappuccino.number, cappuccino.name)))
            buyByCoffeeDrinkNumber(coffeeDrinkNumber, coffeeMachine)
    elif (ACTION_FILL == action):
        fillRequest = FillRequest(
            int(input('Write how many ml of water you want to add:')),
            int(input('Write how many ml of milk you want to add:')),
            int(input('Write how many grams of coffee beans you want to add:')),
            int(input('Write how many disposable coffee cups you want to add:')))
        fill(fillRequest, coffeeMachine)
    elif (ACTION_TAKE == action):
        take(coffeeMachine)
    elif (ACTION_REMAINING == action):
        remaining(coffeeMachine)
    elif (ACTION_EXIT == action):
        sys.exit()
    else:
        print('Unknown action')





#printHowManyCupsCanBeDone(countOfCups, coffeeMachine)

#countOfIngeredients(25)

# print('Starting to make a coffee')
# print('Grinding coffee beans')
# print('Boiling water')
# print('Mixing boiled water with crushed coffee beans')
# print('Pouring coffee into the cup')
# print('Pouring some milk into the cup')
# print('Coffee is ready!')