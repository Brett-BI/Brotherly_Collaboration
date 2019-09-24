import sys

class Axe:

    def __init__(self):
        print("You have my axe!")
        self.base_damage = 30
        self.base_crit_chance = 2
        self.base_hit_chance = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

    def get_base_damage(self):
        return self.base_damage


class Fists:

    def __init__(self):
        print("Give 'em a taste of Thunder and Lightning.")
        self.base_damage = 8
        self.base_crit_chance = 1
        self.base_hit_chance = 1, 2, 3, 4, 5

    def get_base_damage(self):
        return self.base_damage


class Sword:

    def __init__(self):
        print("Stick them with the pointy end.")
        self.base_damage = 25
        self.base_crit_chance = 5
        self.base_hit_chance = 1, 2, 3, 4, 5

    def get_base_damage(self):
        return self.base_damage