from lab03 import multiply
from lab03 import collectOddValues
from lab03 import countInts
from lab03 import reverseString
from lab03 import removeSubString
import pytest

def test_multiply():
    assert multiply(5,4) == 20
    assert multiply(0,4) == 0
    assert multiply(5,0) == 0
    assert multiply(1,1) == 1

def test_collectOddValues():
    assert collectOddValues([1,2,3,4,5]) == [1,3,5]
    assert collectOddValues([1,1,1,1,1,1]) == [1,1,1,1,1,1]
    assert collectOddValues([5,4,3,2,1]) == [5,3,1]
    assert collectOddValues([2,4,6,8,10]) == []

def test_countInts():
    assert countInts([], 2) == 0
    assert countInts([2,2,2,2,2,2,2,2,2], 2) == 9
    assert countInts([1,2,3,4,3,2,1], 5) == 0
    assert countInts([18,2,3,4,3,2,1], 18 ) == 1

def test_reverseString():
    assert reverseString("CMPSC9") == "9CSPMC" 
    assert reverseString("") == ""
    assert reverseString("rACecar") == "raceCAr"
    assert reverseString("9.0") == "0.9"

def test_removeSubString():
    assert removeSubString("Lolololol", "lol") == "Loo"
    assert removeSubString("Lolololol", "") == "Lolololol"
    assert removeSubString("", "lol") == ""
    assert removeSubString("abc", "d") == "abc"
    assert removeSubString("xyxyxyxyxyxyxyxyxyxyxyxyxy", "xy") == ""

