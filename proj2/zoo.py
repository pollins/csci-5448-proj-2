from abc import ABC, abstractmethod


class Zoo:
    """
    Class for a Zoo of animals. Functions as a list, and is both iterator and
    iterable.
    """

    def __init__(self):
        """
        Construct a Zoo
        """

        self._animals = []

    def append(self, animal):
        """
        Add an animal to the Zoo

        param

        animal (Animal): Animal to add
        """

        self._animals.append(animal)

    def __iter__(self):
        """
        Implementing protocol for iterator
        """

        return iter(self._animals)

    def __next__(self):
        """
        Makes class iterable
        """

        return next(self)


class Subject(ABC):
    """
    Subject interface for Observer pattern, taken from Freeman et al.
    """

    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class Observer(ABC):
    """
    Observer interface for Observer pattern, from Freeman et al.
    """

    @abstractmethod
    def update(self, action):
        pass


class Zookeeper(Subject):

    def __init__(self):
        """
        Construct a Zookeeper with Observer list for Observer pattern
        """

        self._observers = []
        self._action = None

    def set_action(self, action):
        """
        Set Zookeeper's current action
        """

        self._action = action
        self.action_changed()

    def action_changed(self):
        """
        Carry out commands for when action is changed
        """

        self.notify_observers()

    def do_action(self, action):
        """
        Prints what the zookeeper does, given the predicate of the sentence

        param:

        action (str): end of sentence
        """
        self.set_action(action)
        print(f'The zookeeper is {action}')

    def wake(self, zoo):
        """
        Wake the Animals in a Zoo

        param:

        zoo (Zoo): Zoo in which to do the action
        """

        self.do_action('waking the animals.')
        for animal in zoo:
            animal.wake_up()

    def roll_call(self, zoo):
        """
        Call roll for the Animals in a Zoo

        param:

        zoo (Zoo): Zoo in which to do the action
        """

        self.do_action('calling roll.')
        for animal in zoo:
            animal.perform_noise()

    def feed(self, zoo):
        """
        Feed the animals in a Zoo

        param:

        zoo (Zoo): Zoo in which to do the action
        """

        self.do_action('feeding the animals.')
        for animal in zoo:
            animal.eat()

    def exercise(self, zoo):
        """
        Exercise the animals in a Zoo

        param:

        zoo (Zoo): Zoo in which to do the action
        """

        self.do_action('exercising the animals.')
        for animal in zoo:
            animal.roam()

    def shut_down(self, zoo):
        """
        Put all the animals to sleep

        param:

        zoo (Zoo): Zoo in which to do the action
        """

        self.do_action('shutting down the zoo.')
        for animal in zoo:
            animal.sleep()

    # these methods from Freeman et al.
    def register_observer(self, observer):
        """Method for observer pattern, add observer to list"""

        self._observers.append(observer)

    def remove_observer(self, observer):
        """For observer pattern, remove observer from list"""
        
        i = self._observers.index(observer)
        if i >= 0:
            self._observers.remove(self._observers[i])

    def notify_observers(self):
        """Notify subscribed observers of action"""

        for observer in self._observers:
            observer.update(self._action)


class ZooAnnouncer(Observer):
    """Zoo Announcer class for observer pattern, announces actions of
    observer"""

    def __init__(self, zookeeper):
        """
        Constructor for Zoo Announcer, registers to observer list of Zookeeper
        """

        self._action = None
        self._zookeeper = zookeeper
        self._zookeeper.register_observer(self)

    def __del__(self):
        """
        Destructor as prescribed for observer
        """

        self._zookeeper.remove_observer(self)

    def update(self, action):
        """
        Observer update method, changes action and announces, from Freeman et
        al.
        """

        self._action = action
        self.announce()

    def announce(self):
        """
        Prints activity of publisher zookeeper
        """

        print(f'This is the Zoo Announcer. The zookeeper will now be {self._action}')

# Eric Freeman et al. Head First Design Patterns. 2004.
