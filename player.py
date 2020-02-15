class Player:

    def __init__(self):
        self.base_health = 100

    def add_health(self, health_amount):
        self.base_health += health_amount

    def remove_health(self, health_amount):
        self.base_health = self.base_health - health_amount

    def get_health(self):
        return self.base_health
