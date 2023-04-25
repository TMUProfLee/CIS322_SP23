from testing_base import *

def test_start_game(capsys, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '2')
    start_game()
    captured = capsys.readouterr()
    expected_output = "**************************\n*                        *\n*  Welcome to My Game!   *\n*                        *\n**************************\n\nHow many players would you like to have? "
    assert captured.out == expected_output
