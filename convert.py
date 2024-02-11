def CelsiusToFahr(cel):
    try:
        cel = float(cel)
        fahr = (cel * 1.8) + 32
        return fahr
    except ValueError:
        # handle case that its not a valid input
        return "Not a valid Input"
    
'''
def CelsiusToKelv(cel):
    kelv = (cel + 273.15)
    return kelv

def FahrToCel(fahr):
    cel = (fahr - 32) * 5/9
    return cel

def FahrToKel(fahr):
    kelv = (fahr - 32) * 5/9
    return kelv

def KelvToCel(kelv):
    cel = (kelv - 273.15)
    return cel

def KelvToFahr(kelv):
    fahr = (kelv - 273.15) * 9/5 +32
    return fahr
'''