import console
import player_input
import computer_input
from choice_creator import ChoiceCreator

class Game():
   @classmethod
   def play(cls):
      console.display("Rock (r), Paper (p) or Scissors (s):")

      player_choice = ChoiceCreator.create(player_input.read_choice())
      computer_choice = ChoiceCreator.create(computer_input.read_choice())

      console.display("You played " + str(player_choice) + "!")
      console.display("Computer played " + str(computer_choice) + "!")

      console.display(cls._winning_message(player_choice, computer_choice))

   @classmethod
   def _winning_message(cls, player_choice, computer_choice):
      if player_choice == computer_choice:
         return "It's a tie!"
      elif player_choice.beats(computer_choice):
         return "Player wins!"
      else:
         return "Computer wins!"

if __name__ == "__main__":
   Game.play()
