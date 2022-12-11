import control as co
import matplotlib.pyplot as plt

D = 0.8

L, R, C = 330e-6, 100, 3.3e-6

G = co.tf([1 - D], [L * C, L / R, (1 - D) ** 2])

t, y = co.step_response(G)

plt.plot(t, 5 * y)

plt.show()
