# Base Class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def show_identity(self):
        print(f"{self.name} is a superhero from {self.origin} with the power of {self.power}!")

    def attack(self):
        print(f"{self.name} uses {self.power} to fight evil! ⚡")


# Subclass (Inheritance + Polymorphism Example)
class TechHero(Superhero):
    def __init__(self, name, power, origin, gadget):
        super().__init__(name, power, origin)
        self.gadget = gadget

    def attack(self):
        print(f"{self.name} uses their {self.gadget} and {self.power} to save the day! 💻")

# Another Subclass
class MagicHero(Superhero):
    def __init__(self, name, power, origin, spell):
        super().__init__(name, power, origin)
        self.spell = spell

    def attack(self):
        print(f"{self.name} casts {self.spell} with their {self.power}! ✨")


# Example Usage
iron_byte = TechHero("IronByte", "Tech Genius", "Cyber City", "Smart Gauntlet")
arcana = MagicHero("Arcana", "Mystic Arts", "Eldoria", "Firestorm")

iron_byte.show_identity()
iron_byte.attack()

arcana.show_identity()
arcana.attack()
