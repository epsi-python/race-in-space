from abc import ABC, abstractmethod
import sys

class Converter(ABC):

    def __init__(self, from_currency, to_currency):
        self.from_currency = from_currency
        self.to_currency = to_currency

    @abstractmethod
    def convert(self, amount) -> float:
        pass

class App:
    def __init__(self, converter : Converter):
        self.converter = converter
        
    def start(self):
        for line in sys.stdin:
            self.converter.convert(int(line))
            break

class SelectConverter:
    @classmethod
    def get_choice(cls):
        print("1. FXConverter")
        print("2. USDConverter")
        for line in sys.stdin:
            try:
                choice = int(line)
            except:
                print("Wrong selection")
                choice = 0
            return cls.get_converter(choice)
            
    @classmethod
    def get_converter(cls,choice) -> Converter:
        if (choice == 1):
            return FXConverter()
        if (choice == 2):
            return USDConverter()


class FXConverter(Converter):
    def __init__(self):
        super().__init__('EUR', 'PIG')

    def convert(self, amount):
        print(f'FXConverter: {amount} {self.from_currency} = {amount * 1.2} {self.to_currency}')
        return amount * 1.2

class USDConverter(Converter):
    def __init__(self):
        super().__init__('EUR', 'USD')

    def convert(self, amount):        
        print(f'USDConverter: {amount} {self.from_currency} = {amount * 1.34} {self.to_currency}')
        return amount * 1.34

if __name__ == '__main__':
    converter = FXConverter()
    app = App(converter)
    app.start()
    app.converter = USDConverter()
    app.start()