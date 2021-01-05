from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    def expenditure(self):
        print(f'Такнь на всю одежду: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3}')

    @abstractmethod
    def abstract(self):
        pass

class Coat(Clothes):
    def expenditure(self):
        print(f'Ткань для пальто: {self.param / 6.5 + 0.5}')

    def abstract(self):
        pass

class Costume(Clothes):
    def expenditure(self):
        print(f'Ткань для костюма: {2 * self.param + 0.3}')

    def abstract(self):
        pass

coat = Coat(200)
coat.expenditure()

costume = Costume(60)
costume.expenditure()