def race(v1, v2, g):
    if v1 >= v2:
        return None
    
    # calculate time to catch up using formula: lead / (B speed - A speed)
    # convert to seconds by multiplying by 3600 (number of seconds per hour)
    total_seconds = int((g / (v2 - v1)) * 3600)
    
    # calculate hours by dividing total_seconds by 3600 (number of seconds per hour)
    hours = total_seconds // 3600

    # calculate minutes by first finding the remainder of the calculation above to find hours
    # divide the remainder by 60 (number of seconds per minute)
    minutes = (total_seconds % 3600) // 60

    # calculate seconds by finding the remainder of the calculation to find minutes (60 seconds per minute)
    seconds = total_seconds % 60

    # return formatted results
    return [hours, minutes, seconds]
