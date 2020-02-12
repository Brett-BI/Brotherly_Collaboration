import sys
import pygame
# import pygame.freetype
# import pygame.font

from time import sleep
from random import choice, randint

import consumables
import weapons
from player import Player


# create a player object instead of user
# create separate instances of player with specific names - set abilities based on names or types or something...
# also import the user module 
# make objects of weapons some how.
# wuggob


class GameSequence:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the beginning of the game"""
        pygame.init()

        # New instances of both the player and computer
        self.player = Player()
        self.computer = Player()

        # Set the default weapon for each player to fists
        self.weapon = weapons.Fists()

        self.weapon_choice()

    def weapon_choice(self):
        # User picks a weapon for the game
        weapon_choice = True

        while weapon_choice:
            weapon_choice = input("\nChoose a weapon. Do you want an axe or a sword: ")
            weapon_choice = weapon_choice.lower()

            if weapon_choice == "axe":
                self.weapon = weapons.Axe()
                print(f"\nYou chose the {weapon_choice}.")
                print(f"The {weapon_choice} has up to {self.weapon.get_base_damage()} damage.")
                weapon_choice = False
                self.combat_series()

            elif weapon_choice == "sword":
                self.weapon = weapons.Sword()
                print(f"\nYou chose the {weapon_choice}.")
                print(f"The {weapon_choice} has up to {self.weapon.get_base_damage()} damage.")
                weapon_choice = False
                self.combat_series()

            else:
                print("\nThat isn't a choice.")
                continue

    def combat_series(self):

        while True:
            defense_choice = ["blocked", "parried"]
            # blocked = .25 * damage caused
            # parried = .75 * damage caused
            attack = input("\nEnter A to attack: ")
            attack = attack.lower()

            if attack == "a":
                print("You attacked!")
                sleep(1)
                hit_chance = choice(self.axe_hit_chance)

                if hit_chance != 1:
                    print("You hit!")
                    sleep(1)
                    crit = randint(1, 1)

                    if crit == 1:
                        print("You had a critical strike!")
                        sleep(1)
                        crit_damage = (randint(10, 30) + 15)

                        print(f"You hit for {crit_damage} critical damage!")
                        sleep(1)
                        self.computer.remove_health(crit_damage)
                        print(f"The computer now has {self.computer.get_health()} health.\n")
                        sleep(2)

                        if self.computer.get_health() <= 0:
                            self.computer_loss()

                        else:
                            print("The computer is about to attack!")
                            sleep(1)

                            user_defense = randint(1, 1)

                            if user_defense != 1:
                                computer_attack_damage = randint(1, 5)
                                print(f"The computer hit you for {computer_attack_damage} damage!")
                                sleep(1)
                                self.player.remove_health(computer_attack_damage)
                                print(f"You now have {self.player.get_health()} health remaining.")
                                sleep(1)

                                if self.player.get_health() <= 0:
                                    self.user_loss()

                                elif 70 >= self.player.get_health() > 0:
                                    consumables.health_potion.use(self.player)

                            else:
                                defense = choice(defense_choice)
                                print(f"You {defense}!")
                                continue

                    elif crit != 1:
                        damage = randint(1, 30)
                        print(f"You hit for {damage}.")
                        sleep(1)
                        self.computer.remove_health(damage)
                        print(f"The computer now has {self.computer.get_health()} health.\n")
                        sleep(2)

                        if self.computer.remove_health(damage) <= 0:
                            self.computer_loss()

                        else:
                            print("The computer is about to attack!")
                            sleep(1)
                            computer_attack_damage = randint(10, 25)
                            print(f"The computer hit you for {computer_attack_damage} damage!")
                            sleep(1)
                            self.player.remove_health(computer_attack_damage)
                            print(f"You now have {self.player.get_health()} health remaning.")
                            sleep(1)

                            if self.player.get_health() <= 0:
                                self.user_loss()

                            elif 70 >= self.player.get_health() > 0:
                                consumables.health_potion.use(self.player)
                                continue

                            else:
                                continue

                else:
                    print("You missed!")
                    sleep(1)

                    print("The computer is about to attack!")
                    sleep(1)
                    computer_attack_damage = randint(100, 130)
                    print(f"The computer hit you for {computer_attack_damage} damage!")
                    sleep(1)
                    self.user_remove_health(computer_attack_damage)
                    print(f"You now have {player.get_health()} health remaning.")
                    sleep(1)

                    if self.player.get_health() <= 0:
                        self.user_loss()

                    elif 70 >= self.player.get_health() > 0:
                        consumables.health_potion.use(self.player)

                    else:
                        continue

            else:
                print("Try again.")
                continue

    def computer_loss(self):

        print("\nYou win!")
        sleep(2)

        while True:

            play_again = input("Play again? Y/N: ")
            play_again = play_again.lower()

            if play_again == "y":
                self.weapon_choice()

            elif play_again == "n":
                sys.exit()

            else:
                print("Choose Y or N.\n")
                continue

    def user_loss(self):

        print("\nYou lose!")
        sleep(2)

        while True:

            play_again = input("Play again? Y/N: ")
            play_again = play_again.lower()

            if play_again == "y":
                self.weapon_choice()

            elif play_again == "n":
                sys.exit()

            else:
                print("Choose Y or N.\n")
                continue


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = GameSequence()
    ai.run_game()
