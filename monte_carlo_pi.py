import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_pi(n):

    x = np.random.uniform(-1, 1, n)
    y = np.random.uniform(-1, 1, n)

    D = x**2 + y**2

    nb_points = np.sum(D <= 1)

    pi_estime = 4 * nb_points / n

    return pi_estime


def convergence_pi():

    T = [10, 100, 1000, 10000, 100000, 1000000, 10000000]

    estimations = []
    erreurs = []

    for n in T:

        pi_estime = monte_carlo_pi(n)

        estimations.append(pi_estime)

        erreur = abs(pi_estime - np.pi)

        erreurs.append(erreur)

    return T, estimations, erreurs


T, estimations, erreurs = convergence_pi()

print("Estimations :", estimations)
print("Erreurs :", erreurs)

# Graphique 1 : convergence vers pi

plt.figure(figsize=(8,5))

plt.plot(T, estimations, marker='o', label="Monte Carlo")

plt.axhline(np.pi, color='r', label="True value of pi")

plt.xscale('log')

plt.xlabel("Number of simulations")
plt.ylabel("Estimated value of pi")
plt.title("Monte Carlo estimation of pi")

plt.legend()

plt.show()


# Graphique 2 : erreur

plt.figure(figsize=(8,5))

plt.plot(T, erreurs, marker='o')

plt.xscale('log')
plt.yscale('log')

plt.xlabel("Number of simulations")
plt.ylabel("Absolute Error")

plt.title("Error of Monte Carlo estimation")

plt.show()
