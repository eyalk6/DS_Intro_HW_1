#A

def my_func(x1, x2, x3):
    try:
        if (not isinstance(x1, float)) or (not isinstance(x2, float)) or (not isinstance(x3, float)):
            return ("Error: parameters should be float")
        num = (x1+x2+x3)*(x2+x3)*x3
        denominator = x1+x2+x3
        return num/denominator
    except:
        return ("Not a number – denominator equals zero")
  
     
#B

def convert(hours, minutes):
    if (hours<0) or (minutes<0):
        return ("Input error!")
    hours = hours*(60*60)
    minutes = minutes*60
    return hours + minutes

