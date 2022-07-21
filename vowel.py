import re
a = input("Enter the word:\n")
c = re.compile('[^aeiouAEIOU]')
if(len(c.findall(a))):
	print("it is not a vowel") 
else:
	print("it is a vowel") 