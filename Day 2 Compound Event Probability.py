from fraction import Fraction

#declaring data
x=[4,3]
y=[5,4]
z=[4,4]

#calculating probabilities ffor red
x_red = x[0] / sum(x)
y_red = y[0] / sum(y)
z_red = z[0] / sum(z)

#calculating probablity
probablity =(x_red * y_red * (1 - z_red)) + (x_red * (1 - y_red)* z_red) + ((1 - x_red)* y_red* z_red)

probablity1 = Fraction(probablity).limit_denominator()
print(probablity1)

