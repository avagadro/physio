import  sys, random
#import pyperclip
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def main():
 myMessage = raw_input('enter the message to be encrypted or decrypted \n')
 myKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
 #LFWOAYUISVKMNXPBDCRJTQEGHZ
 #myMode = 'encrypt' # set to 'encrypt' or 'decrypt'
# myMode = raw_input('enter whether encryption or decryption is required \n')
 #if myMode == 'encrypt':
  #translated = encryptMessage(myKey, myMessage)
 #elif myMode == 'decrypt':
  #translated = decryptMessage(myKey, myMessage)
 print('Using key %s' % (myKey))
 Ciphertext=encryptMessage(myKey, myMessage)
 Plaintext=decryptMessage(myKey, Ciphertext)
 print('The encrpyted message is:\n'+Ciphertext+'|\n')
 print('The decrypted message is:\n'+Plaintext+'|\n')
 #print('The %sed message is:' % (myMode))
 #print(translated)
 #pyperclip.copy(translated)
 #print()
 
def encryptMessage(key, message):
 translated = ''
 charsA = LETTERS
 charsB = key
 for symbol in message:
  if symbol.upper() in charsA:
# encrypt/decrypt the symbol
   symIndex = charsA.find(symbol.upper())
  if symbol.isupper():
   translated += charsB[symIndex].upper()
  if symbol.islower():
   translated += charsB[symIndex].lower()
  else:
   translated += symbol # symbol is not in LETTERS, just add it
 return translated

 #return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
 translated = ''
 charsB = LETTERS
 charsA = key
 for symbol in message:
  if symbol.upper() in charsA:
# encrypt/decrypt the symbol
   symIndex = charsA.find(symbol.upper())
  if symbol.isupper():
   translated += charsB[symIndex].upper()
  if symbol.islower():
   translated += charsB[symIndex].lower()
  else:
   translated += symbol # symbol is not in LETTERS, just add it
 return translated

 #return translateMessage(key, message, 'decrypt')

#def translateMessage(key, message, mode):
 #translated = ''
 #charsA = LETTERS
 #charsB = key
 #if mode == 'decrypt':
# For decrypting, we can use the same code as encrypting. We
# just need to swap where the key and LETTERS strings are used.
  #charsA, charsB = charsB, charsA
# loop through each symbol in the message
 #for symbol in message:
  #if symbol.upper() in charsA:
# encrypt/decrypt the symbol
   #symIndex = charsA.find(symbol.upper())
  #if symbol.isupper():
   #translated += charsB[symIndex].upper()
  #if symbol.islower():
   #translated += charsB[symIndex].lower()
  #else:
   #translated += symbol # symbol is not in LETTERS, just add it
 #return translated

def getRandomKey():
 key = list(LETTERS)
 random.shuffle(key)
 return ''.join(key)

if __name__ == '__main__':
 main()
