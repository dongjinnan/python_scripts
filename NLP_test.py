# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 13:46:14 2020

@author: Jane Dong
"""

def validate(s):
	
	length = len(s)
	if length < 1 or length > 10**4 or length%2 != 0:
		return False
	
	a = s
	count = 0
	while(count < length/2):
		a = a.replace('()', '').replace('{}', '').replace('[]', '')
		count += 1
	
	if len(a) > 0:
		return False
	else:
		return True
		

if __name__ == "__main__":
	print("Please input a string s containing just the characters '(',')','{','}','[',']'.")
	while True:
		s = input('s = ')
		print(validate(s))
