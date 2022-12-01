import control as co
import matplotlib.pyplot as plt
import numpy as np

C1 = 5.08-5
C3 = 6.44e-6
R1 = 3.094e+4
R2 = 6.23e+4

#Gc = (co.tf([1], [C1, 0]) + co.tf([R2], [1])) * co.tf([1], [C3, 0]) / (co.tf([1], [C1, 0]) + co.tf([R2], [1]) + co.tf([1], [C3, 0])) / co.tf([R1], [1])
Gc = co.tf([C1 * R2, 1], [R1 * C1 * C3 * R2, (C1 + C3) * R1, 0])

res = co.bode(Gc)

plt.show()
