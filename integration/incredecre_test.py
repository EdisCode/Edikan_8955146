# import the test framework
import incredecre

# Unit tests
def test_increment():
    assert incredecre.increment(10) == 11

# These tests are designed to fail for demonstration purposes.
def test_decrement():
    assert incredecre.decrement(3) == 4

def test_incredecrecombined():
    assert incredecre.decrement(incredecre.increment(3)) == 9