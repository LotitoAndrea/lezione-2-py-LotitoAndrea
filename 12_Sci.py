numeroStudenti = int(input("Inserisci il numero degli studenti: "))
pesoStudenti = float(input("Inserisci il peso degli studenti: "))
pesoSciBorsone = 5
pesoTotale = numeroStudenti * (pesoStudenti + pesoSciBorsone)
print("Il peso totale è: ", pesoTotale, "kg")