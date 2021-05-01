import Sieves
import numpy as np
from timeit import repeat
import matplotlib.pyplot as plt

# maximální horní mez pro síta
MAX = 10**6

# prostor horních mezí pro hledání prvočísel
# dolní mez nechme na čísle > 2
Ns = np.linspace(10, MAX, 30, dtype="int64")



# nemusíme importovat všechny funkce ručně
funcs = [func for func in dir(Sieves) if func[0] != "_"]


# odstranění nevyhovujícího
funcs.remove("np")
funcs.remove("deque")


# matice výsledných časů
times_matrix = []

# časování jednotlivých sít
for func in funcs:
	times = []
	for N in Ns:
		siv = f"Sieves.{func}({N})"
		print(siv)
		times.append(min(repeat(siv, number=1, repeat=2, globals=globals())))
	times_matrix.append(np.array(times))


# vykreslení grafů
for i,times in enumerate(times_matrix):
	plt.scatter(Ns, times*1000, label=f"{funcs[i]}")


# popisy os, legenda atp.
plt.legend(fontsize=20)
plt.ylabel("T (ms)", fontsize=15)
plt.xlabel("N", fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()
