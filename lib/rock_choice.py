from choice import Choice

class RockChoice(Choice):
   def __init__(self):
      super(RockChoice, self).__init__("r", ["p"])

   def __str__(self):
      return "Rock"

