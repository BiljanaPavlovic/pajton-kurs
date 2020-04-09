namirnice=[["hleb",30],["jaja",14]]

print(namirnice[0][1])

namirnice[0].append(int(input("Unesite kolicinu hleba:")))

namirnice[1].append(int(input("Unesite kolicinu jaja:")))

trosak=namirnice[0][1]*namirnice[0][2]+namirnice[1][1]*namirnice[1][2]

print(namirnice)
print("Ukupan trosak je:",trosak)

