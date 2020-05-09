proizvod=1

for i in range(4,51):
    if i%6==0:
        proizvod=proizvod*i
        #proizvod*=i
        
print(f"proizvod je {proizvod}")