def days_in_month(year, month):
    """
    Return the number of days based on the year and month given. We will check if the year and month are affected by a leap year.
    
    Arguments:
        int(object): the year we want to evaluate.
        int(object): the month we want to evaluate.
    
    Returns:
        int(object): the number of days that exist in the year and month given.
    """
    # check if it's a valid month name:
    if month not in (
        1,2,3,4,5,6,7,8,9,10,11,12):
        # print to please enter in a valid month name:
        print("Please enter a valid month number")
    # else clause:
    else:
        # check if it's a leap year and month of feburary:
        if year % 4 ==0 and month == 2:
            # return 29 days:
            return 29
        # check if it's not a leap year and the month of feburary:
        elif year % 4 !=0 and month == 2:
            # return 28 days:
            return 28
        # check if it's not a leap year and not the month of feburary:
        elif year % 4 != 0 and month != 2:
            # then check if it's a month with 30 days:
            if month in (4, 6, 9, 11):
                # return 30 days:
                return 30
            # else return 31 days:
        # else return 31 days:
        else:
            return 31