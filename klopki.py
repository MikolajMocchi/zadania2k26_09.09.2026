def minmaksim(list):
	minimal = min(list)
	maksimal = max(list)

	return (minimal, maksimal)

liczby = (6, 7, 123,420,76,10,1)

wynik = minmaksim(liczby)

print(wynik)