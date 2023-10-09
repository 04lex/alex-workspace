""" Seven-segment display, using it for countdowns, clocks"""
















def getSevSegStr(number, minWidth=0):
    """ Return a seven-segment display string of number. The returned
    string will be padded with zeros if it is similar than minWidth."""

    # Convert number to string in case it's an int or float:
    number = str(number).zfill(minWidth)

    rows = ['', '', '']
    for i, numeral in enumerate(number):
        if numeral == '.': # Render the decimal point.
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += '.'
            continue # Skip the space in between digits.
        elif numeral == '-': # Render the negative sign:
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += '--'
        elif numeral == '0': # Render the 0
            rows[0] += ' '
            rows[1] += '│'
            rows[2] += ' '
