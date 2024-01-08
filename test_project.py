import pytest
from unittest.mock import patch
from project import game_board, attempts, r1_position, r2_position, replay

def test_game_board():
    board = ['~'] * 20
    result = game_board(board)

    assert "ROW 1 --- | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ |" in result
    assert "ROW 2 --- | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ | ~ |" in result


def test_attempts_valid_input():
    with patch('builtins.input', return_value='5'):
        result = attempts()
    assert result == 5


def test_attempts_invalid_input_then_valid_input():
    with patch('builtins.input', side_effect=['abc', '6']):
        result = attempts()
    assert result == 6


def test_r1_position_valid_input():
    with patch('builtins.input', return_value='6'):
        result = r1_position()
    assert result == 5

def test_r1_position_invalid_input_then_valid_input():
    with patch('builtins.input', side_effect=['abc', '6']):
        result = r1_position()
    assert result == 5


def test_r2_position_valid_input():
    with patch('builtins.input', return_value='6'):
        result = r2_position()
    assert result == 5


def test_r2_position_invalid_input_then_valid_input():
    with patch('builtins.input', side_effect=['abc', '6']):
        result = r2_position()
    assert result == 5


def test_replay_yes():
    with patch('builtins.input', return_value='yes'):
        result = replay()
    assert result == True


def test_replay_no_entry():
    with patch('builtins.input', return_value=''):
        result = replay()
    assert result == False