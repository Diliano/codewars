import math

def race(v1, v2, g):
    if v1 >= v2:
        return None
    
    # calculate time to catch up using the formula lead / speed difference (calculated using speed B - speed A)
    time = g / (v2 - v1)
    # calculate hours using the integer value of time
    hours = int(time)
    # calculate minutes by mutiplying the decimal part of hours by 60
    minutes = (time - hours) * 60
    # calculate seconds by multiplying the decimal part of minutes by 60
    seconds = (minutes - int(minutes)) * 60
    
    # return formatted list, using the integer value of minutes and rounding seconds down as instructed in the kata
    return [hours, int(minutes), math.floor(seconds)]