# simple linear regression f(x)

# x is the input and y is the output
def slope_intercept_simple_linear_regression(x, y):
    
    # compute the sum of input and output
    sum = x + y
    
    # compute the product of the output and the input and its sum
    product = x * y
    sum_of_product = product.sum()
    
    # compute the squared value of the input and its sum
    x_squared = x * x
    sum_x_squared = x_squared.sum()
    
    # use the formula for the slope
    numerator = sum_of_product - ((x.sum() * y.sum()) / x.size())
    denominator = sum_x_squared - ((x.sum() * x.sum()) / x.size())
    slope = numerator / denominator
    
    # use the formula for the intercept
    intercept = y.mean() - (slope * x.mean())
    
    # returns intercept and slope
    return (intercept, slope)

