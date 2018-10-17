from choice import Choice
from rock_choice import RockChoice
from paper_choice import PaperChoice
from scissor_choice import ScissorChoice

class ChoiceCreator():
   @classmethod
   def create(cls, val):
      return RockChoice() if val == "r" else PaperChoice() if val == "p" else ScissorChoice()
