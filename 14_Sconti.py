jeans1 = int(input("Inserisci il prezzo del primo jeans: "))
jeans2 = int(input("Inserisci il prezzo del secondo jeans: "))
sconto = 0.20
prezzoTotale = jeans1 + jeans2
prezzoScontato = prezzoTotale - (prezzoTotale * sconto)
print("Il prezzo scontato è: ", prezzoScontato)
banconote = int(input("Inserisci i contanti: "))
resto = banconote - prezzoScontato
print("Il resto è: ", resto)