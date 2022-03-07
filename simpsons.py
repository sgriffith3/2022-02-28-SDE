#!/usr/bin/python3
"""Alta3 Research | Building functions to test"""
# the homer function expects a word to be passed to it
# if it is not given one, it assumes the default "salad"
def homer(sd="salad"):
   return f"You don't win friends with {sd}"

# the milhouse function expects a word to be passed to it
# if it is not given one, it assumes the default "milhouse"
def milhouse(mh="milhouse"):
    return f"Everything is coming up {mh}"

# the troymcclure function expects a word to be passed to it
# if it is not given one, it assumes the default 3
def troymcclure(tm=3):
    if tm > 2:
        return f"2 minus {tm} equals negative fun!"
    else:
        return None

# tests MUST begin with the word test_ or they will be ignored
def test_homer():
    # assert will return true or raise an AssertionError
    # the primary application is debugging
    assert homer("doughnuts") == "You don't win friends with doughnuts"

# tests MUST begin with the word test_ or they will be ignored
def test_milhouse():
    # assert will return true or raise an AssertionError
    # the primary application is debugging
    assert milhouse("daffodils") == "Everything is coming up daffodils"

# tests MUST begin with the word test_ or they will be ignored
def test_troymcclure():
    assert troymcclure(5) == "2 minus 5 equals negative fun!"
    assert not troymcclure(1)

# testing a failure
def test_homer_fail():
    # This should produce a failure.
    assert homer("pretzels") != "You don't win friends with salad"

