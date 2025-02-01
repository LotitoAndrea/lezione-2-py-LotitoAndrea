kgPesce = float(input("Inserisci il kg di pesce: "))
prezzoKgPesce = float(input("Inserisci il prezzo al kg del pesce: "))
prezzoTotale = kgPesce * prezzoKgPesce
print("Il prezzo totale è: ", prezzoTotale)
banconote = int(input("Inserisci i contanti che si vogliono pagare: "))
resto = banconote - prezzoTotale
print("Il resto è: ", resto)