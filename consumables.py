from random import randint
from time import sleep


class HealthPotion:

    def __init__(self):
        print('Hello from Sector Z')

    def use(self):

        while True:

            potion_use = input("Do you want the brotherly JOEtion? Y/N ")
            potion_use = potion_use.lower()

            if potion_use == "y":
                potion_health = randint(10, 30)
                # use the user class to add health here
                self.add_health(potion_health)  # 10, 20, 25, 30, etc.
                print(f"You gained {potion_health} health.")
                sleep(1)
                print(f"You now have {self.get_health()} health.")
                sleep(1)
                break

            elif potion_use == "n":
                break

            else:
                print("Try again")
                continue
