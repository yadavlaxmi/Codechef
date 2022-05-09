def is_leap(year):
    leap = True
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return leap  
            else:
                return False
        else:
            return leap
    else:
        return False
# LEAP_YEAR