from choice import Choice

class ScissorChoice(Choice):
   def __init__(self):
      super(ScissorChoice, self).__init__("s", ["r"])

   def __str__(self):
      return "Scissors"

