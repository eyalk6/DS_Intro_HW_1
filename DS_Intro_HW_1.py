def my_func(x1, x2, x3):
    try:
        if (not isinstance(x1, float)) or (not isinstance(x2, float)) or (not isinstance(x3, float)):
            return ("Error: parameters should be float")
        num = (x1+x2+x3)*(x2+x3)*x3
        denominator = x1+x2+x3
        return num/denominator
    except:
        return ("Not a number – denominator equals zero")



my_func(2.8, 2.9, 3.0)   
     
