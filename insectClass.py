import random

# The insect class simulates an insect with wings and legs


class Insect:
    def __init__(self):
        self.wings = "long"
        self.legs = "long"

    def wings(self):
        if random.randint(0, 1) == 0:
            self.wings = "long"
        else:
            self.wings = "short"

    def legs(self):
        if random.randint(0, 3) == 0:
            self.legs = "long"
        else:
            self.legs = "short"

    def flight_length(self):
        return self.wings
