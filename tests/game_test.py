from lib.game import Game
import lib.console

def test_play_prompts_for_users_option(mocker):
   mocker.patch('lib.console.display')
   mocker.patch('lib.console.display_no_newline')
   mocker.patch('lib.player_input.read_choice')
   mocker.patch('lib.computer_input.read_choice')

   Game.play()

   lib.console.display.assert_any_call("Rock (r), Paper (p) or Scissors (s):")

def test_play_players_choice_is_displayed(mocker):
   mocker.patch('lib.console.display')
   mocker.patch('lib.console.display_no_newline')
   mocker.patch('lib.computer_input.read_choice')
   mocker.patch('lib.player_input.read_choice', return_value="r")

   Game.play()

   lib.console.display.assert_any_call("You played Rock!")

def test_play_players_choice_is_displayed_if_user_picks_other_option(mocker):
   mocker.patch('lib.console.display')
   mocker.patch('lib.console.display_no_newline')
   mocker.patch('lib.computer_input.read_choice')
   mocker.patch('lib.player_input.read_choice', return_value="s")

   Game.play()

   lib.console.display.assert_any_call("You played Scissors!")

def test_play_computers_choice_is_displayed(mocker):
   mocker.patch('lib.console.display')
   mocker.patch('lib.console.display_no_newline')
   mocker.patch('lib.player_input.read_choice')
   mocker.patch('lib.computer_input.read_choice', return_value="p")

   Game.play()

   lib.console.display.assert_any_call("Computer played Paper!")

def test_play_computers_choice_is_displayed_if_computer_picks_other_option(mocker):
   mocker.patch('lib.console.display')
   mocker.patch('lib.console.display_no_newline')
   mocker.patch('lib.player_input.read_choice')
   mocker.patch('lib.computer_input.read_choice', return_value="r")

   Game.play()

   lib.console.display.assert_any_call("Computer played Rock!")

def test_play_states_when_the_computer_wins(mocker):
   mocker.patch('lib.console.display')
   mocker.patch('lib.player_input.read_choice', return_value="s")
   mocker.patch('lib.computer_input.read_choice', return_value="r")

   Game.play()

   lib.console.display.assert_any_call("Computer wins!")

def test_play_states_when_the_player_wins(mocker):
   mocker.patch('lib.console.display')
   mocker.patch('lib.player_input.read_choice', return_value="p")
   mocker.patch('lib.computer_input.read_choice', return_value="r")

   Game.play()

   lib.console.display.assert_any_call("Player wins!")

