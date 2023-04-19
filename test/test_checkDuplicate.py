# from testing_base import *
import sys
sys.path.append("./..")
from source.Utilities import checkDuplicate
# initializeGame()

def test_check_yes_duplicate():
    assert(checkDuplicate("Jonny")) == True

def test_check_no_duplicate():
    assert(checkDuplicate("JDog")) == False

def test_check_case_insensitive():
    assert(checkDuplicate("jonny")) == True