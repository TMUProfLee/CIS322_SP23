from testing_base import *

def test_start_game(capsys, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '2')
    start_game()
    captured = capsys.readouterr()
    expected_output = "**************************\n*                        *\n*  Welcome to Go Fish    *\n*                        *\n**************************\n\n"
    assert captured.out == expected_output
