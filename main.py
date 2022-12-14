from gameRelated import game, saveHandler
from playerRelated import player, buildings

started = False
info = None
stats = player.Stats()
events = player.Event()
money = player.Money()
shop = buildings.Shop({'rock': 5, 'shovel': 10})
dataSave = {}
# noinspection PyBroadException
try:
    saveData = saveHandler.load()
    if saveData is not {}:
        for data in saveData:
            if data == 'money':
                money.setMoney(saveData[data])
            elif data == 'items':
                for item in saveData[data]:
                    shop.giveItem(item)
            elif data == 'name':
                info = player.Info(saveData[data])
            elif data == 'started':
                started = saveData[data]
except:
    exit(2)

if info is None:
    info = player.Info(input("What is your name? "))

if started is not True:
    started = game.start(info.getName())
    game.intro(info.getName())
# Game Loop
while True:
    money.setMoney(30)
    saveHandler.save({'money': money.getMoney(), 'items': shop.getInv(), 'name': info.getName(), 'started': started})
    break
