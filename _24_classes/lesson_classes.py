class Ork:
    def __init__(self, level: int) -> None:
        self.level = level
        self.health_points = 100 * level
        self.attack_power = 100 * level

    def attack(self):
        print(f"Ork attack with {self.attack_power} power")
ork = Ork(level=2)
print(ork.attack_power)
ork.attack()


class Mans:
    def __init__(self, level: int) -> None:
        self.level = level
        self.health_points = 100 * level
        self.attack_power = 100 * level

    def attack_1(self):
        print(f"Ork attack with {self.attack_power} power")

    def __str__(self):
        return f"Mans (level:{self.level}), hp:{self.health_points}"
mans = Mans(level=1)
print(mans)
