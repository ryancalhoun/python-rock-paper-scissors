from choice import Choice

class PaperChoice(Choice):
   def __init__(self):
      super(PaperChoice, self).__init__("p", ["s"])

   def __str__(self):
      return "Paper"

