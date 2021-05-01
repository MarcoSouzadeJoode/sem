import Sieves
import numpy as np
from timeit import repeat
import matplotlib.pyplot as plt


Ns = np.linspace(10, 1*10**4, 30, dtype="int64")



# nemusíme importovat všechny funkce ručně
funcs = [func for func in dir(Sieves) if func[0] != "_"]
funcs.remove("np")
funcs.remove("deque")


times_matrix = []

for func in funcs:
	times = []
	for N in Ns:
		siv = f"Sieves.{func}({N})"
		print(siv)
		times.append(min(repeat(siv, number=1, repeat=2, globals=globals())))
	times_matrix.append(np.array(times))

for i,times in enumerate(times_matrix):
	plt.scatter(Ns, times*1000, label=f"{funcs[i]}")

plt.legend(fontsize=20)
plt.ylabel("T (ms)", fontsize=15)
plt.xlabel("N", fontsize=15)
plt.show()
