#This function return yes or no input String
def YesOrNo (str):
    newStr = str.upper()
    if(newStr == "YES"):
        return 0
    elif(newStr == "NO"):
        return 1
    else:
        return 2