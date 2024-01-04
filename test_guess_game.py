import pytest
from guess_game import game_board, attempts

def test_game_board():
    board = ['~'] * 20
    result = game_board(board)

    assert "ROW 1 ---" in result
    assert "| ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ |" in result
    assert "ROW 2 ---" in result
    assert "| ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ |" in result
