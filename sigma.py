def samogloski(tekst):
	samogloski = set("aeiyou")
	return sum(1 for znak in tekst.lower() if znak in samogloski)

print(samogloski("potemkin basta"))
print(samogloski("six seaven"))
print(samogloski("evil dzień"))
print(samogloski("long sword"))
