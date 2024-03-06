import string
import pytest
import pandas as pd
import hw1

def test_series():
	assert isinstance(hw1.sadie, pd.Series)

# These are the four tests that are for credit. The above is a check 
# for you to use if you would like. 

def test_builddata_type():
	assert isinstance(hw1.builddata(hw1.friends), pd.DataFrame)

def test_builddata_shape():
	expected = (5,2)
	assert hw1.builddata(hw1.friends).shape == expected

def test_smithdata_columns():
	expected = "house"
	assert list(hw1.smithdata(hw1.friends).columns)[0] == expected

def test_smithdata_shape():
	expected = (5,1)
	assert hw1.smithdata(hw1.friends).shape == expected

#tests for question 3

#checks if the person pays enough its giving a tuple back
def test_change_type_enough():
	assert isinstance(hw1.make_change(10, 17.39), tuple)

#checks if its not the correct amount it returns a string saying its not enough
def test_change_type_no():
	assert isinstance(hw1.make_change(10, 2.75), str)

#checks if length of tuple is correct
def test_change_length():
	expected = 6
	assert len(hw1.make_change(10, 17.39)) == expected

#checks if total change is correct
def test_change_correct():
	expected = 7.39
	assert hw1.make_change(10, 17.39)[0] == expected

#checks if nickels are correct
def test_nickels_correct():
	expected = 0
	assert hw1.make_change(10, 17.39)[4] == expected

#checks if pennies given back is correct
def test_pennies_correct():
	expected = 4
	assert hw1.make_change(10, 17.39)[5] == expected
