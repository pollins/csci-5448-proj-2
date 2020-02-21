from abc import ABC, abstractmethod


class NoiseBehavior(ABC):
    """
    This the encapsulated noise behavior for the implementation of the
    strategy pattern. This class acts as an interface.
    """

    @abstractmethod
    def make_noise(self, full_name):
        """
        Abstract noisemaking behavior method
        """

        pass


class Roar(NoiseBehavior):
    """
    Behavior for roaring animals
    """

    def make_noise(self, full_name):
        """
        Roar noise behavior
        """

        print(f'{full_name} roars.')


class Silence(NoiseBehavior):
    """
    Behavior for silent animals
    """

    def make_noise(self, full_name):
        """
        Silence behavior
        """

        print(f'{full_name} is silent.')


class Hoot(NoiseBehavior):
    """
    Behavior for hooting animals
    """

    def make_noise(self, full_name):
        """
        Hooting behavior
        """

        print(f'{full_name} hoots.')


class Hiss(NoiseBehavior):
    """
    Behavior for hissing animals
    """

    def make_noise(self, full_name):
        """
        Hissing behavior
        """

        print(f'{full_name} hisses.')
