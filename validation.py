import Sieves
import numpy as np

N = 1000

# nemusíme importovat všechny funkce ručně
funcs = [func for func in dir(Sieves) if func[0] != "_"]
funcs.remove("np")
funcs.remove("deque")

# vytiskneme všechna prvočísla menší než N,
# uložíme do seznamu

prime_matrix = []

for func in funcs:
	siv = getattr(Sieves, func)
	a = siv(N)
	prime_matrix.append(a)


for i, a in enumerate(prime_matrix):
	print(a)
	for j, b in enumerate(prime_matrix):
		if a.all() == b.all():
			print("OK")
		else:
			print(f"Mismatch between function {i} and {j}")

