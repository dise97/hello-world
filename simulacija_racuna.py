banane=1
hljeb=5
mlijeko=1
jabuke=3

potrebno_je_kupiti = ["banane", "hljeb","mlijeko", "jabuke"]
print("Potrebno je kupiti:", potrebno_je_kupiti)
def sracunaj(banane):
    if banane == 1:
        print("Kupio sam banane i koštalo je:",banane*3, "KM")
    else:
        print("Nisam kupio što je bilo potrebno.")

sracunaj(banane)
del potrebno_je_kupiti[0]
ostalo_je_kupiti = potrebno_je_kupiti
print("Ostalo je kupiti:",ostalo_je_kupiti)


def sracunaj(hljeb):
    if banane == 1:
        print("Kupio sam hljeb i koštalo je:",hljeb*1, "KM")
    else:
        print("Nisam kupio što je bilo potrebno.")

sracunaj(hljeb)
del potrebno_je_kupiti[0]
ostalo_je_kupiti1 = ostalo_je_kupiti
print("Ostalo je kupiti:", ostalo_je_kupiti1)

def sracunaj(mlijeko):
    if banane == 1:
        print("Kupio sam mlijeko i koštalo je:",mlijeko*1.5, "KM")
    else:
        print("Nisam kupio što je bilo potrebno.")

sracunaj(mlijeko)
del potrebno_je_kupiti[0]
ostalo_je_kupiti2 = ostalo_je_kupiti1
print("Ostalo je kupiti:",ostalo_je_kupiti2)

def sracunaj(jabuke):
    if banane == 1:
        print("Kupio sam jabuke i koštalo je:",jabuke*1.5, "KM")
    else:
        print("Nisam kupio što je bilo potrebno.")

sracunaj(jabuke)
del potrebno_je_kupiti[0]
ostalo_je_kupiti3=ostalo_je_kupiti2
print("Ostalo je kupiti:",ostalo_je_kupiti3)
racun = (jabuke*1.5+hljeb*1+banane*3+mlijeko*1.5)
print("Moram platiti:", racun, "KM")
