import dansplotcore as dpc

from schrodinger import *

n = 500
shape = (n,)

v = np.zeros(shape, dtype=float)

# Gaussian wave packet with momentum
psi = np.zeros(shape, dtype=complex)
packet_x = 100
packet_r = 50
packet_w2 = 20 ** 2  # squared width
packet_p = 0.5  # momentum
for x in range(packet_x - packet_r, packet_x + packet_r + 1):
    d2= (x - packet_x) ** 2
    psi[x] = np.exp(-d2 / packet_w2 + 1j * x * packet_p)

hamiltonian = hamiltonian_single_particle(psi, v, 1, 1)

plot = dpc.Plot(primitive=dpc.p.LineComplexY())

class Updater:
    def __init__(self):
        self(0)

    def __call__(self, dt):
        plot.clear()
        for _ in range(1000):
            evolve(psi, hamiltonian, 0.001)
        plot.plot(probability(psi))
        plot.plot(psi)

plot.show(update=Updater())
