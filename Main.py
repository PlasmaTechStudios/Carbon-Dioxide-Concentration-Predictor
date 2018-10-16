from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
xs = np.array([], dtype = np.float64)
with open('yearsInDecimalsX.txt', 'r') as xf:
    for xline in xf:
        x = xline
        float(x)
        xs = np.append(xs, float(x))
#parsing and storing data in y value
ys = np.array([], dtype = np.float64)
with open('carbonLevelsY.txt', 'r') as yf:
    for yline in yf:
        y = yline
        float(y)
        ys = np.append(ys, float(y))
def BestFitSlopeAndIntercept(xs,ys):
     m = ((mean(xs) * mean(ys)) - mean(xs * ys)) / ((mean(xs) * mean(xs)) - mean(xs*xs))
     b = mean(ys) - m*mean(xs)
     return m, b 
def squared_error(ys_orig, ys_line):
    return sum((ys_line-ys_orig)**2)
def coefficient_of_determination(ys_orig, ys_line):
    y_mean_line = [mean(ys_orig) for y in ys_orig]
    squared_error_regr = squared_error(ys_orig, ys_line)
    squared_error_y_mean = squared_error(ys_orig, y_mean_line)
    return 1 - (squared_error_regr / squared_error_y_mean)
m, b = BestFitSlopeAndIntercept(xs,ys)
regression_line = [(m*x)+b for x in xs]
predict_input = float(input("Input a year in the future... "))
predict_x = predict_input
predict_y = ((m*predict_x) + b)
r_squared = coefficient_of_determination(ys, regression_line)
print("In the year "  , int(predict_input) ,", carbon dioxide concentrations in the Earth's atmosphere will be about ", round(predict_y, 2) , "ppm")
print(" ")
print("the coefficient of determination for this line is ", r_squared)
#coefficient of determination shows you how good a best fit line is.(values are between 1 and 0. Lower is better)
plt.scatter(xs, ys)
plt.show()
