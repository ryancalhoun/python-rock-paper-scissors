from lib.choice_creator import ChoiceCreator

def test_strifiy():
   assert "Rock" == str(ChoiceCreator.create("r"))
   assert "Scissors" == str(ChoiceCreator.create("s"))
   assert "Paper" == str(ChoiceCreator.create("p"))

def test_paper_beats_rock():
   assert ChoiceCreator.create("p").beats(ChoiceCreator.create("r")) == True
   assert ChoiceCreator.create("r").beats(ChoiceCreator.create("p")) == False

def test_rock_beats_scissors():
   assert ChoiceCreator.create("s").beats(ChoiceCreator.create("p")) == True
   assert ChoiceCreator.create("s").beats(ChoiceCreator.create("r")) == False

def test_scissors_beats_paper():
   assert ChoiceCreator.create("s").beats(ChoiceCreator.create("p")) == True
   assert ChoiceCreator.create("p").beats(ChoiceCreator.create("s")) == False

