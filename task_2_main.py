from numpy import sqrt, tan, pi, cos

g = 9.8
h = 6.62607015e-34
k = 1.38064852e-23
e = 2.7182818284

print(sqrt((g * 100 * tan(30)**2) / (2 * cos(pi / 3)**2 * (1 - tan(30) * tan(pi / 3)))))

print((2 / sqrt(pi)) * (h / ((k * 200)**(3/2))) * (e**(-300 / k * 200)) * (300**(200 / 2)))