import random

class Coin:

    def __init__(self, big=False, clean=True, heads=True, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.big = big
        self.clean = clean
        self.heads = heads

        if big:
            self.value = self.original_value*2
        else:
            self.value = self.original_value

        if clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color

    def rust(self):
        self.color = self.rusty_color

    def clean(self):
        self.color = self.clean_color

    def __del__(self):
        return "coin spent!"

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __str__(self):
        return "{}Rs coin".format(int(self.original_value))


class One_Rupee(Coin):

    def __init__(self):
        data = {
            "original_value": 1,
            "clean_color": "bronze",
            "rusty_color": "brownish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5
        }
        super().__init__(**data)

class Two_Rupees(Coin):

    def __init__(self):
        data = {
            "original_value": 2,
            "clean_color": "golden",
            "rusty_color": "yellowish",
            "num_edges": 1,
            "diameter": 24.5,
            "thickness": 3.75,
            "mass": 11.5
        }
        super().__init__(**data)

class Five_Rupees(Coin):

    def __init__(self):
        data = {
            "original_value": 5,
            "clean_color": "silver",
            "rusty_color": None,
            "num_edges": 1,
            "diameter": 26.5,
            "thickness": 4.25,
            "mass": 13.5
        }
        super().__init__(**data)

    def rust(self):
        self.color = self.clean_color

    def clean(self):
        self.color = self.clean_color


class Ten_Rupees(Coin):

    def __init__(self):
        data = {
            "original_value": 10,
            "clean_color": "silver",
            "rusty_color": None,
            "num_edges": 1,
            "diameter": 28.5,
            "thickness": 4.65,
            "mass": 15.5
        }
        super().__init__(**data)

    def rust(self):
        self.color = self.clean_color

    def clean(self):
        self.color = self.clean_color

coins = [One_Rupee(), Two_Rupees(), Five_Rupees(), Ten_Rupees()]

for coin in coins:
    arguments = [coin, coin.color, coin.value, coin.diameter, coin.thickness,
                 coin.num_edges, coin.mass]

    string = "{} - color:{}, value(Rs):{}, diameter(mm):{}, thickness(mm):{} ," \
             "num_edges:{}, mass(gm):{}".format(*arguments)

    print(string)