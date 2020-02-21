from abc import ABC, abstractmethod
from random import randint
import behaviors as b


class Animal(ABC):
    """
    Main superclass for all animals.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize an Animal object. _type to be initialized by subclasses.

        param:

        name (str): Animal's name
        """

        self._name = name
        self._type = None
        self._awake = False
        self._noise_behavior = None

    def get_name(self) -> str:
        """
        Name accessor.

        return:

        name (str): Animal's name
        """

        return self._name

    def get_type(self) -> str:
        """
        Type accessor.

        return:

        type (str): Type of animal (defined in subclass)
        """

        return self._type

    def is_awake(self) -> bool:
        """
        Gets current awake status of animal.

        return:

        awake (bool): If awake, True
        """

        return self._awake

    def get_full_name(self) -> str:
        """
        Returns the animal's full name in the form "[Animal] the [Type]".

        return:

        full_name (str): Full name of the animal
        """

        return f'{self.get_name()} the {self.get_type()}'

    def do_action(self, action: str) -> None:
        """
        Prints that the animal has done a specific action. If the animal is
        asleep, simply prints that information.

        param:

        action (str): the end of the sentence after full_name
        """

        if not self.is_awake():
            action = 'is asleep!'
        print(f'{self.get_full_name()} {action}')

    def wake_up(self) -> None:
        """
        Sets the animal's status to awake and reports this. If the animal is
        awake, prints that information.
        """

        if not self.is_awake():
            self._awake = True
            self.do_action('wakes up.')
        else:
            self.do_action('is already awake!')

    def perform_noise(self) -> None:
        """
        Perform the noise behavior (strategy pattern). Must have full name to
        print properly.
        """

        self._noise_behavior.make_noise(self.get_full_name())

    @abstractmethod
    def eat(self) -> None:
        """
        Abstract method for eating behavior
        """

        pass

    @abstractmethod
    def roam(self) -> None:
        """
        Abstract method for roaming behavior
        """

        pass

    def sleep(self) -> None:
        """
        Reports that the animal is going to sleep and then sets the animal's
        status to asleep. (Through do_action, will report if already asleep)
        """

        if self.is_awake():
            self.do_action('goes to sleep.')
            self._awake = False
        else:
            self.do_action('')


class Invertebrate(Animal):
    """
    Superclass for Invertebrates
    """

    def __init__(self, name):
        """
        Constructs an invertebrate with appropriate noise behavior (strategy
        pattern)
        """

        super().__init__(name)
        self._noise_behavior = b.Silence()


class Dragonfly(Invertebrate):
    """
    Specific Dragonfly class
    """

    def __init__(self, name):
        """
        Construct a Dragonfly
        """

        super().__init__(name)
        self._type = 'Dragonfly'

    def eat(self):
        """
        Dragonfly-specific eating behavior
        """

        self.do_action('eats some mosquitoes.')

    def roam(self):
        """
        Dragonfly-specific roaming behavior
        """

        self.do_action('flutters about.')


class Lobster(Invertebrate):
    """
    Specific Lobster class
    """

    def __init__(self, name):
        """
        Constructs a Lobster
        """

        super().__init__(name)
        self._type = 'Lobster'

    def eat(self):
        """
        Lobster-specific eating behavior
        """

        self.do_action('eats some fish.')

    def roam(self):
        """
        Lobster-specific roaming behavior
        """

        self.do_action('scuttles around.')


class Reptile(Animal):
    """
    Superclass for Reptiles
    """

    def roam(self):
        """
        Reptile-specific roaming behavior
        """

        self.do_action('prances about.')


class Ostrich(Reptile):
    """
    Specific Ostrich class
    """

    def __init__(self, name):
        """
        Construct an ostrich with specific noise (strategy pattern)
        """

        super().__init__(name)
        self._type = 'Ostrich'
        self._noise_behavior = b.Hoot()

    def eat(self):
        """
        Ostrich-specific eating behavior
        """

        self.do_action('eats some seeds.')


class TRex(Reptile):
    """
    Specific TRex class
    """

    def __init__(self, name):
        """
        Construct a TRex with specific noise (strategy pattern)
        """

        super().__init__(name)
        self._type = 'T. rex'
        self._noise_behavior = b.Roar()

    def eat(self):
        """
        TRex-specific eating behavior
        """

        self.do_action('eats a steak.')


class Feline(Animal):
    """
    Superclass for Felines
    """

    def act(self) -> None:
        """
        Method to be called for sleeping, roaming, and noisemaking for all
        Felines. Randomly does one of the three. The non-overriden noise
        behavior is called here. (strategy pattern)
        """

        val = randint(0, 2)
        if val == 0:
            self.sleep()
        elif val == 1:
            self.actually_roam()
        elif val == 2:
            super().perform_noise()

    def actually_roam(self) -> None:
        """
        Abstract method for _actual_ roaming behavior for Felines, as opposed
        to the inherited method which results in random behavior.
        """

        self.do_action('runs around.')

    def roam(self) -> None:
        """
        Feline-specific (random) roaming behavior
        """

        self.act()

    def perform_noise(self) -> None:
        """
        Feline-specific (random) noisemaking behavior
        """

        self.act()

    def sleep(self) -> None:
        """
        Feline-specific (random) sleeping behavior
        """

        self.act()


class Cat(Feline):
    """
    Specific Cat class
    """

    def __init__(self, name):
        """
        Constructs a cat
        """

        super().__init__(name)
        self._type = 'Cat'
        self._noise_behavior = b.Hiss()

    def eat(self) -> None:
        """
        Cat-specific eating behavior
        """

        self.do_action('eats some cat food.')


class Lion(Feline):
    """
    Specific Lion class
    """

    def __init__(self, name):
        """
        Constructs a Lion
        """

        super().__init__(name)
        self._type = 'Lion'
        self._noise_behavior = b.Roar()

    def eat(self):
        """
        Lion-specific eating behavior
        """

        self.do_action('eats a zebra.')


class Tiger(Feline):
    """
    Specific tiger class
    """

    def __init__(self, name):
        """
        Constructs a tiger
        """

        super().__init__(name)
        self._type = 'Tiger'
        self._noise_behavior = b.Roar()

    def eat(self):
        """
        Tiger-specific eating behavior
        """

        self.do_action('eats an antelope.')
