# Aufgabe 1:
# Schreiben Sie ein Python-Programm, das
# 1) den Benutzer begrüßt
# 2) eine erste Zahl entgegen nimmt
# 3) eine zweite Zahl entgegen nimmt
# 4) die Summe der beiden Zahlen berechnet und ausgibt
# 5) die Differenz der beiden Zahlen berechnet und ausgibt
# 6) das Produkt der beiden Zahlen berechnet und ausgibt
# 7) den Quotienten der beiden Zahlen berechnet und ausgibt

#1
print("Hallo lieber Benutzer!")

#2
erste_zahl_string = input("Eingabe einer ersten Zahl:")
erste_zahl = int(erste_zahl_string)
print("Die Eingabe für die erste Zahl lautete:", erste_zahl)

#3
zweite_zahl_string = input("Eingabe einer zweiten Zahl:")
zweite_zahl = int(zweite_zahl_string)
print("Die Eingabe für die zweite Zahl lautete:", zweite_zahl)

#4
print("Summe:",erste_zahl+zweite_zahl)

#5
print("Differenz:",erste_zahl-zweite_zahl)

#6
print("Produkt:",erste_zahl*zweite_zahl)

#7
print("Ouotient:",erste_zahl/zweite_zahl)
