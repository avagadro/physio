#Title-  Double Transposition Cipher
#Amey Deshmukh
#BE EXTC
#Roll No. 14

import math

def main():
	myMessage = input("Enter your message:-> ")
	myKey = input("Enter the key1 in terms of no. of columns:-> ")
	myKey1 = input("Enter the key2 in terms of no. of columns:-> ")
	myKey=int(myKey)
	myKey1=int(myKey1)	
	# Encryption stage I
	ciphertext1 = encryptMessage(myKey, myMessage)

	#Encryption stage II	
	ciphertext = encryptMessage(myKey1, ciphertext1)
   
	# Print the encrypted string in ciphertext to the screen, with
	# a | (called "pipe" character) after it in case there are spaces at
	# the end of the encrypted message.
	print ("\nThe encrypted message is:-> %s" %ciphertext + '|')

# Decryption stage I
	plaintext1 = decryptMessage(myKey1, ciphertext)
# Decryption stage II
	plaintext = decryptMessage(myKey, plaintext1)

	# Print with a | (called "pipe" character) after it in case
	# there are spaces at the end of the decrypted message.
	print ("\nThe decrypted message is:-> %s" %plaintext)

def encryptMessage(key, message):
	# Each string in ciphertext represents a column in the grid.
	ciphertext = [''] * key
	
	# Loop through each column in ciphertext.
	for col in range(key):
		pointer = col

	 # Keep looping until pointer goes past the length of the message.
		while pointer<len(message):
			# Place the character at pointer in message at the end of the
			# current column in the ciphertext list.
			ciphertext[col] += message[pointer]
  			
			# move pointer over
			pointer += key

	 # Convert the ciphertext list into a single string value and return it.
	return ''.join(ciphertext)

def decryptMessage(key, message):
	# The transposition decrypt function will simulate the "columns" and
	# "rows" of the grid that the plaintext is written on by using a list
	# of strings. First, we need to calculate a few values.
	
	# The number of "columns" in our transposition grid:
	numOfColumns = math.ceil(float(len(message) )/ key)
	numOfColumns = int(numOfColumns)
	
	# The number of "rows" in our grid will need:
	numOfRows = key
	# The number of "shaded boxes" in the last "column" of the grid:
	numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
	
	# Each string in plaintext represents a column in the grid.
	plaintext = [''] * numOfColumns
     
	# The col and row variables point to where in the grid the next
	# character in the encrypted message will go.
	col = 0
	row = 0
	for symbol in message:
		plaintext[col] += symbol
		col += 1 # point to next column
		# If there are no more columns OR we're at a shaded box, go back to
		# the first column and the next row.
		if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
			col = 0
			row += 1
	return ''.join(plaintext)

# If amey52.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
	main()
