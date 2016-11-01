'''
One day, the Grasshopper was jumping on the lawn and found a piece of paper with a string. Grasshopper became interested what is the minimum jump ability he should have in order to be able to reach the far end of the string, jumping only on vowels of the English alphabet. Jump ability is the maximum possible length of his jump.

Formally, consider that at the begginning the Grasshopper is located directly in front of the leftmost character of the string. His goal is to reach the position right after the rightmost character of the string. In one jump the Grasshopper could jump to the right any distance from 1 to the value of his jump ability.

The following letters are vowels: 'A', 'E', 'I', 'O', 'U' and 'Y'.

'''

letters = list(input().strip())

jumpAbility = 0
i = 1
for letter in letters:
	if(letter in ('A', 'E', 'I', 'O', 'U', 'Y')):
		i = 1
	else: 
		i += 1
	
	if(i > jumpAbility):
		jumpAbility = i
print(jumpAbility)


