from zoo import Zoo, Zookeeper, ZooAnnouncer
from animals import Cat, Dragonfly, Lion, Lobster, Ostrich, Tiger, TRex

# Construct and populate Zoo
zoo = Zoo()
zoo.append(Cat("Charles"))
zoo.append(Cat("Chuck"))
zoo.append(Dragonfly("Dave"))
zoo.append(Dragonfly("Donna"))
zoo.append(Lion("Lance"))
zoo.append(Lion("Lily"))
zoo.append(Lobster("Larry"))
zoo.append(Lobster("Lenny"))
zoo.append(Ostrich("Oscar"))
zoo.append(Ostrich("Olive"))
zoo.append(Tiger("Terry"))
zoo.append(Tiger("Tammy"))
zoo.append(TRex("Tony"))
zoo.append(TRex("Toni"))

# Construct Zookeeper and execute routine
zookeeper = Zookeeper(zoo)
zoo_announcer = ZooAnnouncer(zookeeper)
zookeeper.wake()
zookeeper.roll_call()
zookeeper.feed()
zookeeper.exercise()
zookeeper.shut_down()
