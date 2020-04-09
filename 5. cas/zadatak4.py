opstine=["Novi Beograd"]

opstine.append("Palilula")
opstine.append("Stari grad")
opstine.append("Vozdovac")
opstine.append("Zemun")
opstine.append("Pancevo")

print(opstine)

print(len(opstine))

opstine.remove("Palilula")
opstine.sort()
print(opstine)

opstine.sort(reverse=True)
print(opstine)
print(opstine.index("Pancevo"))
