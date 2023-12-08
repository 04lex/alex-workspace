import datetime

def este_bisect(an):
    """
    dacă (anul este divizibil cu 4 și anul nu este divizibil cu 100) atunci (an bisect)
    dacă (anul este divizibil cu 400) atunci (an bisect)
    altfel (an obișnuit)

    Args:
        an ([int]): [description]

    Returns:
        [bool]: [description]
    """
    return (an % 400 == 0) or ( (an % 100) and (an % 4 == 0) )


def get_year_month_day(cnp):

    start_year = "20" if cnp[0] in ["5", "6"] else "19"

    year = f"{start_year}{cnp[1]}{cnp[2]}"
    year = int(year)

    month = f"{cnp[3]}{cnp[4]}"
    month = int(month)

    day = f"{cnp[5]}{cnp[6]}"
    day = int(day)

    return (year, month, day)


def get_varsta(cnp):
    year, month, day = get_year_month_day(cnp)

    birthday = datetime.datetime(year, month, day)
    today = datetime.datetime.now()

    varsta = today.year - birthday.year - ((birthday.month > today.month) or (birthday.month == today.month) and (birthday.day > today.day))

    return varsta

def este_baiat(cnp):
    return True if cnp[0] in ["1", "5"] else False

def este_fata(cnp):
    return True if cnp[0] in ["2", "6"] else False


def are_varsta_de_buletin(cnp):
    if cnp[0] in ["1", "2"]:
        return True

    varsta = get_varsta(cnp)

    return varsta >= 14




def este_cnp_valid(cnp):
    if len(cnp) != 13:
        return False

    if not cnp.isnumeric():
        return False

    if not cnp[0] in ["1", "2", "5", "6"]:
        return False


    year, month, day = get_year_month_day(cnp)

    if month not in range(1, 13):
        return False

    ## V1
    # if month in [4, 6, 9, 11]:
    #     if day not in range(1, 31):
    #         return False
    #     else:
    #         if day not in range(1, 32):
    #             return False

    ## V2
    if month in [4, 6, 9, 11]:
        MAX_DAYS = 30
    ## EX: 29 februrarie, 30 februarie, 31 aprilie, etc
    elif month == 2:
        MAX_DAYS = 28 + este_bisect(year)
    else:
        MAX_DAYS = 31

    if day not in range(1, MAX_DAYS + 1):
        return False


    



    if not are_varsta_de_buletin(cnp):
        return False

    return True

def are_voie_in_club(cnp):
    varsta = get_varsta(cnp)
    baiat = este_baiat(cnp)
    fata = este_fata(cnp)

    if varsta > 70 or varsta < 16:
        return False

    if varsta < 18 and baiat:
        return False

    if varsta < 16 and fata:
        return False

    return True


    