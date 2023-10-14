""" This program hacks messages encrypted with Caesar Crypter"""







print('Caesar Cipher Hacker')

# Let the user specify the message to hack:
print('Enter the encrypted message to hack:')
message = input('> ')

# Every possible symbol that can be encrypted/decrypted:
# (This must match the SYMBOLS used when crypting the message)
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)): # Loop through every possible key. 
    translated = ''

    # Decrypt each symbol in the message:
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol) # Get the number of the symbol. 
            num = num - key # decrypt the number. 

            # handle the wrap-around if num is less than 0.
            if num < 0:
                num = num + len(SYMBOLS)

            # add decrypted number's symbol to translated:
            translated = translated + SYMBOLS[num]
        else:
            # just add the symbol without decrypting
            translated = translated + symbol

        # Display the key being tested, along with its decrypted text:
        print('Key #{}: {}'.format(key, translated))