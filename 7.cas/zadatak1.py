ime=input("Unesite ime Petar:")
'''
while ime.lower()!="petar" and ime.lower()!="петар":
    ime=input("Uneli ste pogresno ime, pokusajte ponovo:")

'''

while ime.upper() not in ["PETAR","ПЕТАР"]:
    ime=input("Uneli ste pogresno ime, pokusajte ponovo:")




print("Bravo, uneli ste ispravno ime.")
