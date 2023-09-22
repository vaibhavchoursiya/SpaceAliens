from game_database import *

def test_datebase_fuc():
    """"Test Write Data function."""
    write_data(data=12)
    highscore = read_data()
    assert highscore == "12"
