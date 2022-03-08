import pytest
from main import *
import unittest.mock as mock


# inputs for 18.4 bmi
def geninputs():
	inputs = [5, 9, 122]

	for item in inputs:
		yield item


# inputs for 18.5 bmi
def geninputs1():
	inputs = [5, 10, 126]

	for item in inputs:
		yield item


# inputs for 18.6 bmi
def geninputs2():
	inputs = [5, 9, 123]

	for item in inputs:
		yield item


# inputs for 24.9 bmi **
def geninputs3():
	inputs = [6, 0, 179]

	for item in inputs:
		yield item


# inputs for 25.0 bmi **
def geninputs4():
	inputs = [6, 0, 180]

	for item in inputs:
		yield item


# inputs for 25.1 bmi **
def geninputs5():
	inputs = [6, 0, 181]

	for item in inputs:
		yield item


# inputs for 29.9 bmi **
def geninputs6():
	inputs = [6, 0, 215]

	for item in inputs:
		yield item


# inputs for 30 bmi **
def geninputs7():
	inputs = [6, 0, 216]

	for item in inputs:
		yield item


# inputs for 30.1 bmi **
def geninputs8():
	inputs = [6, 0, 217]

	for item in inputs:
		yield item


GEN = geninputs()
GEN1 = geninputs1()
GEN2 = geninputs2()
GEN3 = geninputs3()
GEN4 = geninputs4()
GEN5 = geninputs5()
GEN6 = geninputs6()
GEN7 = geninputs7()
GEN8 = geninputs8()


# Test 18.4 BMI
def test1(monkeypatch, capsys):
	monkeypatch.setattr('builtins.input', lambda _: next(GEN))
	main()
	out, err = capsys.readouterr()
	assert out.strip() == "Underweight"
		

# 29.9, 30, 30.1
