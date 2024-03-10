def array(string):
    split = string.split(",")
    
    if string == "" or len(split) < 3:
        return None
    
    return (" ").join(split[1:-1])