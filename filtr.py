def palidro(slowo): 
    slowo = input("Podaj słowo: ").lower()
    
    if slowo == slowo[::-1]:
        print(True)
    else:
        print(False)
print(palidro("kajak"))
palidro("kajak")
