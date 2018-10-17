import lib.computer_input
import random

def test_should_seed_randomness(mocker):
   mocker.patch("random.seed")
   mocker.patch("random.randint", return_value=0)

   lib.computer_input.read_choice()

   assert random.seed.called

def test_should_get_correct_random_integer(mocker):
   mocker.patch("random.seed")
   mocker.patch("random.randint", return_value=0)

   lib.computer_input.read_choice()

   random.randint.assert_called_with(0, 2)

def test_read_choice_should_return_back_r_or_s_or_p(mocker):
   mocker.patch("random.randint", return_value=0)
   result = lib.computer_input.read_choice()
   assert result == "r"

   mocker.patch("random.randint", return_value=1)
   result = lib.computer_input.read_choice()
   assert result == "p"

   mocker.patch("random.randint", return_value=2)
   result = lib.computer_input.read_choice()
   assert result == "s"
