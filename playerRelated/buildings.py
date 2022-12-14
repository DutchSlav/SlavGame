class Shop:
    def __init__(self, items: dict) -> None:
        self.itemsList = []
        for i in items:
            self.itemsList.append(i)
        self.items = items
        self.inv = []

    def buy(self, money: int | float) -> int | float:
        print(f'Shopkeeper: Greetings, visitor. What are you interested in today?')
        print(f'Shopkeeper: You can buy these items: {self.itemsList}.')
        item = input('What would you like to buy? ')
        if item in self.items:
            if money >= self.items[item]:
                self.giveItem(item)
                return money - self.items[item]
            else:
                print('Shopkeeper: If you aint\'t buying, get the hell out of here!')
                return money
        else:
            print('Shopkeeper: We don\'t have that in stock.')

    def giveItem(self, item: str) -> None:
        self.inv.append(item)

    def getInv(self) -> list:
        return self.inv

    def addItem(self, name: str, cost: float | int) -> None:
        self.items[name] = cost

    def remItem(self, name: str) -> None:
        del self.items[name]

    def getShop(self) -> dict:
        return self.items
