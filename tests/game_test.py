from lib.game import Game
import lib.console

def test_play(mocker):
   mocker.patch('lib.console.display')

   Game().play()

   lib.console.display.assert_called_once_with("Let's play a game!")

