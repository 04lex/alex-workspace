"""Bitmap Message
Displays a text message accordeing to the provided bitmap image"""



import sys






bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""


print('Enter the message to display with the bitmap.')
message = input('> ')
if message == '':
    sys.exit()

# Loop over each line in the bitmap:
for line in bitmap.splitlines():
    for i, bit in enumerate(line):
        if bit == ' ':
            # Print an empty space since there's a space in the bitmap:
            print(' ', end='')
        else:
            # Print a character from the message:
            print(message[i % len(message)], end ='')
    print() # Print a new line.